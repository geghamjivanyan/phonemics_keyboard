import { KeyboardKey, KeyboardActions } from "../interface";

const WHITE = "#FAFAFA"; // (250,250,250)
const YELLOW = "#E6E6B4"; // (230,230,180)
const RED = "#F0C8C8"; // (240,200,200)
const VIOLET = "#DCC8DC"; // (220,200,220)
const GREEN = "#C8F0C8"; // (200,240,200)
const BLUE = "#C8D2FA"; // (200,210,250)

export const KEYBOARD_1: Array<Array<KeyboardKey>> = [
  [
    {
      id: 1,
      english: "a",
      arabic: "ـ",
      color: VIOLET,
      action: KeyboardActions.SPACE,
    },
    {
      id: 2,
      english: "b",
      arabic: "",
      color: VIOLET,
      action: KeyboardActions.SWITCH_KEYBOARD,
    },
    { id: 3, english: "c", arabic: "\u0644", color: VIOLET },
    { id: 4, english: "d", arabic: "\u064E", color: BLUE },
    { id: 5, english: "e", arabic: "\u064F", color: YELLOW },
    { id: 6, english: "f", arabic: "\u0650", color: RED },
  ],
  [
    { id: 7, english: "g", arabic: "\u0641", color: WHITE },
    { id: 8, english: "h", arabic: "\u0646", color: WHITE },
    { id: 9, english: "i", arabic: "\u0631", color: GREEN },
    { id: 10, english: "j", arabic: "\u0633", color: GREEN },
    { id: 11, english: "k", arabic: "\u0621", color: BLUE },
    {
      id: 12,
      english: "l",
      arabic: ".",
      color: RED,
      action: KeyboardActions.DOT,
    },
  ],
  [
    { id: 13, english: "m", arabic: "\u0645", color: RED },
    { id: 14, english: "n", arabic: "\u066E", color: RED },
    { id: 15, english: "o", arabic: "\u062F", color: RED },
    { id: 16, english: "p", arabic: "\u0635", color: YELLOW },
    { id: 17, english: "q", arabic: "\u062D", color: GREEN },
    { id: 18, english: "r", arabic: "\u0647", color: RED },
  ],
  [
    {
      id: 19,
      english: "s",
      arabic: "",
      color: RED,
      action: KeyboardActions.DELETE,
    },
    { id: 20, english: "t", arabic: "\u0637", color: RED },
    { id: 21, english: "u", arabic: "\u0643", color: YELLOW },
    { id: 22, english: "v", arabic: "\u0642", color: WHITE },
    { id: 23, english: "w", arabic: "\u0639", color: WHITE },
    {
      id: 24,
      english: "x",
      arabic: "",
      color: GREEN,
      action: KeyboardActions.ENTER,
    },
  ],
];

export const KEYBOARD_2: Array<Array<KeyboardKey>> = [
  [
    {
      id: 1,
      english: "a",
      arabic: "ـ",
      color: VIOLET,
      action: KeyboardActions.SPACE,
    },
    {
      id: 2,
      english: "b",
      arabic: "",
      color: VIOLET,
      action: KeyboardActions.SWITCH_KEYBOARD,
    },
    { id: 3, english: "c", arabic: "\u0644", color: VIOLET },
    { id: 4, english: "d", arabic: "\u0627", color: BLUE },
    { id: 5, english: "e", arabic: "\u0648", color: YELLOW },
    { id: 6, english: "f", arabic: "\u064a", color: RED },
  ],
  // Second row
  [
    { id: 7, english: "g", arabic: "\u0641", color: WHITE },
    { id: 8, english: "h", arabic: "\u0646", color: WHITE },
    { id: 9, english: "i", arabic: "\u0631", color: GREEN },
    { id: 10, english: "j", arabic: "\u0633", color: GREEN },
    { id: 11, english: "k", arabic: "\u0621", color: BLUE },
    {
      id: 12,
      english: "l",
      arabic: "",
      color: RED,
      action: KeyboardActions.DOT,
    },
  ],
  // Third row
  [
    { id: 13, english: "m", arabic: "\u0645", color: RED },
    { id: 14, english: "n", arabic: "\u066E", color: RED },
    { id: 15, english: "o", arabic: "\u062F", color: RED },
    { id: 16, english: "p", arabic: "\u0635", color: YELLOW },
    { id: 17, english: "q", arabic: "\u062D", color: GREEN },
    { id: 18, english: "r", arabic: "\u0647", color: RED },
  ],
  // Bottom row
  [
    {
      id: 19,
      english: "s",
      arabic: "",
      color: RED,
      action: KeyboardActions.DELETE,
    },
    { id: 20, english: "t", arabic: "\u0637", color: RED },
    { id: 21, english: "u", arabic: "\u0643", color: YELLOW },
    { id: 22, english: "v", arabic: "\u0642", color: WHITE },
    { id: 23, english: "w", arabic: "\u0639", color: WHITE },
    {
      id: 24,
      english: "x",
      arabic: "",
      color: GREEN,
      action: KeyboardActions.ENTER,
    },
  ],
];
