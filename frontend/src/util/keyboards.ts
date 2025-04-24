import { KeyboardKey, KeyboardActions } from "../interface";

const WHITE = "#FAFAFA"; // (250,250,250) +
const YELLOW = "#E6E6B4"; // (230,230,180) +
const RED = "#F0C8C8"; // (240,200,200) +
const PURPLE = "#d397d3"; // (211 151 211)
const GREEN = "#C8F0C8"; // (200,240,200) +
const BLUE = "#C8D2FA"; // (200,210,250)
// const BLACK = "#000000";

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
      color: WHITE,
      english: "a",
      arabic: "",
      action: KeyboardActions.DELETE,
    },
    {
      id: 2,
      color: BLUE,
      english: "b",
      arabic: "",
      action: KeyboardActions.SWITCH_KEYBOARD,
    },
    { id: 3, color: YELLOW, english: "c", arabic: "\u0644" },
    { id: 4, color: RED, english: "d", arabic: "\u064E" },
    { id: 5, color: RED, english: "e", arabic: "\u064F" },
    { id: 6, color: RED, english: "f", arabic: "\u0650" },
  ],
  [
    { id: 7, color: PURPLE, english: "g", arabic: "\u0641" },
    { id: 8, color: YELLOW, english: "h", arabic: "\u0646" },
    { id: 9, color: YELLOW, english: "i", arabic: "\u0631" },
    { id: 10, color: YELLOW, english: "j", arabic: "\u0633" },
    { id: 11, color: BLUE, english: "k", arabic: "\u0621" },
    {
      id: 12,
      color: BLUE,
      english: "l",
      arabic: ".",
      action: KeyboardActions.DOT,
    },
  ],
  [
    { id: 13, color: PURPLE, english: "m", arabic: "\u0645" },
    { id: 14, color: PURPLE, english: "n", arabic: "\u066E" },
    { id: 15, color: PURPLE, english: "o", arabic: "\u062F" },
    { id: 16, color: YELLOW, english: "p", arabic: "\u0635" },
    { id: 17, color: YELLOW, english: "q", arabic: "\u062D" },
    { id: 18, color: YELLOW, english: "r", arabic: "\u0647" },
  ],
  [
    {
      id: 19,
      color: WHITE,
      english: "s",
      arabic: "ـ",
      action: KeyboardActions.SPACE,
    },
    { id: 20, color: PURPLE, english: "t", arabic: "\u0637" },
    { id: 21, color: GREEN, english: "u", arabic: "\u0643" },
    { id: 22, color: GREEN, english: "v", arabic: "\u0642" },
    { id: 23, color: YELLOW, english: "w", arabic: "\u0639" },
    {
      id: 24,
      color: WHITE,
      english: "x",
      arabic: "",
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
      color: WHITE,
      english: "a",
      arabic: "",
      action: KeyboardActions.DELETE,
    },
    {
      id: 2,
      color: BLUE,
      english: "b",
      arabic: "",
      action: KeyboardActions.SWITCH_KEYBOARD,
    },
    { id: 3, color: YELLOW, english: "c", arabic: "\u0644" },
    { id: 4, color: RED, english: "d", arabic: "\u0627" },
    { id: 5, color: RED, english: "e", arabic: "\u0648" },
    { id: 6, color: RED, english: "f", arabic: "\u064a" },
  ],
  // Second row
  [
    { id: 7, color: PURPLE, english: "g", arabic: "\u0641" },
    { id: 8, color: YELLOW, english: "h", arabic: "\u0646" },
    { id: 9, color: YELLOW, english: "i", arabic: "\u0631" },
    { id: 10, color: YELLOW, english: "j", arabic: "\u0633" },
    { id: 11, color: BLUE, english: "k", arabic: "\u0621" },
    {
      id: 12,
      color: BLUE,
      english: "l",
      arabic: "",
      action: KeyboardActions.DOT,
    },
  ],
  // Third row
  [
    { id: 13, color: PURPLE, english: "m", arabic: "\u0645" },
    { id: 14, color: PURPLE, english: "n", arabic: "\u066E" },
    { id: 15, color: PURPLE, english: "o", arabic: "\u062F" },
    { id: 16, color: YELLOW, english: "p", arabic: "\u0635" },
    { id: 17, color: YELLOW, english: "q", arabic: "\u062D" },
    { id: 18, color: YELLOW, english: "r", arabic: "\u0647" },
  ],
  // Bottom row
  [
    {
      id: 19,
      color: WHITE,
      english: "s",
      arabic: "ـ",
      action: KeyboardActions.SPACE,
    },
    { id: 20, color: PURPLE, english: "t", arabic: "\u0637" },
    { id: 21, color: GREEN, english: "u", arabic: "\u0643" },
    { id: 22, color: GREEN, english: "v", arabic: "\u0642" },
    { id: 23, color: YELLOW, english: "w", arabic: "\u0639" },
    {
      id: 24,
      color: WHITE,
      english: "x",
      arabic: "",
      action: KeyboardActions.ENTER,
    },
  ],
];
