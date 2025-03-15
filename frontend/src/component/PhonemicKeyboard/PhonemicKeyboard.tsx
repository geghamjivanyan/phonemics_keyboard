import { useState } from "react";

import { DOT_TRANSFORMATIONS, KEYBOARD_1, KEYBOARD_2 } from "../../util";
import { KeyboardActions, KeyboardKey } from "../../interface";
import { HexKeyButton } from "../HexKeyButton";
import { TypedText } from "../TypedText";
import "./PhonemicKeyboard.css";
import { applyTransformations } from "../../util/new-transformation";

const SPACE_BETWEEN_ROW = 90;

export const PhonemicKeyboard = () => {
  const [typedText, setTypedText] = useState("");
  const [activeKeyboard, setActiveKeyboard] = useState(KEYBOARD_1);

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

      <TypedText typedText={typedText} />
    </div>
  );
};
