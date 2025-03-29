import { escapeRegex } from "../escape-regex";

export const ARABIC_ORTHOGRAPHIC_RULES = [
  // Diacritic transformations
  { pattern: new RegExp("ـَ", "u"), replace: "ـا" },
  { pattern: new RegExp("ً", "u"), replace: "ًـ" },
  { pattern: new RegExp("ٍ", "u"), replace: "ٍـ" },
  { pattern: new RegExp("ٌ", "u"), replace: "ٌـ" },

  // Double consonant transformations (e.g., ـضض → ـالضّ)
  ...[
    "ض",
    "ص",
    "ث",
    "د",
    "ش",
    "س",
    "ت",
    "ن",
    "ط",
    "ر",
    "ز",
    "ظ",
    "ذ",

  ].map((letter) => ({
    pattern: new RegExp(`ـ${escapeRegex(letter)}${escapeRegex(letter)}`, "u"),
    replace: letter === "ل" ? `ـالل` : `ـال${letter}ّ`,
  })),
  ...[

    "ق",
    "ف",
    "غ",
    "ع",
    "ه",
    "خ",
    "ح",
    "ج",
    "ي",
    "ب",
    "ل",
    "م",
    "ك",
    "و",
  ].map((letter) => ({
    pattern: new RegExp(`${escapeRegex(letter)}${escapeRegex(letter)}`, "u"),
    replace: `${letter}ّ`,
  })),

  // Prefix transformations with ل (e.g., ـلق → ـالق)
  ...["ق", "ف", "غ", "ع", "ه", "خ", "ح", "ج", "ي", "ب", "م", "ك", "ء", "و"].map(
    (letter) => ({
      pattern: new RegExp(`ـل${escapeRegex(letter)}`, "u"),
      replace: `ـال${letter}`,
    }),
  ),

  // Hamza transformations (reordered)
  { pattern: new RegExp("ـءَ", "u"), replace: "ـأَ" },
  { pattern: new RegExp("ـءِ", "u"), replace: "ـإ" },
  { pattern: new RegExp("ـءُ", "u"), replace: "ـأُ" },
  { pattern: new RegExp("ِء", "u"), replace: "ِئ" },
  { pattern: new RegExp("ءِ", "u"), replace: "ئِ" },
  { pattern: new RegExp("ُء", "u"), replace: "ُؤ" },
  { pattern: new RegExp("ءُ", "u"), replace: "ؤُ" },
  { pattern: new RegExp("َء", "u"), replace: "َأ" },
  { pattern: new RegExp("ءَ", "u"), replace: "أَ" },
  { pattern: new RegExp("ءََ", "u"), replace: "ءا" },
  { pattern: new RegExp("أََ", "u"), replace: "آ" },

  // Complex prefix rules
  { pattern: new RegExp("ـفَؤُ", "u"), replace: "ـفَأُ" },
  { pattern: new RegExp("ـفَئِ", "u"), replace: "ـفَإِ" },
  { pattern: new RegExp("ـكَؤُ", "u"), replace: "ـكَأُ" },
  { pattern: new RegExp("ـكَئِ", "u"), replace: "ـكَإِ" },
  { pattern: new RegExp("كَإِيب", "u"), replace: "كَئيب" },
  { pattern: new RegExp("ـوَكَؤُ", "u"), replace: "ـوَكَأُ" },
  { pattern: new RegExp("ـوَكَئِ", "u"), replace: "ـوَكَإِ" },
  { pattern: new RegExp("وَكَؤُ", "u"), replace: "وَكَأُ" },
  { pattern: new RegExp("وَكَئِ", "u"), replace: "وَكَإِ" },
  { pattern: new RegExp("فَكَالؤُ", "u"), replace: "فَكَالأُ" },
  { pattern: new RegExp("فَكَالئِ", "u"), replace: "فَكَالإِ" },
  { pattern: new RegExp("وَكَالؤُ", "u"), replace: "وَكَالأُ" },
  { pattern: new RegExp("وَكَالئِ", "u"), replace: "وَكَالإِ" },

  // Names and suffixes
  { pattern: new RegExp("عَبدَل", "u"), replace: "كَبِأَ" },
  { pattern: new RegExp("عَبدِل", "u"), replace: "كَبِإِ" },
  { pattern: new RegExp("عَبدُل", "u"), replace: "كَبِأُ" },
  { pattern: new RegExp("عَبدَالءِ", "u"), replace: "أَلِإِ" },
  { pattern: new RegExp("عَبدَالءُ", "u"), replace: "أَلِأُ" },

  // Trailing ـ rules
  { pattern: new RegExp("حَتَّاـ", "u"), replace: "َّ" },
  { pattern: new RegExp("عَلاـ", "u"), replace: "الأُ" },
  { pattern: new RegExp("بَلاـ", "u"), replace: "بِا" },
  { pattern: new RegExp("إلاـ", "u"), replace: "ـالإِ" },
  { pattern: new RegExp("مَتاـ", "u"), replace: "فَالإِ" },
  { pattern: new RegExp("عيساـ", "u"), replace: "فَوَالإِ" },
  { pattern: new RegExp("موساـ", "u"), replace: "فَلِلإِ" },
  { pattern: new RegExp("لَداـ", "u"), replace: "وَلِلإِ" },
  { pattern: new RegExp("أَنّاـ", "u"), replace: "ـأَلِلإِ" },
  { pattern: new RegExp("أولاـ", "u"), replace: "ـلِلإِ" },
  { pattern: new RegExp("رَعاـ", "u"), replace: "فَلِأُ" },
  { pattern: new RegExp("رَماـ", "u"), replace: "ـفَبِإِ" },
  { pattern: new RegExp("اءًـ", "u"), replace: "وءا" },
  { pattern: new RegExp("أًـ", "u"), replace: "أًـ" },
  { pattern: new RegExp("ةًـ", "u"), replace: "ةًـ" },
  { pattern: new RegExp("اًـ", "u"), replace: "اًـ" },
  { pattern: new RegExp("ىًـ", "u"), replace: "ىًـ" },
];

export function ArabicPhonemicTransformer(text: string): string {
  let transformed = text;
  ARABIC_ORTHOGRAPHIC_RULES.forEach(({ pattern, replace }) => {
    const globalPattern = new RegExp(pattern.source, "gu");
    transformed = transformed.replace(globalPattern, replace);
  });
  return transformed;
}
