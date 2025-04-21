export const DOT_TRANSFORMATIONS: Record<string, string> = {
 
  // أ -> خ -> ج -> ح (4 dots cycle)
  "\u0623": "\u0625", // أ -> إ (1st dot)
  "\u0625": "\u0626", // إ -> ئ (2nd dot)
  "\u0626": "\u0624", // ئ -> ؤ (3rd dot)
  "\u0624": "\u0623", // ؤ -> أ (4rd dot)

  
  // ح -> خ -> ج -> ح (3 dots cycle)
  "\u062D": "\u062E", // ح -> خ (1st dot)
  "\u062E": "\u062C", // خ -> ج (2nd dot)
  "\u062C": "\u062D", // ج -> ح (3rd dot)

  // ب (dotless) -> ب -> ت -> ث -> ب (dotless)
  "\u066E": "\u0628", // ٮ -> ب (1st dot)
  "\u0628": "\u062A", // ب -> ت (2nd dot)
  "\u062A": "\u062B", // ت -> ث (3rd dot)
  "\u062B": "\u066E", // ث -> ٮ (4th dot)

  // ه -> ة -> ه -> ة -> ه (2-dot pattern extended)
  "\u0647": "\u0629", // ه -> ة (odd dots)
  "\u0629": "\u0647", // ة -> ه (even dots)

  // ه -> ة -> ه -> ة -> ه (2-dot pattern extended)
  "\u0635": "\u0636", // ص -> ض (odd dots)
  "\u0636": "\u0635", // ض -> ص (even dots)

  // ه -> ة -> ه -> ة -> ه (2-dot pattern extended)
  "\u0639": "\u063A", // ع -> غ (odd dots)
  "\u063A": "\u0639", // غ -> ع (even dots)

  // ن -> ت -> ن -> ت -> ن (1-dot pattern extended)
  "\u0646": "\u062A", // ن -> ت (odd dots)

  //  ي -> ل -> م -> ك (1-dot no change pattern)
  "\u064A": "\u064A", // ي -> ي (odd dots)
  "\u0644": "\u0644", // ل -> ل (odd dots)
  "\u0645": "\u0645", // م -> م (odd dots)
  "\u0643": "\u0643", // ك -> ك (odd dots)
  "\u0648": "\u0648", // و -> و (odd dots)
  "\u0641": "\u0642", // ف -> ق (odd dots)
  "\u0642": "\u0641", // ق -> ف (odd dots)
  "\u0627": "\u0649", // ا -> ا (odd dots)
  "\u0621": "\u0621", // ء -> ء (odd dots)

  // ر -> ز -> ر -> ز -> ر (2-dot pattern)
  "\u0631": "\u0632", // ر -> ز (odd dots)
  "\u0632": "\u0631", // ز -> ر (even dots)

  // د -> ذ -> د -> ذ -> د (2-dot pattern)
  "\u062F": "\u0630", // د -> ذ (odd dots)
  "\u0630": "\u062F", // ذ -> د (even dots)

  // ط -> ظ -> ط -> ظ -> ط (2-dot pattern)
  "\u0637": "\u0638", // ط -> ظ (odd dots)
  "\u0638": "\u0637", // ظ -> ط (even dots)

  // س -> ش -> س -> ش -> س (2-dot pattern)
  "\u0633": "\u0634", // س -> ش (odd dots)
  "\u0634": "\u0633", // ش -> س (even dots)

  // Vowel transformations
  "\u064E": "\u064B", // فتح -> تنوين فتح
  "\u064F": "\u064C", // ضم -> تنوين ضم
  "\u0650": "\u064D", // كسر -> تنوين كسر
};
