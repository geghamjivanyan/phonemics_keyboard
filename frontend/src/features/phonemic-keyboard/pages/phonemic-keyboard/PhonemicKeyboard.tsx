import { useState, useEffect, useRef, useCallback } from "react";
import { API_BASE_URL } from "../../../../config/config.ts";
import { useDebounce } from "../../hooks";
import { DOT_TRANSFORMATIONS, arabicPhonemicTransformer } from "../../utils";
import {
  KeyboardActions,
  type KeyboardKey,
  type SearchResponse,
} from "../../interface";
import { KeyboardVersion } from "../../constant";
import { Keyboard } from "../../components/keyboard";
import { TypedText } from "../../components/typed-text";
import styles from "./PhonemicKeyboard.module.css";

const INITIAL_SPACE = " ";

export const PhonemicKeyboard = () => {
  const [transformedText, setTransformedText] = useState<string>(INITIAL_SPACE);
  const [rhythms, setRhythms] = useState<string[]>([]);
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [selectedRhythm, setSelectedRhythm] = useState<string>();
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isHamza, setIsHamza] = useState<boolean>(false);
  const [lastOperation, setLastOperation] = useState<{
    type: "insert" | "delete" | "replace" | "transform" | "api";
    data?: unknown;
  } | null>(null);
  const [keyboardVersion, setKeyboardVersion] = useState<KeyboardVersion>(
    KeyboardVersion.One,
  );
  const keyboardSwitchPendingRef = useRef(keyboardVersion);

  const debouncedText = useDebounce<string>(transformedText);
  const applyTransformation = useCallback(() => {
    // Skip transformation if the last operation was already a transformation or API update
    if (lastOperation?.type === "transform" || lastOperation?.type === "api") {
      return;
    }

    const newTransformedText = arabicPhonemicTransformer(transformedText);

    if (newTransformedText !== transformedText) {
      setTransformedText(newTransformedText);
      setLastOperation({ type: "transform" });
    }
  }, [transformedText, lastOperation]);

  useEffect(() => {
    // Only apply transformations for insert and replace operations
    if (lastOperation?.type === "insert" || lastOperation?.type === "replace") {
      applyTransformation();
    }
  }, [lastOperation, applyTransformation]);

  useEffect(() => {
    const controller = new AbortController();
    void fetchSuggestions(controller.signal);
    return () => controller.abort();
  }, [debouncedText, selectedRhythm, keyboardVersion]);

  useEffect(() => {
    const onKeyDown = (e: KeyboardEvent): void => {
      if (e.key !== "Enter") return;
      handleEnter();
      e.preventDefault();
    };

    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [suggestions, transformedText]);

  const fetchSuggestions = async (signal: AbortSignal): Promise<void> => {
    if (debouncedText.trim() === "") {
      setRhythms([]);
      setSuggestions([]);
      setIsHamza(false);
      return;
    }

    setIsLoading(true);
    try {
      const hasKeyboardChanged =
        keyboardSwitchPendingRef.current !== keyboardVersion;
      keyboardSwitchPendingRef.current = keyboardVersion;

      const response = await fetch(`${API_BASE_URL}/search/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: debouncedText,
          rhythms: selectedRhythm,
          keyboard: keyboardVersion,
          keyboardChanged: hasKeyboardChanged,
        }),
        signal,
      });

      const responseData: SearchResponse = await response.json();
      setRhythms(responseData.data.rhythms || []);
      setSuggestions(responseData.data.suggestions || []);
      setIsHamza(responseData.data.isHamza || false);

      if (responseData.data.text && responseData.data.text !== debouncedText) {
        setTransformedText(responseData.data.text);
        setLastOperation({ type: "api", data: responseData.data.text });
      }
    } catch (error: unknown) {
      console.error("Error fetching suggestions:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const insertCharacter = (char: string): void => {
    setTransformedText((prev: string) => prev + char);
    setLastOperation({ type: "insert", data: char });
  };

  const handleEnter = (): void => {
    if (suggestions.length > 0) {
      handleSuggestionClick(suggestions[0]);
    } else {
      console.log("ENTER", transformedText);
    }
  };

  const deleteLastCharacter = (): void => {
    setTransformedText((prev) =>
      prev.length > INITIAL_SPACE.length ? prev.slice(0, -1) : INITIAL_SPACE,
    );
    setLastOperation({ type: "delete" });
  };

  const switchKeyboard = (): void => {
    setKeyboardVersion((v) =>
      v === KeyboardVersion.One ? KeyboardVersion.Two : KeyboardVersion.One,
    );
  };

  const handleDotInput = (): void => {
    const last = transformedText.at(-1) ?? "";
    const repl = DOT_TRANSFORMATIONS[last];

    setTransformedText((prev) => {
      return repl ? prev.slice(0, -1) + repl : prev + ".";
    });

    setLastOperation({
      type: repl ? "replace" : "insert",
      data: repl ? { original: last, replacement: repl } : ".",
    });
  };

  const handleSuggestionClick = (suggestion: string): void => {
    if (isHamza) {
      setTransformedText((prev: string) => {
        const trimmed = prev.trimEnd();
        if (trimmed === "") return suggestion + " ";

        const lastSpaceIndex = trimmed.lastIndexOf(" ");
        const newText =
          lastSpaceIndex === -1
            ? suggestion + " "
            : trimmed.substring(0, lastSpaceIndex + 1) + suggestion + " ";

        return newText + prev.slice(trimmed.length);
      });
      setLastOperation({ type: "replace", data: suggestion });
    } else {
      setTransformedText((prev) => prev + suggestion);
      setLastOperation({ type: "insert", data: suggestion });
    }
  };

  const handleRhythmClick = (rhythm: string): void => {
    setSelectedRhythm(rhythm);
  };

  const handleKeyClick = (key: KeyboardKey): void => {
    switch (key.action) {
      case KeyboardActions.ENTER:
        handleEnter();
        break;
      case KeyboardActions.DELETE:
        deleteLastCharacter();
        break;
      case KeyboardActions.SPACE:
        insertCharacter(key.arabic);
        break;
      case KeyboardActions.SWITCH_KEYBOARD:
        switchKeyboard();
        break;
      case KeyboardActions.DOT:
        handleDotInput();
        break;
      default:
        insertCharacter(key.arabic);
        break;
    }
  };

  return (
    <div className={styles.keyboardContainer}>
      <Keyboard version={keyboardVersion} onKeyClick={handleKeyClick} />
      <TypedText
        typedText={transformedText}
        rhythms={rhythms}
        suggestions={suggestions}
        isLoading={isLoading}
        onSuggestionSelect={handleSuggestionClick}
        onRhythmSelect={handleRhythmClick}
      />
    </div>
  );
};
