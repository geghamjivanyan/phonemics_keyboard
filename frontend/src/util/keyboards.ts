import { KeyboardKey, KeyboardActions } from "../interface";

const WHITE = "#FAFAFA"; // (250,250,250) +
const YELLOW = "#E6E6B4"; // (230,230,180) +
const RED = "#F0C8C8"; // (240,200,200) +
const PURPLE = "#d397d3"; // (211 151 211)
const GREEN = "#C8F0C8"; // (200,240,200) +
const BLUE = "#C8D2FA"; // (200,210,250)
const BLACK = '#000000';

// wrqpjihc  in yellow
// tonmg    in purple
// def    in red
// vu    in green
// asx    in white
// bl    in black

export const KEYBOARD_1: Array<Array<KeyboardKey>> = [
  [
    {
      id: 1,
      english: "a",
      arabic: "ـ",
      color: WHITE,
      action: KeyboardActions.SPACE,
    },
    {
      id: 2,
      english: "b",
      arabic: "",
      color: BLUE,
      action: KeyboardActions.SWITCH_KEYBOARD,
    },
    { id: 3, english: "c", arabic: "\u0644", color: YELLOW },
    { id: 4, english: "d", arabic: "\u064E", color: RED },
    { id: 5, english: "e", arabic: "\u064F", color: RED },
    { id: 6, english: "f", arabic: "\u0650", color: RED },
  ],
  [
    { id: 7, english: "g", arabic: "\u0641", color: PURPLE },
    { id: 8, english: "h", arabic: "\u0646", color: YELLOW },
    { id: 9, english: "i", arabic: "\u0631", color: YELLOW },
    { id: 10, english: "j", arabic: "\u0633", color: YELLOW },
    { id: 11, english: "k", arabic: "\u0621", color: BLUE },
    {
      id: 12,
      english: "l",
      arabic: ".",
      color: BLUE,
      action: KeyboardActions.DOT,
    },
  ],
  [
    { id: 13, english: "m", arabic: "\u0645", color: PURPLE },
    { id: 14, english: "n", arabic: "\u066E", color: PURPLE },
    { id: 15, english: "o", arabic: "\u062F", color: PURPLE },
    { id: 16, english: "p", arabic: "\u0635", color: YELLOW },
    { id: 17, english: "q", arabic: "\u062D", color: YELLOW },
    { id: 18, english: "r", arabic: "\u0647", color: YELLOW },
  ],
  [
    {
      id: 19,
      english: "s",
      arabic: "",
      color: WHITE,
      action: KeyboardActions.DELETE,
    },
    { id: 20, english: "t", arabic: "\u0637", color: PURPLE },
    { id: 21, english: "u", arabic: "\u0643", color: GREEN },
    { id: 22, english: "v", arabic: "\u0642", color: GREEN },
    { id: 23, english: "w", arabic: "\u0639", color: YELLOW },
    {
      id: 24,
      english: "x",
      arabic: "",
      color: WHITE,
      action: KeyboardActions.ENTER,
    },
  ],
];

// wrqpjihc  in yellow
// tonmg    in purple
// def    in red
// vu    in green
// asx    in white
// bl    in black

export const KEYBOARD_2: Array<Array<KeyboardKey>> = [
  [
    {
      id: 1,
      english: "a",
      arabic: "ـ",
      color: WHITE,
      action: KeyboardActions.SPACE,
    },
    {
      id: 2,
      english: "b",
      arabic: "",
      color: BLUE,
      action: KeyboardActions.SWITCH_KEYBOARD,
    },
    { id: 3, english: "c", arabic: "\u0644", color: YELLOW },
    { id: 4, english: "d", arabic: "\u0627", color: RED },
    { id: 5, english: "e", arabic: "\u0648", color: RED },
    { id: 6, english: "f", arabic: "\u064a", color: RED },
  ],
  // Second row
  [
    { id: 7, english: "g", arabic: "\u0641", color: PURPLE },
    { id: 8, english: "h", arabic: "\u0646", color: YELLOW },
    { id: 9, english: "i", arabic: "\u0631", color: YELLOW },
    { id: 10, english: "j", arabic: "\u0633", color: YELLOW },
    { id: 11, english: "k", arabic: "\u0621", color: BLUE },
    {
      id: 12,
      english: "l",
      arabic: "",
      color: BLUE,
      action: KeyboardActions.DOT,
    },
  ],
  // Third row
  [
    { id: 13, english: "m", arabic: "\u0645", color: PURPLE },
    { id: 14, english: "n", arabic: "\u066E", color: PURPLE },
    { id: 15, english: "o", arabic: "\u062F", color: PURPLE },
    { id: 16, english: "p", arabic: "\u0635", color: YELLOW },
    { id: 17, english: "q", arabic: "\u062D", color: YELLOW },
    { id: 18, english: "r", arabic: "\u0647", color: YELLOW },
  ],
  // Bottom row
  [
    {
      id: 19,
      english: "s",
      arabic: "",
      color: WHITE,
      action: KeyboardActions.DELETE,
    },
    { id: 20, english: "t", arabic: "\u0637", color: PURPLE },
    { id: 21, english: "u", arabic: "\u0643", color: GREEN },
    { id: 22, english: "v", arabic: "\u0642", color: GREEN },
    { id: 23, english: "w", arabic: "\u0639", color: YELLOW },
    {
      id: 24,
      english: "x",
      arabic: "",
      color: WHITE,
      action: KeyboardActions.ENTER,
    },
  ],
];
