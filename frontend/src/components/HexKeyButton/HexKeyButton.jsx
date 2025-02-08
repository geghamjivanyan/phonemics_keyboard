import "./HexKeyButton.css";

export const HexKeyButton = ({ color, arabic, english, onClick }) => {
  return (
    <button
      className="hex-key-wrapper"
      style={{ backgroundColor: color }}
      onClick={() => onClick(arabic)}
    >
      <span className="arabic">{arabic}</span>
      <span className="english">{english}</span>
    </button>
  );
};
