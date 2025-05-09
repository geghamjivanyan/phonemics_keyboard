import React, { CSSProperties, memo } from "react";
import { KEYBOARD_1, KEYBOARD_2 } from "../../util";
import { KeyboardKey } from "../../interface";
import { KeyboardVersion } from "../../constant";
import { HexKeyButton } from "../hex-key-button";
import "./Keyboard.css";

interface KeyboardProps {
  version: KeyboardVersion;
  onKeyClick: (key: KeyboardKey) => void;
}

const SWITCH_LABEL: Record<KeyboardVersion, string> = {
  [KeyboardVersion.One]: "تشكيل",
  [KeyboardVersion.Two]: "إهمال",
} as const;

const KEYBOARD_MAP: Record<KeyboardVersion, KeyboardKey[][]> = {
  [KeyboardVersion.One]: KEYBOARD_1,
  [KeyboardVersion.Two]: KEYBOARD_2,
} as const;

export const Keyboard: React.FC<KeyboardProps> = memo(
  ({ version, onKeyClick }) => {
    const activeKeyboard = KEYBOARD_MAP[version];

    return (
      <div className="keyboard">
        {activeKeyboard.map((row, rowIndex) => (
          <div
            className="keyboard-row"
            key={rowIndex}
            style={{ "--row-index": rowIndex } as CSSProperties}
          >
            {row.map((keyData: KeyboardKey) => (
              <HexKeyButton
                key={keyData.id}
                keyData={keyData}
                switchLogo={SWITCH_LABEL[version]}
                onClick={() => onKeyClick(keyData)}
              />
            ))}
          </div>
        ))}
      </div>
    );
  },
);
