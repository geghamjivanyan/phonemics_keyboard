import React from "react";
import styles from "./TypedText.module.css";

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
    <div
      className={`${styles.typedTextWrapper} ${hasRhythms ? styles.hasRhythms : ""}`}
    >
      {hasRhythms && (
        <div className={styles.rhythmsContainer}>
          {rhythms.map((rhythm, index) => (
            <div
              key={index}
              className={styles.rhythmItem}
              onClick={() => onRhythmSelect && onRhythmSelect(rhythm)}
            >
              {rhythm}
            </div>
          ))}
        </div>
      )}

      <div className={styles.typedText} dir="rtl">
        {typedText}
        {isLoading && <span className={styles.loadingIndicator}>•••</span>}
      </div>

      {hasSuggestions && (
        <div className={styles.suggestionsContainer}>
          <ul>
            {suggestions.map((suggestion, index) => (
              <li
                className={styles.suggestionItem}
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
