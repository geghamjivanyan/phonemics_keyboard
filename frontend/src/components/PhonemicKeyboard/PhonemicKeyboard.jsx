import { useState } from "react";

import type { KeyboardKey } from "../../interfaces";
import { KEYS } from "../../utils";
import { HexKeyButton } from "../HexKeyButton";
import { TypedText } from "../TypedText";
import "./PhonemicKeyboard.css";

const SPACE_BETWEEN_ROW = 90;

export const PhonemicKeyboard = () => {
  const [typedText, setTypedText] = useState("");

  const insertCharacter = (char): void => {
    setTypedText((prev) => prev + char);
  };

  const deleteLastCharacter = (): void => {
    setTypedText((prev: string) => prev.slice(0, -1));
  };

  function handleKeyClick(key: KeyboardKey): void {
    if (key.action === "delete") {
        deleteLastCharacter();
        return;
    }

    if (key.action === "clef") {
        console.log("Clef Clicked!", key, "typedText: ", typedText)
        return;
    }

    insertCharacter(key.arabic);
  }

  return (
    <div className="keyboard-container">
      <div className="keyboard">
        {KEYS.map((row: Array<KeyboardKey>, rowIndex: number) => (
          <div
            className="keyboard-row"
            key={rowIndex}
            style={{ top: `${rowIndex * SPACE_BETWEEN_ROW}px` }}
          >
            {row.map((keyData:KeyboardKey) => (
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
