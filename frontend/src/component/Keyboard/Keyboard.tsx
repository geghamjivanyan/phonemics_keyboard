import { KeyboardKey } from "../../interface";
import React, { CSSProperties } from "react";
import { HexKeyButton } from "../HexKeyButton";
import { KEYBOARD_1 } from "../../util";
import "./Keyboard.css";

interface KeyboardProps {
  activeKeyboard: KeyboardKey[][];
  onKeyClick: (key: KeyboardKey) => void;
}

const SWITCH_LABEL: Record<"k1" | "k2", string> = {
  k1: "تشكيل",
  k2: "إهمال",
} as const;

const getSwitchLabel = (kb: KeyboardKey[][]): string =>
  kb === KEYBOARD_1 ? SWITCH_LABEL.k1 : SWITCH_LABEL.k2;

export const Keyboard: React.FC<KeyboardProps> = ({
  activeKeyboard,
  onKeyClick,
}) => (
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
            switchLogo={getSwitchLabel(activeKeyboard)}
            onClick={() => onKeyClick(keyData)}
          />
        ))}
      </div>
    ))}
  </div>
);
