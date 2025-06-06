// Dynamic Regex Approach
import { escapeRegex } from "../escape-regex";

export const NEW_TRANSFORMATIONS: Array<{
  pattern: RegExp;
  replace: string;
}> = [
  // Rule: A + B = A + C (ءَ → أَ)
  ...[
    // List A ordered from longest to shortest
    "وَكَال",
    "فَكَال",
    "وَكَبِ",
    "وَبِال",
    "فَبِال",
    "أَبِال",
    "بِال",
    "فَوَال",
    "كَال",
    "وَكَ",
    "فَال",
    "كَلِ",
    "كَبِ",
    "وَلِ",
    "أَلِ",
    "لِل",
    "فَلِل",
    "وَلِل",
    "أَلِل",
    "فَبِ",
    "وَبِ",
    "أَبِ",
    "ال",
    "فَ",
    "كَ",
    "وَ",
    "بِ",
    "لِ",
  ].flatMap((prefix) => [
    {
      pattern: new RegExp(`^${escapeRegex(prefix)}ءَ$`, "u"),
      replace: `${prefix}أَ`,
    },
  ]),

  // Rule: A + D = A + E (ءُ → أُ)
  ...[
    "وَكَال",
    "فَكَال",
    "وَكَبِ",
    "وَبِال",
    "فَبِال",
    "أَبِال",
    "بِال",
    "فَوَال",
    "كَال",
    "وَكَ",
    "فَال",
    "كَلِ",
    "كَبِ",
    "وَلِ",
    "أَلِ",
    "لِل",
    "فَلِل",
    "وَلِل",
    "أَلِل",
    "فَبِ",
    "وَبِ",
    "أَبِ",
    "ال",
    "فَ",
    "كَ",
    "وَ",
    "بِ",
    "لِ",
  ].flatMap((prefix) => [
    {
      pattern: new RegExp(`^${escapeRegex(prefix)}ءُ$`, "u"),
      replace: `${prefix}أُ`,
    },
  ]),

  // Rule: A + F = A + G (ءِ → إِ)
  ...[
    "وَكَال",
    "فَكَال",
    "وَكَبِ",
    "وَبِال",
    "فَبِال",
    "أَبِال",
    "بِال",
    "فَوَال",
    "كَال",
    "وَكَ",
    "فَال",
    "كَلِ",
    "كَبِ",
    "وَلِ",
    "أَلِ",
    "لِل",
    "فَلِل",
    "وَلِل",
    "أَلِل",
    "فَبِ",
    "وَبِ",
    "أَبِ",
    "ال",
    "فَ",
    "كَ",
    "وَ",
    "بِ",
    "لِ",
  ].flatMap((prefix) => [
    {
      pattern: new RegExp(`^${escapeRegex(prefix)}ءِ$`, "u"),
      replace: `${prefix}إِ`,
    },
  ]),

  // Rule: H + H = H + J (Consonant doubling)
  ...[
    "ج",
    "ح",
    "خ",
    "ه",
    "ع",
    "غ",
    "ف",
    "ق",
    "ث",
    "ص",
    "ض",
    "ك",
    "م",
    "ن",
    "ت",
    "ل",
    "ب",
    "ي",
    "س",
    "ش",
    "و",
    "ر",
    "ز",
    "د",
    "ذ",
    "ط",
    "ظ",
    "چ",
    "ڤ",
    "پ",
    "گ",
    "ژ",
  ].flatMap((letter) => [
    {
      pattern: new RegExp(
        `^${escapeRegex(letter)}${escapeRegex(letter)}$`,
        "u",
      ),
      replace: `${letter}ّ`,
    },
  ]),
];

export function applyTransformations(text: string): string {
  let transformed = text;
  NEW_TRANSFORMATIONS.forEach(({ pattern, replace }) => {
    transformed = transformed.replace(pattern, replace);
  });
  return transformed;
}
