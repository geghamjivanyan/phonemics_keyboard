import { useState, useEffect } from "react";

import { useDebounce } from "../../hook";
import {
  DOT_TRANSFORMATIONS,
  KEYBOARD_1,
  KEYBOARD_2,
  ArabicPhonemicTransformer,
} from "../../util";
import { KeyboardActions, KeyboardKey, SearchResponse } from "../../interface";
import logo1 from "../../assets/logo/logo_1.jpg";
import logo2 from "../../assets/logo/logo_2.jpg";

import { HexKeyButton } from "../HexKeyButton";
import { TypedText } from "../TypedText";
import "./PhonemicKeyboard.css";

const SPACE_BETWEEN_ROW: number = 69;

export const PhonemicKeyboard = () => {
  const [typedText, setTypedText] = useState<string>("");
  const [activeKeyboard, setActiveKeyboard] =
    useState<KeyboardKey[][]>(KEYBOARD_1);
  const [rhythms, setRhythms] = useState<string[]>([]);
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [selectedRhythm, setSelectedRhythm] = useState<string>();
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const debouncedText: string = useDebounce<string>(typedText);

  const transformedText = ArabicPhonemicTransformer(typedText);

  useEffect(() => {
    const controller = new AbortController();
    void fetchSuggestions(controller.signal);
    return () => controller.abort();
  }, [debouncedText, selectedRhythm]);

  const fetchSuggestions = async (signal: AbortSignal): Promise<void> => {
    if (debouncedText.trim() === "") {
      setRhythms([]);
      setSuggestions([]);
      return;
    }

    const transformed = ArabicPhonemicTransformer(debouncedText);
    setIsLoading(true);
    try {
      const response = await fetch("http://34.16.40.142:8000/search/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: transformed, rhythms: selectedRhythm }),
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
    setTypedText((prev: string) => prev + suggestion);
  };

  const handleRhythmClick = (rhythm: string): void => {
    setSelectedRhythm(rhythm);
  };

  const insertCharacter = (char: string): void => {
    setTypedText((prev: string) => prev + char);
  };

  const handleDotInput = (): void => {
    setTypedText((prev: string) => {
      const lastChar = prev.slice(-1);
      const replacement = DOT_TRANSFORMATIONS[lastChar];
      return replacement ? prev.slice(0, -1) + replacement : prev + ".";
    });
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
        insertCharacter(key.arabic);
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
            style={{ top: `${rowIndex * SPACE_BETWEEN_ROW + 2}px` }}
          >
            {row.map((keyData: KeyboardKey) => (
              <HexKeyButton
                key={keyData.id}
                keyData={keyData}
                switchLogo={activeKeyboard === KEYBOARD_1 ? logo1 : logo2}
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
