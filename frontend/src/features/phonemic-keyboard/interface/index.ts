export const KeyboardActions = {
  SPACE: "space",
  SWITCH_KEYBOARD: "switchKeyboard",
  DELETE: "delete",
  ENTER: "enter",
  DOT: "dot",
};

export type KeyboardAction =
  (typeof KeyboardActions)[keyof typeof KeyboardActions];

export interface KeyboardKey {
  id: number;
  english: string;
  arabic: string;
  color: string;
  action?: KeyboardAction;
}

export interface SearchResponse {
  data: {
    rhythms: string[];
    suggestions: string[];
    text: string;
    isHamza: boolean;
  };
}
