import { useState, useEffect } from "react";

import { useDebounce } from "../../hook";
import {
  DOT_TRANSFORMATIONS,
  KEYBOARD_1,
  KEYBOARD_2,
  ArabicPhonemicTransformer,
} from "../../util";
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

const SPACE_BETWEEN_ROW: number = 90;

export const PhonemicKeyboard = () => {
  const [typedText, setTypedText] = useState<string>("");
  const [activeKeyboard, setActiveKeyboard] =
    useState<KeyboardKey[][]>(KEYBOARD_1);
  const [rhythms, setRhythms] = useState<string[]>([]);
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const debouncedText: string = useDebounce<string>(typedText);
  const transformedText = ArabicPhonemicTransformer(typedText);

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

    const transformed = ArabicPhonemicTransformer(debouncedText);
    setIsLoading(true);
    try {
      const response = await fetch("http://localhost:8000/search/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: transformed }),
        signal,
      });

      const data: SearchResponse = await response.json();
      setRhythms(data.data.rhythms || []);
      setSuggestions(data.data.suggestions || []);
    } catch (error: any) {
      console.error("Error fetching suggestions:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSuggestionClick = (suggestion: string): void => {
    setTypedText(suggestion);
  };

  const insertCharacter = (char: string): void => {
    setTypedText((prev: string) => {
      if (prev.endsWith(".")) {
        const transformed: string | undefined = DOT_TRANSFORMATIONS[char];
        if (transformed) {
          return prev.slice(0, -1) + transformed;
        }
      }
      return prev + char;
    });
  };

  const handleDotInput = (): void => {
    setTypedText((prev: string) => {
      const lastThree = prev.slice(-3);
      if (lastThree === "...") {
        return prev.slice(0, -3) + ".";
      } else {
        const lastChar = prev.slice(-1);
        const replacement = DOT_TRANSFORMATIONS[lastChar];
        return replacement ? prev.slice(0, -1) + replacement : prev + ".";
      }
    });
  };

  const handleSpaceInput = (): void => {
    console.log("Space Clicked!");
  };

  const deleteLastCharacter = (): void => {
    setTypedText((prev: string) => prev.slice(0, -1));
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
        handleSpaceInput();
        break;
      case KeyboardActions.ENTER:
        console.log("ENTER", typedText);
        break;
      case KeyboardActions.SWITCH_KEYBOARD:
        switchKeyboard();
        break;
      default:
        insertCharacter(key.arabic);
        break;
    }
  };

  const switchKeyboard = (): void => {
    setActiveKeyboard((prev: KeyboardKey[][]) =>
      prev === KEYBOARD_1 ? KEYBOARD_2 : KEYBOARD_1,
    );
  };

  return (
    <div className="keyboard-container">
      <div className="keyboard">
        {activeKeyboard.map((row: KeyboardKey[], rowIndex: number) => (
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
        typedText={transformedText}
        rhythms={rhythms}
        suggestions={suggestions}
        isLoading={isLoading}
        onSuggestionSelect={handleSuggestionClick}
      />
    </div>
  );
};
