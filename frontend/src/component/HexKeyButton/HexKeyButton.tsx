import { KeyboardActions, KeyboardKey } from "../../interface";
import spacebar from "../../assets/spacebar.svg";
import enter from "../../assets/enter.svg";
import deleteLeft from "../../assets/delete-left.svg";
import globe from "../../assets/globe.png";
import dot from "../../assets/dot-icon.png";
import "./HexKeyButton.css";

const ICONS = {
  [KeyboardActions.SPACE]: spacebar,
  [KeyboardActions.ENTER]: enter,
  [KeyboardActions.DELETE]: deleteLeft,
  [KeyboardActions.SWITCH_KEYBOARD]: globe,
  [KeyboardActions.DOT]: dot,
};

export const HexKeyButton = ({
  keyData,
  onClick,
}: {
  keyData: KeyboardKey;
  onClick: any;
}) => {
  return (
    <button
      aria-label={`Key: ${keyData.arabic}`}
      className="hex-key-wrapper"
      style={{ backgroundColor: keyData.color }}
      onClick={onClick}
    >
      {keyData.action && ICONS[keyData.action] ? (
        <img
          src={ICONS[keyData.action]}
          alt="Key icon"
          width={32}
          height={32}
        />
      ) : (
        <span className="arabic">{keyData.arabic}</span>
      )}
      <span className="english">{keyData.english}</span>
    </button>
  );
};
