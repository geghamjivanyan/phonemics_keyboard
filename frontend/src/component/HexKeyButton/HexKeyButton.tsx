import { KeyboardActions, KeyboardKey } from "../../interface";
import { KEYBOARD_1 } from "../../util";
import spacebar from "../../assets/spacebar.svg";
import enter from "../../assets/enter.svg";
import deleteLeft from "../../assets/delete-left.svg";
import dot from "../../assets/dot-icon.png";
import logo1 from "../../assets/logo/logo_1.jpg";
import logo2 from "../../assets/logo/logo_2.jpg";
import "./HexKeyButton.css";

interface HexKeyButtonProps {
  keyData: KeyboardKey;
  onClick: () => void;
  switchLogo: string;
}

const ICONS = {
  [KeyboardActions.SPACE]: spacebar,
  [KeyboardActions.ENTER]: enter,
  [KeyboardActions.DELETE]: deleteLeft,
  [KeyboardActions.DOT]: dot,
};

const getIconSrc = (
  keyData: KeyboardKey,
  switchLogo: string,
): string | undefined => {
  if (keyData.action === KeyboardActions.SWITCH_KEYBOARD) {
    return switchLogo ? switchLogo : keyData.action;
  }
  return keyData.action ? ICONS[keyData.action] : undefined;
};

export const HexKeyButton = ({
  keyData,
  onClick,
  switchLogo,
}: HexKeyButtonProps) => {
  const iconSrc = getIconSrc(keyData, switchLogo);

  return (
    <button
      aria-label={`Key: ${keyData.arabic}`}
      className="hex-key-wrapper"
      style={{ backgroundColor: keyData.color }}
      onClick={onClick}
    >
      {iconSrc ? (
        <img
          src={iconSrc}
          alt="Key icon"
          width={40}
          height={40}
          className="hex-img"
        />
      ) : (
        <span className="arabic">{keyData.arabic}</span>
      )}
      <span className="english">{keyData.english}</span>
    </button>
  );
};
