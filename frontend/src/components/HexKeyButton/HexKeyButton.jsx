import { KeyboardActions } from "../../interfaces";
import spacebar from "../../assets/spacebar.svg";
import enter from "../../assets/enter.svg";
import globe from "../../assets/globe.png";
import dot from "../../assets/dot-icon.png";
import deleteLeft from "../../assets/delete-left.svg";
import "./HexKeyButton.css";

export const HexKeyButton = ({ keyData, onClick }) => {
  const ICONS = {
    [KeyboardActions.SPACE]: spacebar,
    [KeyboardActions.ENTER]: enter,
    [KeyboardActions.DELETE]: deleteLeft,
    [KeyboardActions.SWITCH_KEYBOARD]: globe,
    [KeyboardActions.DOT]: dot,
  };

  return (
    <button
      aria-label={`Key: ${keyData.arabic}`}
      className="hex-key-wrapper"
      style={{ backgroundColor: keyData.color }}
      onClick={onClick}
    >
      {ICONS[keyData.action] ? (
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
