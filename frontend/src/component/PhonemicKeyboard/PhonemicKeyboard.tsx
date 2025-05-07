import { CSSProperties, useState, useEffect, useCallback } from "react";
import { useDebounce } from "../../hook";
import {
  DOT_TRANSFORMATIONS,
  KEYBOARD_1,
  KEYBOARD_2,
  arabicPhonemicTransformer,
} from "../../util";
import { KeyboardActions, KeyboardKey, SearchResponse } from "../../interface";
import { API_BASE_URL } from "../../config";
import { HexKeyButton } from "../HexKeyButton";
import { TypedText } from "../TypedText";
import "./PhonemicKeyboard.css";

const SWITCH_LABEL: Record<"k1" | "k2", string> = {
  k1: "تشكيل",
  k2: "إهمال",
} as const;

const getSwitchLabel = (kb: KeyboardKey[][]): string =>
  kb === KEYBOARD_1 ? SWITCH_LABEL.k1 : SWITCH_LABEL.k2;

const INITIAL_SPACE = " ";

export const PhonemicKeyboard = () => {
  const [transformedText, setTransformedText] = useState<string>(INITIAL_SPACE);
  const [activeKeyboard, setActiveKeyboard] =
    useState<KeyboardKey[][]>(KEYBOARD_1);
  const [rhythms, setRhythms] = useState<string[]>([]);
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [selectedRhythm, setSelectedRhythm] = useState<string>();
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isHamza, setIsHamza] = useState<boolean>(false);
  const [lastOperation, setLastOperation] = useState<{
    type: "insert" | "delete" | "replace" | "transform" | "api";
    data?: any;
  } | null>(null);

  const withDiacritics = activeKeyboard === KEYBOARD_1;
  const keyboard = activeKeyboard === KEYBOARD_1 ? 1 : 2;

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
  }, [debouncedText, selectedRhythm, withDiacritics, keyboard]);

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
      const response = await fetch(`${API_BASE_URL}/search/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: debouncedText,
          rhythms: selectedRhythm,
          withDiacritics,
          keyboard,
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
    } catch (error: any) {
      console.error("Error fetching suggestions:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const insertCharacter = (char: string): void => {
    setTransformedText((prev: string) => prev + char);
    setLastOperation({ type: "insert", data: char });
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

  const deleteLastCharacter = (): void => {
    setTransformedText((prev) =>
      prev.length > INITIAL_SPACE.length ? prev.slice(0, -1) : INITIAL_SPACE,
    );
    setLastOperation({ type: "delete" });
  };

  const handleEnter = (): void => {
    if (suggestions.length > 0) {
      handleSuggestionClick(suggestions[0]);
    } else {
      console.log("ENTER", transformedText);
    }
  };

  const switchKeyboard = (): void => {
    setActiveKeyboard((prev: KeyboardKey[][]) =>
      prev === KEYBOARD_1 ? KEYBOARD_2 : KEYBOARD_1,
    );
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
      case KeyboardActions.DELETE:
        deleteLastCharacter();
        break;
      case KeyboardActions.DOT:
        handleDotInput();
        break;
      case KeyboardActions.SPACE:
        insertCharacter(key.arabic);
        break;
      case KeyboardActions.ENTER:
        handleEnter();
        break;
      case KeyboardActions.SWITCH_KEYBOARD:
        switchKeyboard();
        break;
      default:
        insertCharacter(key.arabic);
        break;
    }
  };

  return (
    <div className="keyboard-container">
      <div className="keyboard">
        {activeKeyboard.map((row: KeyboardKey[], rowIndex: number) => (
          <div
            className="keyboard-row"
            key={rowIndex}
            style={{ "--row-index": rowIndex } as CSSProperties}
          >
            {row.map((keyData: KeyboardKey) => (
              <HexKeyButton
                key={keyData.id}
                keyData={keyData}
                switchLogo={getSwitchLabel(activeKeyboard)}
                onClick={() => handleKeyClick(keyData)}
              />
            ))}
          </div>
        ))}
      </div>

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
