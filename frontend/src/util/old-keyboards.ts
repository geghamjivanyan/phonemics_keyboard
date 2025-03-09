const WHITE = "#FAFAFA"; // (250,250,250)
const YELLOW = "#E6E6B4"; // (230,230,180)
const RED = "#F0C8C8"; // (240,200,200)
const VIOLET = "#DCC8DC"; // (220,200,220)
const GREEN = "#C8F0C8"; // (200,240,200)
const BLUE = "#C8D2FA"; // (200,210,250)

export const KEYS: Array<Array<any>> = [
  [
    { id: 1, english: "a", arabic: "\u066d", color: VIOLET },
    { id: 2, english: "b", arabic: "\u0641", color: VIOLET },
    { id: 3, english: "c", arabic: "\u0648", color: VIOLET },
    { id: 4, english: "d", arabic: "\u0637", color: BLUE },
    { id: 5, english: "e", arabic: "\u0621", color: YELLOW },
    { id: 6, english: "DEL", arabic: "\u232B", color: RED, action: "delete" },
  ],
  [
    { id: 7, english: "%", arabic: "\u003e", color: WHITE },
    { id: 8, english: "y", arabic: "\u0642", color: WHITE },
    { id: 9, english: "g", arabic: "\u0641", color: GREEN },
    { id: 10, english: "h", arabic: "\u066e", color: GREEN },
    { id: 11, english: "i", arabic: "\u062F", color: BLUE },
    {
      id: 12,
      english: "",
      arabic: "",
      color: RED,
      action: "clef",
    },
  ],
  [
    { id: 13, english: "j", arabic: "\u0643", color: RED },
    { id: 14, english: "k", arabic: "\u0020", color: RED },
    { id: 15, english: "l", arabic: "\u0646", color: RED },
    { id: 16, english: "m", arabic: "\u0645", color: YELLOW },
    { id: 17, english: "n", arabic: "\u0633", color: GREEN },
    { id: 18, english: "o", arabic: "\u062F", color: RED },
    { id: 19, english: "p", arabic: "\u0069", color: RED },
  ],
  [
    { id: 20, english: "q", arabic: "\u064A", color: RED },
    { id: 21, english: "r", arabic: "\u064e", color: YELLOW },
    { id: 22, english: "z", arabic: "\u0644", color: WHITE },
    { id: 23, english: "%", arabic: "\u0631", color: WHITE },
    { id: 24, english: "s", arabic: "\u0635", color: GREEN },
    { id: 25, english: "t", arabic: "\u062D", color: BLUE },
    { id: 26, english: "t", arabic: "\u0647", color: BLUE },
  ],
];

export const OLD_KEYS: Array<Array<any>> = [
  [
    { id: 1, english: "a", arabic: "\u064e", color: VIOLET },
    { id: 2, english: "b", arabic: "\u064f", color: VIOLET },
    { id: 3, english: "c", arabic: "\u0650", color: VIOLET },
    { id: 4, english: "d", arabic: "\u0642", color: BLUE },
    { id: 5, english: "e", arabic: "\u062c", color: YELLOW },
    { id: 6, english: "f", arabic: "\u0647", color: RED },
    { id: 7, english: "%", arabic: "\u0647", color: WHITE },
  ],
  [
    { id: 8, english: "y", arabic: ">", color: WHITE },
    { id: 9, english: "g", arabic: "\u0641", color: GREEN },
    { id: 10, english: "h", arabic: "\u0645", color: GREEN },
    { id: 11, english: "i", arabic: "\u0643", color: BLUE },
    { id: 12, english: "j", arabic: "\u0633", color: RED },
    { id: 13, english: "k", arabic: "\u062d", color: RED },
    { id: 14, english: "l", arabic: "\u0639", color: RED },
  ],
  [
    { id: 15, english: "m", arabic: "\u066D", color: YELLOW },
    { id: 16, english: "n", arabic: "\u066E", color: GREEN },
    { id: 17, english: "o", arabic: "\u0646", color: RED },
    { id: 18, english: "p", arabic: "\u0631", color: RED },
    { id: 19, english: "q", arabic: "\u0635", color: RED },
    { id: 20, english: "r", arabic: "\u0621", color: YELLOW },
    { id: 21, english: "z", arabic: "_", color: WHITE },
  ],
  [
    { id: 22, english: "%", arabic: "_", color: WHITE },
    { id: 23, english: "s", arabic: "\u0637", color: GREEN },
    { id: 24, english: "t", arabic: "\u062F", color: BLUE },
    { id: 25, english: "u", arabic: "\u0644", color: VIOLET },
    { id: 26, english: "v", arabic: "\u0627", color: YELLOW },
    { id: 27, english: "w", arabic: "\u0648", color: BLUE },
    { id: 28, english: "x", arabic: "\u064A", color: VIOLET },
    { id: 29, english: "x", arabic: "\u064A", color: WHITE },
  ],
];
