import { escapeRegex } from "../escape-regex";

export const ARABIC_ORTHOGRAPHIC_RULES = [
  // Diacritic transformations

  { pattern: new RegExp("ـ", "u"), replace: " " },

  // space+tanween=vn
  { pattern: new RegExp(" ً", "u"), replace: " أَن" },
  { pattern: new RegExp(" ٌ", "u"), replace: " أُن" },
  { pattern: new RegExp(" ٍ", "u"), replace: " إِن" },

  // tanween at ends
  //{ pattern: new RegExp("ِي", "u"), replace: "" },
  //{ pattern: new RegExp("", "u"), replace: "" },
  //{ pattern: new RegExp("", "u"), replace: "" },
  //{ pattern: new RegExp("", "u"), replace: "" },

  
  // space+hamza put correctly
  { pattern: new RegExp(" ء", "u"), replace: " أ" },
  { pattern: new RegExp(" أِ", "u"), replace: " إِ" },
  { pattern: new RegExp("أََ", "u"), replace: "آ" },
  
  // bi+hamza
  { pattern: new RegExp("بِء", "u"), replace: "بِئ" },
  { pattern: new RegExp("بِئَ", "u"), replace: "بِأَ" },
  { pattern: new RegExp("بِئُ", "u"), replace: "بِأُ" },
  { pattern: new RegExp("بِئِ", "u"), replace: "بِإِ" },
  
  // space + bi + u
  { pattern: new RegExp(" بُِ", "u"), replace: " بِو" },
  { pattern: new RegExp("وَبُِ", "u"), replace: "وَبِو" },
  { pattern: new RegExp("كَبُِ", "u"), replace: "كَبِو" },
  { pattern: new RegExp("فَبُِ", "u"), replace: "فَبِو" },
  { pattern: new RegExp("أَبُِ", "u"), replace: "أَبِو" },
  
  // space + li + u
  { pattern: new RegExp(" لُِ", "u"), replace: " لِو" },
  { pattern: new RegExp("وَلُِ", "u"), replace: "وَلِو" },
  { pattern: new RegExp("كَلُِ", "u"), replace: "كَلِو" },
  { pattern: new RegExp("فَلُِ", "u"), replace: "فَلِو" },
  { pattern: new RegExp("أَلُِ", "u"), replace: "أَلِو" },

  // damma+damma and kasra+kasra and add more
  { pattern: new RegExp("ُُ", "u"), replace: "ُو" },
  { pattern: new RegExp("ُوُ", "u"), replace: "وُو" },
  { pattern: new RegExp("وُوُ", "u"), replace: "وُوّ" },
  { pattern: new RegExp("ِِ", "u"), replace: "ِي" },
  { pattern: new RegExp("ِيِ", "u"), replace: "يِي" },
  { pattern: new RegExp("يِيِ", "u"), replace: "يِيّ" },
  
  
  // space + damma/kasra = space + w/y + damma/kasra
  { pattern: new RegExp(" ُ", "u"), replace: " و" },
  { pattern: new RegExp(" ِ", "u"), replace: " ي" },
  
  // simple vowel combination rule a+u, a+i, u+a, i+a
  { pattern: new RegExp("َُ", "u"), replace: "َو" }, 
  { pattern: new RegExp("اُ", "u"), replace: "او" },
  { pattern: new RegExp("َِ", "u"), replace: "َي" },
  { pattern: new RegExp("اِ", "u"), replace: "اي" },
  { pattern: new RegExp("َُ", "u"), replace: "وَ" },
  { pattern: new RegExp("َِ", "u"), replace: "يَ" },

  // al + hamza
  { pattern: new RegExp("الءَ", "u"), replace: "الأَ" },
  { pattern: new RegExp("الءُ", "u"), replace: "الأُ" },
  { pattern: new RegExp("الءِ", "u"), replace: "الإِ" },

  ///////////////////
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
  { pattern: new RegExp("اُ", "u"), replace: "ٌ " },
  { pattern: new RegExp("َُ", "u"), replace: "او" },
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

  // Double consonant transformations (e.g.,  ضض →  الضّ)
  ...["ض", "ص", "ث", "د", "ش", "س", "ت", "ن", "ط", "ر", "ز", "ظ", "ذ"].map(
    (letter) => ({
      pattern: new RegExp(` ${escapeRegex(letter)}${escapeRegex(letter)}`, "u"),
      replace: letter === "ل" ? ` الل` : ` ال${letter}ّ`,
    }),
  ),
  ...[
    "ق",
    "ف",
    "غ",
    "ع",
    "ت",
    "ث",
    "د",
    "ذ",
    "ش",
    "ه",
    "خ",
    "ح",
    "ج",
    "س",
    "ص",
    "ط",
    "ظ",
    "ن",
    "ض",
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

  // Prefix transformations with ل (e.g.,  لق →  الق)
  ...[
    "ق",
    "ف",
    "غ",
    "ل",
    "ع",
    "ه",
    "خ",
    "ح",
    "ج",
    "ي",
    "ب",
    "م",
    "ك",
    "ء",
    "و",
  ].map((letter) => ({
    pattern: new RegExp(` ل${escapeRegex(letter)}`, "u"),
    replace: ` ال${letter}`,
  })),

  // Hamza transformations (reordered)
  { pattern: new RegExp(" ءَ", "u"), replace: " أَ" },
  { pattern: new RegExp(" ءِ", "u"), replace: " إ" },
  { pattern: new RegExp(" ءُ", "u"), replace: " أُ" },
  { pattern: new RegExp("ِء", "u"), replace: "ِئ" },
  { pattern: new RegExp("ءِ", "u"), replace: "ئِ" },
  { pattern: new RegExp("ءُ", "u"), replace: "ؤُ" },
  { pattern: new RegExp("ُء", "u"), replace: "ُؤ" },
  { pattern: new RegExp("َء", "u"), replace: "َأ" },
  { pattern: new RegExp("ءَ", "u"), replace: "أَ" },
  { pattern: new RegExp("ءََ", "u"), replace: "ءا" },
  { pattern: new RegExp("ءََ", "u"), replace: "آ" },

  // Complex prefix rules
  { pattern: new RegExp(" فَؤُ", "u"), replace: " فَأُ" },
  { pattern: new RegExp(" فَئِ", "u"), replace: " فَإِ" },
  { pattern: new RegExp(" كَؤُ", "u"), replace: " كَأُ" },
  { pattern: new RegExp(" كَئِ", "u"), replace: " كَإِ" },
  { pattern: new RegExp("كَإِيب", "u"), replace: "كَئيب" },
  { pattern: new RegExp(" وَؤُ", "u"), replace: " وَأُ" },
  { pattern: new RegExp(" وَئِ", "u"), replace: " وَإِ" },
  { pattern: new RegExp("بِئِ", "u"), replace: "بإِ" },
  { pattern: new RegExp("بِئَ", "u"), replace: "بِأَ" },
  { pattern: new RegExp("بِئُ", "u"), replace: "بِأُ" },
  { pattern: new RegExp("الؤُ", "u"), replace: "الأُ" },
  { pattern: new RegExp("الئِ", "u"), replace: "الإِ" },
  { pattern: new RegExp("لِئِ", "u"), replace: "لِأَ" },
  { pattern: new RegExp("لِئُ", "u"), replace: "لِأُ" },
  { pattern: new RegExp("لِلئِ", "u"), replace: "لِلإِ" },
  { pattern: new RegExp("لِلؤُ", "u"), replace: "لِلأُ" },

  { pattern: new RegExp("لِئِ", "u"), replace: "لِإِ" },
  { pattern: new RegExp("أَئِ", "u"), replace: "أَإِ" },
  { pattern: new RegExp("أَؤُ", "u"), replace: "أَأُ" },

  { pattern: new RegExp(" لَِ", "u"), replace: " لِا" },

  // Names and suffixes
  { pattern: new RegExp("عَبدَل", "u"), replace: "عَبدَال" },
  { pattern: new RegExp("عَبدِل", "u"), replace: "عَبدِال" },
  { pattern: new RegExp("عَبدُل", "u"), replace: "عَبدُال" },
  { pattern: new RegExp("عَبدَالءِ", "u"), replace: "عَبدَالإِ" },
  { pattern: new RegExp("عَبدَالءُ", "u"), replace: "عَبدَالأُ" },

  // Trailing   rules
  { pattern: new RegExp("حَتَّا ", "u"), replace: "حَتَّى " },
  { pattern: new RegExp("عَلا ", "u"), replace: "عَلَى" },
  { pattern: new RegExp("بَلا ", "u"), replace: "بَلَى" },
  { pattern: new RegExp("إلا ", "u"), replace: "إِلَى " },
  { pattern: new RegExp("مَتا ", "u"), replace: "مَتَى" },
  { pattern: new RegExp("عيسا ", "u"), replace: "عِيسَى " },
  { pattern: new RegExp("موسا ", "u"), replace: "مُوسَى " },
  { pattern: new RegExp("لَدا ", "u"), replace: " لَدَى " },
  { pattern: new RegExp("أولا ", "u"), replace: "أَولَى " },
  { pattern: new RegExp("رَعا ", "u"), replace: "رَعَى " },
  { pattern: new RegExp("رَما ", "u"), replace: "رَمَى " },
  { pattern: new RegExp("اءً ", "u"), replace: "وءا" },
  { pattern: new RegExp("أً ", "u"), replace: "أً " },
  { pattern: new RegExp("ةً ", "u"), replace: "ةً " },
  { pattern: new RegExp("اً ", "u"), replace: "اً " },
  { pattern: new RegExp("ىً ", "u"), replace: "ىً " },
  { pattern: new RegExp(" َ", "u"), replace: " ا" },
  { pattern: new RegExp("ً", "u"), replace: "ً " },
  { pattern: new RegExp("ٍ", "u"), replace: "ٍ " },
  { pattern: new RegExp("ٌ", "u"), replace: "ٌ " },
  { pattern: new RegExp("ً ّا", "u"), replace: "ّاً " },
  { pattern: new RegExp("ً ا", "u"), replace: "اً " },

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

export function arabicPhonemicTransformer(text: string): string {
  let transformed = text;
  ARABIC_ORTHOGRAPHIC_RULES.forEach(({ pattern, replace }) => {
    const globalPattern = new RegExp(pattern.source, "gu");
    transformed = transformed.replace(globalPattern, replace);
  });
  return transformed;
}
