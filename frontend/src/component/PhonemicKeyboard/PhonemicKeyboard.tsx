import { useState, useEffect } from "react";

import { useDebounce } from "../../hook";
import { DOT_TRANSFORMATIONS, KEYBOARD_1, KEYBOARD_2 } from "../../util";
import { applyTransformations } from "../../util/new-transformation";
import { KeyboardActions, KeyboardKey } from "../../interface";

import { HexKeyButton } from "../HexKeyButton";
import { TypedText } from "../TypedText";
import "./PhonemicKeyboard.css";

export interface SearchResponse {
  data: {
    rhythms: string[];
    suggestions: string[];
  };
}

const SPACE_BETWEEN_ROW = 90;

export const PhonemicKeyboard = () => {
  const [typedText, setTypedText] = useState("");
  const [activeKeyboard, setActiveKeyboard] = useState(KEYBOARD_1);

  const [rhythms, setRhythms] = useState<string[]>([]);
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const debouncedText = useDebounce(typedText);

  useEffect(() => {
    const controller = new AbortController();
    void fetchSuggestions(controller.signal);
    return () => controller.abort();
  }, [debouncedText]);

  const fetchSuggestions = async (signal: AbortSignal): Promise<void> => {
    if (debouncedText.trim() === "") {
      setRhythms([]);
      setSuggestions([]);
      return;
    }

    setIsLoading(true);
    try {
      const response = await fetch("http://localhost:8000/search/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: debouncedText }),
        signal,
      });

      const data: SearchResponse = await response.json();
      setRhythms(data.data.rhythms || []);
      setSuggestions(data.data.suggestions || []);
    } catch (error) {
      console.error("Error fetching suggestions:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSuggestionClick = (suggestion: string) => {
    setTypedText(suggestion);
  };

  const insertCharacter = (char: string): void => {
    setTypedText((prev) => {
      if (prev.endsWith(".")) {
        const transformed = DOT_TRANSFORMATIONS[char];
        if (transformed) {
          return prev.slice(0, -1) + transformed;
        }
      }

      return prev + char;
    });
  };

  const handleDotInput = (): void => {
    setTypedText((prev) => {
      const lastChar = prev.slice(-1);
      const replacement = DOT_TRANSFORMATIONS[lastChar];
      return replacement ? prev.slice(0, -1) + replacement : prev + ".";
    });
  };

  const handleSpaceInput = (): void => {
    setTypedText((prev) => {
      const newText = prev + " ";
      return applyTransformations(newText);
    });
  };

  const deleteLastCharacter = (): void => {
    setTypedText((prev: string) => prev.slice(0, -1));
  };

  function handleKeyClick(key: KeyboardKey): void {
    switch (key.action) {
      case KeyboardActions.DELETE:
        deleteLastCharacter();
        return;
      case KeyboardActions.DOT:
        handleDotInput();
        return;
      case KeyboardActions.SPACE:
        handleSpaceInput();
        return;
      case KeyboardActions.ENTER:
        console.log("ENTER", typedText);
        return;
      case KeyboardActions.SWITCH_KEYBOARD:
        switchKeyboard();
        return;
      default:
        insertCharacter(key.arabic);
    }
  }

  const switchKeyboard = (): void => {
    setActiveKeyboard((prev) =>
      prev === KEYBOARD_1 ? KEYBOARD_2 : KEYBOARD_1,
    );
  };

  return (
    <div className="keyboard-container">
      <div className="keyboard">
        {activeKeyboard.map((row: Array<KeyboardKey>, rowIndex: number) => (
          <div
            className="keyboard-row"
            key={rowIndex}
            style={{ top: `${rowIndex * SPACE_BETWEEN_ROW}px` }}
          >
            {row.map((keyData: KeyboardKey) => (
              <HexKeyButton
                key={keyData.id}
                keyData={keyData}
                onClick={() => handleKeyClick(keyData)}
              />
            ))}
          </div>
        ))}
      </div>

      <TypedText
        typedText={typedText}
        rhythms={rhythms}
        suggestions={suggestions}
        isLoading={isLoading}
        onSuggestionSelect={handleSuggestionClick}
      />
    </div>
  );
};
