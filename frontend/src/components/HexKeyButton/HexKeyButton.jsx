import clefIcon from "../../assets/clef.png";
import "./HexKeyButton.css";

export const HexKeyButton = ({ keyData, onClick }) => {
  return (
    <button
      aria-label={`Key: ${keyData.arabic}`}
      className="hex-key-wrapper"
      style={{ backgroundColor: keyData.color }}
      onClick={onClick}
    >
      <span className="arabic">{keyData.arabic}</span>
      {keyData.action === "clef" && (
        <img src={clefIcon} alt="Clef icon" width={22} />
      )}
      <span className="english">{keyData.english}</span>
    </button>
  );
};
