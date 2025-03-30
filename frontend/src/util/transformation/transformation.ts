import { escapeRegex } from "../escape-regex";

export const ARABIC_ORTHOGRAPHIC_RULES = [
  // Diacritic transformations

  { pattern: new RegExp("ـ", "u"), replace: " " },

  
  { pattern: new RegExp(" ً", "u"), replace: " أَن" },
  { pattern: new RegExp(" ٌ", "u"), replace: " أُن" },
  { pattern: new RegExp(" ٍ", "u"), replace:  " إِن" },
  
  { pattern: new RegExp(" ءَ", "u"), replace: " أَ" },
  { pattern: new RegExp(" ءُ", "u"), replace: " أُ" },
  { pattern: new RegExp(" ءِ", "u"), replace: " إِ" },
  { pattern: new RegExp("أََ", "u"), replace: "آ" },

  { pattern: new RegExp("ُُ", "u"), replace: "ُو" },
  { pattern: new RegExp("ِِ", "u"), replace: "ِي" },

  { pattern: new RegExp(" ُ", "u"), replace: " و" },
  { pattern: new RegExp(" ِ", "u"), replace: " ي" },
  
  { pattern: new RegExp("الءَ", "u"), replace: "الأَ" },
  { pattern: new RegExp("الءُ", "u"), replace: "الأُ" },
  { pattern: new RegExp("يِ", "u"), replace: "يّ" },
  { pattern: new RegExp("يِّ", "u"), replace: "يِّ" },
  { pattern: new RegExp("يِِّ", "u"), replace: "يِّي" },
  { pattern: new RegExp("وُ", "u"), replace: "وّ" },
  { pattern: new RegExp("وُّ", "u"), replace: "وُّو" },
  { pattern: new RegExp(" الُ", "u"), replace: " الو" },
  { pattern: new RegExp(" الِ", "u"), replace: " الي" },
  { pattern: new RegExp(" الل", "u"), replace: " الل" },
  { pattern: new RegExp("ََ", "u"), replace: "َا" },
  { pattern: new RegExp(" ُُ", "u"), replace: " ُو" },
  { pattern: new RegExp(" ِِ", "u"), replace: " ِي" },
  { pattern: new RegExp("َُ", "u"), replace: "َو" },
  { pattern: new RegExp("َِ", "u"), replace: "َي" },
  { pattern: new RegExp("َُ", "u"), replace: "وَ" },
  { pattern: new RegExp("ُِ", "u"), replace: "وِ" },
  { pattern: new RegExp("ُُِ", "u"), replace: "ُيُ" },
  { pattern: new RegExp("َِ", "u"), replace: "يَ" },
  { pattern: new RegExp("ُِ", "u"), replace: "يُ" },
  { pattern: new RegExp("ُِِ", "u"), replace: "ِوِ" },
  { pattern: new RegExp("اُ", "u"), replace: "ٌـ" },
  { pattern: new RegExp("ٌ", "u"), replace: "او" },
  { pattern: new RegExp("اِ", "u"), replace: "اي" },
  { pattern: new RegExp("ِيَ", "u"), replace: "ِيَ" },
  { pattern: new RegExp("ِيُ", "u"), replace: "ِيُ" },
  { pattern: new RegExp("ُوَ", "u"), replace: "ُوَ" },
  { pattern: new RegExp("ُوِ", "u"), replace: "ُوِ" },
  { pattern: new RegExp("َِ", "u"), replace: "يَ" },
  { pattern: new RegExp("ُِ", "u"), replace: "يُ" },

  { pattern: new RegExp("ؤِ", "u"), replace: "ئِ" },
  { pattern: new RegExp("اءََ", "u"), replace: "اءَا" },
  { pattern: new RegExp("يء", "u"), replace: "ئ" },
  { pattern: new RegExp("وءََ", "u"), replace: "وءَا" },
  { pattern: new RegExp("اءُ ", "u"), replace: "اءُ " },
  { pattern: new RegExp("اءِ ", "u"), replace: "اءِ " },








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
  { pattern: new RegExp("ءُ", "u"), replace: "ؤُ" },
  { pattern: new RegExp("ُء", "u"), replace: "ُؤ" },
  { pattern: new RegExp("َء", "u"), replace: "َأ" },
  { pattern: new RegExp("ءَ", "u"), replace: "أَ" },
  { pattern: new RegExp("ءََ", "u"), replace: "ءا" },
  { pattern: new RegExp("ءََ", "u"), replace: "آ" },

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
  { pattern: new RegExp("عَبدَل", "u"), replace: "عَبدَال" },
  { pattern: new RegExp("عَبدِل", "u"), replace: "عَبدِال" },
  { pattern: new RegExp("عَبدُل", "u"), replace: "عَبدُال" },
  { pattern: new RegExp("عَبدَالءِ", "u"), replace: "عَبدَالإِ" },
  { pattern: new RegExp("عَبدَالءُ", "u"), replace: "عَبدَالأُ" },

  // Trailing ـ rules
  { pattern: new RegExp("حَتَّاـ", "u"), replace: "حَتَّى " },
  { pattern: new RegExp("عَلاـ", "u"), replace: "عَلَى" },
  { pattern: new RegExp("بَلاـ", "u"), replace: "بَلَى" },
  { pattern: new RegExp("إلاـ", "u"), replace: "إِلَى " },
  { pattern: new RegExp("مَتاـ", "u"), replace: "مَتَى" },
  { pattern: new RegExp("عيساـ", "u"), replace: "عِيسَى " },
  { pattern: new RegExp("موساـ", "u"), replace: "مُوسَى " },
  { pattern: new RegExp("لَداـ", "u"), replace: " لَدَى " },
  { pattern: new RegExp("أولاـ", "u"), replace: "أَولَى " },
  { pattern: new RegExp("رَعاـ", "u"), replace: "رَعَى " },
  { pattern: new RegExp("رَماـ", "u"), replace: "رَمَى " },
  { pattern: new RegExp("اءًـ", "u"), replace: "وءا" },
  { pattern: new RegExp("أًـ", "u"), replace: "أًـ" },
  { pattern: new RegExp("ةًـ", "u"), replace: "ةًـ" },
  { pattern: new RegExp("اًـ", "u"), replace: "اًـ" },
  { pattern: new RegExp("ىًـ", "u"), replace: "ىًـ" },
  { pattern: new RegExp("ـَ", "u"), replace: "ـا" },
  { pattern: new RegExp("ً", "u"), replace: "ًـ" },
  { pattern: new RegExp("ٍ", "u"), replace: "ٍـ" },
  { pattern: new RegExp("ٌ", "u"), replace: "ٌـ" },

  { pattern: new RegExp("  ", "u"), replace: ", " },
  { pattern: new RegExp(",,", "u"), replace: ". " },
  
  { pattern: new RegExp("اللَاه", "u"), replace: "اللّه" },
  { pattern: new RegExp("هَاأَنتُم", "u"), replace: "هَأَنتُم" },
  { pattern: new RegExp("هَاأَنَا", "u"), replace: "هَأَنَا" },
  { pattern: new RegExp("هَاذِهِ", "u"), replace: "هَذِهِ" },
  { pattern: new RegExp("هَاؤُلَاء", "u"), replace: "هَؤُلَاء" },
  { pattern: new RegExp("ذَالِك", "u"), replace: "ذَلِك" },
   { pattern: new RegExp("هَاذَا", "u"), replace: "هَذَا" },
  { pattern: new RegExp("لَاكِن", "u"), replace: "لَكِن" },
  { pattern: new RegExp("إِلَاه", "u"), replace: "إِلَه" },
  { pattern: new RegExp("الرَّحمَان", "u"), replace: "الرَّحمَن" }, 
  { pattern: new RegExp("أُلِي", "u"), replace: "أُولِي" },
  { pattern: new RegExp("أُلُو", "u"), replace: "أُولُو" },
  { pattern: new RegExp("أُلَائِك", "u"), replace: "أُولَئِك" },
  { pattern: new RegExp("عَمرُ", "u"), replace: "عَمرو" },
];

export function ArabicPhonemicTransformer(text: string): string {
  let transformed = text;
  ARABIC_ORTHOGRAPHIC_RULES.forEach(({ pattern, replace }) => {
    const globalPattern = new RegExp(pattern.source, "gu");
    transformed = transformed.replace(globalPattern, replace);
  });
  return transformed;
}
