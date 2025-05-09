import { memo } from "react";
import { KeyboardActions, type KeyboardKey } from "../../interface";
import spacebar from "../../../../assets/spacebar.svg";
import enter from "../../../../assets/enter.svg";
import deleteLeft from "../../../../assets/delete-left.svg";
import dot from "../../../../assets/dot-icon.png";
import styles from "./HexKeyButton.module.css";

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
    return switchLogo;
  }
  return keyData.action ? ICONS[keyData.action] : undefined;
};

export const HexKeyButton = memo(
  ({ keyData, onClick, switchLogo }: HexKeyButtonProps) => {
    const iconSrc = getIconSrc(keyData, switchLogo);
    const isSwitchKey = keyData.action === KeyboardActions.SWITCH_KEYBOARD;

    return (
      <button
        aria-label={`Key: ${keyData.arabic || keyData.action || "unknown"}`}
        className={styles.hexKeyWrapper}
        style={{ backgroundColor: keyData.color }}
        onClick={onClick}
      >
        {isSwitchKey ? (
          <span className={styles.switchLabel}>{iconSrc}</span>
        ) : iconSrc ? (
          <img
            alt={`${keyData.action} icon`}
            className={styles.hexImg}
            src={iconSrc}
            width={40}
            height={40}
          />
        ) : (
          <span className={styles.arabic}>{keyData.arabic}</span>
        )}
        <span className={styles.english}>{keyData.english}</span>
      </button>
    );
  },
);
