import React from "react";
import "./TypedText.css";

interface TypedTextProps {
  typedText: string;
  rhythms?: string[];
  suggestions?: string[];
  onSuggestionSelect?: (suggestion: string) => void;
  onRhythmSelect?: (rhythm: string) => void;
  isLoading?: boolean;
}

export const TypedText: React.FC<TypedTextProps> = ({
  typedText,
  suggestions = [],
  rhythms = [],
  onSuggestionSelect,
  onRhythmSelect,
  isLoading = false,
}: TypedTextProps) => {
  const hasRhythms = rhythms && rhythms.length > 0;
  const hasSuggestions = suggestions && suggestions.length > 0;

  return (
    <div className={`typed-text-wrapper ${hasRhythms ? "has-rhythms" : ""}`}>
      {hasRhythms && (
        <div className="rhythms-container">
          {rhythms.map((rhythm, index) => (
            <div
              key={index}
              className="rhythm-item"
              onClick={() => onRhythmSelect && onRhythmSelect(rhythm)}
            >
              {rhythm}
            </div>
          ))}
        </div>
      )}

      <div className="typed-text" dir="rtl">
        {typedText}
        {isLoading && <span className="loading-indicator">•••</span>}
      </div>

      {hasSuggestions && (
        <div className="suggestions-container">
          <ul>
            {suggestions.map((suggestion, index) => (
              <li
                className="suggestion-item"
                key={index}
                onClick={() =>
                  onSuggestionSelect && onSuggestionSelect(suggestion)
                }
              >
                {suggestion}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};
