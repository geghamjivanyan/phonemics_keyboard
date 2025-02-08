import { useState } from "react";
import { KEYS } from "../../utils";
import { HexKeyButton } from "../HexKeyButton";
import "./PhonemicKeyboard.css";

const SPACE_BETWEEN_ROW = 90;


export const PhonemicKeyboard = () => {
  const [typedText, setTypedText] = useState("");

  const handleKeyClick = (key) => {
    setTypedText((prev) => prev + key);
  };

  return (
    <div className="keyboard-container">
      <div className="keyboard">
        {KEYS.map((row, rowIndex) => (
          <div
            className="keyboard-row"
            key={rowIndex}
            style={{ top: `${rowIndex * SPACE_BETWEEN_ROW}px` }}
          >
            {row.map((keyData) => (
              <HexKeyButton
                key={keyData.id}
                color={keyData.color}
                arabic={keyData.arabic}
                english={keyData.english}
                onClick={handleKeyClick}
              />
            ))}
          </div>
        ))}
      </div>
      <div className="typed-text">{typedText}</div>
    </div>
  );
};
