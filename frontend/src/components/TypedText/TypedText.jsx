import { patternRecommendations } from "../../utils";
import "./TypedText.css";

export const TypedText = ({ typedText }) => {
  const filteredRecommendations = patternRecommendations.data.filter((item) =>
    item.pattern.startsWith(typedText),
  );

  return (
    <div>
      <div className="typed-text" dir="rtl">
        {typedText}
      </div>
      {filteredRecommendations.length > 0 && (
        <div className="suggestions-container">
          <h3>اقتراحات</h3>
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
