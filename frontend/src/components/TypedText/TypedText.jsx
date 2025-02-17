import { patternRecommendations } from "../../utils";
import "./TypedText.css";

export const TypedText = ({ typedText }) => {
  const filteredRecommendations =
    typedText.trim().length > 0
      ? patternRecommendations.data.filter((item) =>
          item.name.startsWith(typedText),
        )
      : [];

  return (
    <div>
      <div className="typed-text" dir="rtl">
        {typedText}
      </div>
      {filteredRecommendations.length > 0 && (
        <div className="suggestions-container">
          <ul>
            {filteredRecommendations.map((suggestion, index) => (
              <li key={index}>{suggestion.name}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};
