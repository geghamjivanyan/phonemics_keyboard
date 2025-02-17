import { patternRecommendations } from "../../utils";
import "./TypedText.css";

export const TypedText = ({ typedText }) => {
  const normalizedTypedText = typedText.trim().toLocaleLowerCase();

  const filteredRecommendations =
    normalizedTypedText.length > 0
      ? patternRecommendations.data.filter((item) => {
          return item.name.toLocaleLowerCase().startsWith(normalizedTypedText);
        })
      : [];

  return (
    <div className="typed-text-wrapper">
      <div className="typed-text" dir="rtl">
        {typedText}
      </div>
      {filteredRecommendations.length > 0 && (
        <div className="recommendations-container">
          <ul>
            {filteredRecommendations.map((recommendation, index) => (
              <li className="recfixommendation-tag" key={index}>
                {recommendation.name}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};
