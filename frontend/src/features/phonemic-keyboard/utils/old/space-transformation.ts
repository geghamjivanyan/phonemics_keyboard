export const SPACE_TRANSFORMATIONS: Array<{
  pattern: RegExp;
  replace: string;
}> = [
  // فَأ + ُ = فَأُ
  { pattern: /فَأ \u064F$/u, replace: "فَأُ" },
  // فَأ + ِ = فَإِ
  { pattern: /فَأ \u0650$/u, replace: "فَإِ" },

  // كَأ + ُ = كَأُ
  { pattern: /كَأ \u064F$/u, replace: "كَأُ" },
  // كَأ + ِ = كَإِ
  { pattern: /كَأ \u0650$/u, replace: "كَإِ" },

  // وَكَأ + ُ = وَكَأُ
  { pattern: /وَكَأ \u064F$/u, replace: "وَكَأُ" },
  // وَكَأ + ِ = وَكَإِ
  { pattern: /وَكَأ \u0650$/u, replace: "وَكَإِ" },

  // كَالء + ُ = كَالأُ
  { pattern: /كَالء \u064F$/u, replace: "كَالأُ" },
  // كَالء + ِ = كَالإِ
  { pattern: /كَالء \u0650$/u, replace: "كَالإِ" },

  // كَال + ل = كَالل
  { pattern: /كَال ل$/u, replace: "كَالل" },

  // فَكَالء + ُ = فَكَالأُ
  { pattern: /فَكَالء \u064F$/u, replace: "فَكَالأُ" },
  // فَكَالء + ِ = فَكَالإِ
  { pattern: /فَكَالء \u0650$/u, replace: "فَكَالإِ" },

  // وَكَالء + َ = وَكَالأَ
  { pattern: /وَكَالء \u064E$/u, replace: "وَكَالأَ" },
  // وَكَالء + ُ = وَكَالأُ
  { pattern: /وَكَالء \u064F$/u, replace: "وَكَالأُ" },
  // وَكَالء + ِ = وَكَالإِ
  { pattern: /وَكَالء \u0650$/u, replace: "وَكَالإِ" },

  // كَلِئ + َ = كَلِأَ
  { pattern: /كَلِئ \u064E$/u, replace: "كَلِأَ" },
  // كَلِئ + ُ = كَلِأُ
  { pattern: /كَلِئ \u064F$/u, replace: "كَلِأُ" },
  // كَلِئ + ِ = كَلِإِ
  { pattern: /كَلِئ \u0650$/u, replace: "كَلِإِ" },

  // كَبِئ + َ = كَبِأ
  { pattern: /كَبِئ \u064E$/u, replace: "كَبِأ" },
  // كَبِئ + ُ = كَبِأُ
  { pattern: /كَبِئ \u064F$/u, replace: "كَبِأُ" },
  // كَبِئ + ِ = كَبِإِ
  { pattern: /كَبِئ \u0650$/u, replace: "كَبِإِ" },

  // وَكَبِئ + َ = وَكَبِأ
  { pattern: /وَكَبِئ \u064E$/u, replace: "وَكَبِأ" },
  // وَكَبِئ + ُ = وَكَبِأُ
  { pattern: /وَكَبِئ \u064F$/u, replace: "وَكَبِأُ" },
  // وَكَبِئ + ِ = وَكَبِإِ
  { pattern: /وَكَبِئ \u0650$/u, replace: "وَكَبِإِ" },

  // بِئ + َ = بِأَ
  { pattern: /بِئ \u064E$/u, replace: "بِأَ" },
  // بِئ + ُ = بِأُ
  { pattern: /بِئ \u064F$/u, replace: "بِأُ" },
  // بِئ + ِ = بِإِ
  { pattern: /بِئ \u0650$/u, replace: "بِإِ" },

  // أَبِئ + َ = أَبِأَ
  { pattern: /أَبِئ \u064E$/u, replace: "أَبِأَ" },
  // أَبِئ + ُ = أَبِأُ
  { pattern: /أَبِئ \u064F$/u, replace: "أَبِأُ" },
  // أَبِئ + ِ = أَبِإِ
  { pattern: /أَبِئ \u0650$/u, replace: "أَبِإِ" },

  // لِئ + َ = لِأَ
  { pattern: /لِئ \u064E$/u, replace: "لِأَ" },
  // لِئ + ُ = لِأُ
  { pattern: /لِئ \u064F$/u, replace: "لِأُ" },
  // لِئ + ِ = لِإِ
  { pattern: /لِئ \u0650$/u, replace: "لِإِ" },

  // أَلِئ + َ = أَلِأَ
  { pattern: /أَلِئ \u064E$/u, replace: "أَلِأَ" },
  // أَلِئ + ُ = أَلِأُ
  { pattern: /أَلِئ \u064F$/u, replace: "أَلِأُ" },
  // أَلِئ + ِ = أَلِإِ
  { pattern: /أَلِئ \u0650$/u, replace: "أَلِإِ" },

  // وَلِئ + َ = وَلِأَ
  { pattern: /وَلِئ \u064E$/u, replace: "وَلِأَ" },
  // وَلِئ + ُ = وَلِأُ
  { pattern: /وَلِئ \u064F$/u, replace: "وَلِأُ" },
  // وَلِئ + ِ = وَلِإِ
  { pattern: /وَلِئ \u0650$/u, replace: "وَلِإِ" },

  // وَأ + ُ = وَأُ
  { pattern: /وَأ \u064F$/u, replace: "وَأُ" },
  // وَأ + ِ = وَإِ
  { pattern: /وَأ \u0650$/u, replace: "وَإِ" },

  // وَبِئ + َ = وَبِأَ
  { pattern: /وَبِئ \u064E$/u, replace: "وَبِأَ" },
  // وَبِئ + ُ = وَبِأُ
  { pattern: /وَبِئ \u064F$/u, replace: "وَبِأُ" },
  // وَبِئ + ِ = وَبِإِ
  { pattern: /وَبِئ \u0650$/u, replace: "وَبِإِ" },

  // فَبِئ + َ = فَبِأَ
  { pattern: /فَبِئ \u064E$/u, replace: "فَبِأَ" },
  // فَبِئ + ُ = فَبِأُ
  { pattern: /فَبِئ \u064F$/u, replace: "فَبِأُ" },
  // فَبِئ + ِ = فَبِإِ
  { pattern: /فَبِئ \u0650$/u, replace: "فَبِإِ" },

  // فَلِئ + َ = فَلِأَ
  { pattern: /فَلِئ \u064E$/u, replace: "فَلِأَ" },
  // فَلِئ + ُ = فَلِأُ
  { pattern: /فَلِئ \u064F$/u, replace: "فَلِأُ" },
  // فَلِئ + ِ = فَلِإِ
  { pattern: /فَلِئ \u0650$/u, replace: "فَلِإِ" },

  // لِلء + ُ = لِلأُ
  { pattern: /لِلء \u064F$/u, replace: "لِلأُ" },
  // لِلء + ِ = لِلإِ
  { pattern: /لِلء \u0650$/u, replace: "لِلإِ" },

  // أَلِلء + ُ = أَلِلأُ
  { pattern: /أَلِلء \u064F$/u, replace: "أَلِلأُ" },
  // أَلِلء + ِ = أَلِلإِ
  { pattern: /أَلِلء \u0650$/u, replace: "أَلِلإِ" },

  // وَلِلء + ُ = وَلِلأُ
  { pattern: /وَلِلء \u064F$/u, replace: "وَلِلأُ" },
  // وَلِلء + ِ = وَلِلإِ
  { pattern: /وَلِلء \u0650$/u, replace: "وَلِلإِ" },

  // فَلِلء + ُ = فَلِلأُ
  { pattern: /فَلِلء \u064F$/u, replace: "فَلِلأُ" },
  // فَلِلء + ِ = فَلِلإِ
  { pattern: /فَلِلء \u0650$/u, replace: "فَلِلإِ" },

  // الء + ُ = الأُ
  { pattern: /الء \u064F$/u, replace: "الأُ" },
  // الء + ِ = الإِ
  { pattern: /الء \u0650$/u, replace: "الإِ" },

  // فَوَالء + ُ = فَوَالأُ
  { pattern: /فَوَالء \u064F$/u, replace: "فَوَالأُ" },
  // فَوَالء + ِ = فَوَالإِ
  { pattern: /فَوَالء \u0650$/u, replace: "فَوَالإِ" },

  // ال + ل = الل
  { pattern: /ال ل$/u, replace: "الل" },

  // فَالء + ُ = فَالأُ
  { pattern: /فَالء \u064F$/u, replace: "فَالأُ" },
  // فَالء + ِ = فَالإِ
  { pattern: /فَالء \u0650$/u, replace: "فَالإِ" },

  // فَال + ل = فَالل
  { pattern: /فَال ل$/u, replace: "فَالل" },

  // بِ + َ = بِا
  { pattern: /بِ \u064E$/u, replace: "بِا" },
  // فَبِ + َ = فَبِا
  { pattern: /فَبِ \u064E$/u, replace: "فَبِا" },
  // وَبِ + َ = وَبِا
  { pattern: /وَبِ \u064E$/u, replace: "وَبِا" },

  // أَبِ + َ = أَبِا
  { pattern: /أَبِ \u064E$/u, replace: "أَبِا" },

  // وَبِالء + ُ = وَبِالأُ
  { pattern: /وَبِالء \u064F$/u, replace: "وَبِالأُ" },
  // وَبِالء + ِ = وَبِالإِ
  { pattern: /وَبِالء \u0650$/u, replace: "وَبِالإِ" },

  // بِالء + ُ = بِالأُ
  { pattern: /بِالء \u064F$/u, replace: "بِالأُ" },
  // بِالء + ِ = بِالإِ
  { pattern: /بِالء \u0650$/u, replace: "بِالإِ" },

  // أَبِالء + ُ = أَبِالأُ
  { pattern: /أَبِالء \u064F$/u, replace: "أَبِالأُ" },
  // أَبِالء + ِ = أَبِالإِ
  { pattern: /أَبِالء \u0650$/u, replace: "أَبِالإِ" },

  // فَبِالء + ُ = فَبِالأُ
  { pattern: /فَبِالء \u064F$/u, replace: "فَبِالأُ" },
  // فَبِالء + ِ = فَبِالإِ
  { pattern: /فَبِالء \u0650$/u, replace: "فَبِالإِ" },

  // فَبِال + ل = فَبِالل
  { pattern: /فَبِال ل$/u, replace: "فَبِالل" },
  // وَبِال + ل = وَبِالل
  { pattern: /وَبِال ل$/u, replace: "وَبِالل" },
  // فَكَال + ل = فَكَالل
  { pattern: /فَكَال ل$/u, replace: "فَكَالل" },

  // لِ + َ = لِا
  { pattern: /لِ \u064E$/u, replace: "لِا" },

  // ء + َ = أَ
  { pattern: /ء \u064E$/u, replace: "أَ" },
  // ء + ُ = أُ
  { pattern: /ء \u064F$/u, replace: "أُ" },
  // ء + ِ = إِ
  { pattern: /ء \u0650$/u, replace: "إِ" },
  // ء + َ = أَ + َ = آ
  { pattern: /ء \u064E \u064E$/u, replace: "آ" },

  // ال + ء = الء
  { pattern: /ال ء$/u, replace: "الء" },
  // الء + َ = الأَ
  { pattern: /الء \u064E$/u, replace: "الأَ" },
  // الء + ُ = الأُ
  { pattern: /الء \u064F$/u, replace: "الأُ" },

  // ي + ِ = يّ
  { pattern: /ي \u0650$/u, replace: "يّ" },
  // يّ + ِ = يِّ
  { pattern: /يّ \u0650$/u, replace: "يِّ" },
  // يِّ + ِ = يِّي
  { pattern: /يِّ \u0650$/u, replace: "يِّي" },

  // و + ُ = وّ
  { pattern: /و \u064F$/u, replace: "وّ" },
  // وّ + ُ = وُّ
  { pattern: /وّ \u064F$/u, replace: "وُّ" },
  // وُّ + ُ = وُّو
  { pattern: /وُّ \u064F$/u, replace: "وُّو" },

  // الَ = ا
  { pattern: /ال\u064E$/u, replace: "ا" },
  // الُ = و
  { pattern: /ال\u064F$/u, replace: "و" },
  // الِ = ي
  { pattern: /ال\u0650$/u, replace: "ي" },

  // ء + َ = أَ
  { pattern: /ء \u064E$/u, replace: "أَ" },
  // ء + ُ = أُ
  { pattern: /ء \u064F$/u, replace: "أُ" },
  // ء + ِ = إِ
  { pattern: /ء \u0650$/u, replace: "إِ" },

  // ال + ُ = الو
  { pattern: /ال \u064F$/u, replace: "الو" },
  // ال + ِ = الي
  { pattern: /ال \u0650$/u, replace: "الي" },
  // ال + ء = الء
  { pattern: /ال ء$/u, replace: "الء" },

  // الء + َ = الأَ
  { pattern: /الء \u064E$/u, replace: "الأَ" },
  // الء + ُ = الأُ
  { pattern: /الء \u064F$/u, replace: "الأُ" },
  // الء + ِ = الإِ
  { pattern: /الء \u0650$/u, replace: "الإِ" },

  // ال + ل = الل
  { pattern: /ال ل$/u, replace: "الل" },

  // د + د = دّ
  { pattern: /د د$/u, replace: "دّ" },
  // ذ + ذ = ذّ
  { pattern: /ذ ذ$/u, replace: "ذّ" },
  // ط + ط = طّ
  { pattern: /ط ط$/u, replace: "طّ" },
  // ظ + ظ = ظّ
  { pattern: /ظ ظ$/u, replace: "ظّ" },
  // ع + ع = عّ
  { pattern: /ع ع$/u, replace: "عّ" },
  // غ + غ = غّ
  { pattern: /غ غ$/u, replace: "غّ" },
  // ح + ح = حّ
  { pattern: /ح ح$/u, replace: "حّ" },
  // خ + خ = خّ
  { pattern: /خ خ$/u, replace: "خّ" },
  // ج + ج = جّ
  { pattern: /ج ج$/u, replace: "جّ" },
  // چ + چ = چّ
  { pattern: /چ چ$/u, replace: "چّ" },
  // ص + ص = صّ
  { pattern: /ص ص$/u, replace: "صّ" },
  // ض + ض = ضّ
  { pattern: /ض ض$/u, replace: "ضّ" },
  // ٮ + ٮ = ٮّ
  { pattern: /ٮ ٮ$/u, replace: "ٮّ" },
  // ب + ب = بّ
  { pattern: /ب ب$/u, replace: "بّ" },
  // ت + ت = تّ
  { pattern: /ت ت$/u, replace: "تّ" },
  // ث + ث = ثّ
  { pattern: /ث ث$/u, replace: "ثّ" },
  // پ + پ = پّ
  { pattern: /پ پ$/u, replace: "پّ" },
  // س + س = سّ
  { pattern: /س س$/u, replace: "سّ" },
  // ش + ش = شّ
  { pattern: /ش ش$/u, replace: "شّ" },
  // ر + ر = رّ
  { pattern: /ر ر$/u, replace: "رّ" },
  // ز + ز = زّ
  { pattern: /ز ز$/u, replace: "زّ" },
  // ژ + ژ = ژّ
  { pattern: /ژ ژ$/u, replace: "ژّ" },
  // ك + ك = كّ
  { pattern: /ك ك$/u, replace: "كّ" },
  // گ + گ = گّ
  { pattern: /گ گ$/u, replace: "گّ" },
  // ل + ل = لّ
  { pattern: /ل ل$/u, replace: "لّ" },
  // ف + ف = فّ
  { pattern: /ف ف$/u, replace: "فّ" },
  // ڤ + ڤ = ڤّ
  { pattern: /ڤ ڤ$/u, replace: "ڤّ" },
  // ق + ق = قّ
  { pattern: /ق ق$/u, replace: "قّ" },
  // م + م = مّ
  { pattern: /م م$/u, replace: "مّ" },
  // ن + ن = نّ
  { pattern: /ن ن$/u, replace: "نّ" },
  // ه + ه = هّ
  { pattern: /ه ه$/u, replace: "هّ" },

  // ي + ِ = يّ
  { pattern: /ي \u0650$/u, replace: "يّ" },
  // يّ + ِ = يِّ
  { pattern: /يّ \u0650$/u, replace: "يِّ" },
  // يِّ + ِ = يِّي
  { pattern: /يِّ \u0650$/u, replace: "يِّي" },

  // و + ُ = وّ
  { pattern: /و \u064F$/u, replace: "وّ" },
  // وّ + ُ = وُّ
  { pattern: /وّ \u064F$/u, replace: "وُّ" },
  // وُّ + ُ = وُّو
  { pattern: /وُّ \u064F$/u, replace: "وُّو" },

  // أَ + َ = آ
  { pattern: /أَ \u064E$/u, replace: "آ" },

  // َ + َ = ا
  { pattern: /\u064E \u064E$/u, replace: "ا" },
  // ُ + ُ = و
  { pattern: /\u064F \u064F$/u, replace: "و" },
  // ِ + ِ = ي
  { pattern: /\u0650 \u0650$/u, replace: "ي" },

  // َ + ُ = َ + و
  { pattern: /\u064E \u064F$/u, replace: "\u064Eو" },
  // َ + ِ = َ + ي
  { pattern: /\u064E \u0650$/u, replace: "\u064Eي" },

  // ُ + َ = وَ
  { pattern: /\u064F \u064E$/u, replace: "وَ" },
  // ُ + ِ = وِ
  { pattern: /\u064F \u0650$/u, replace: "وِ" },
  // ُ + ِ + ُ = ُ + يُ
  { pattern: /\u064F \u0650 \u064F$/u, replace: "\u064Fي\u064F" },

  // ِ + َ = يَ
  { pattern: /\u0650 \u064E$/u, replace: "يَ" },
  // ِ + ُ = يُ
  { pattern: /\u0650 \u064F$/u, replace: "يُ" },
  // ِ + ُ + ِ = ِ + وِ
  { pattern: /\u0650 \u064F \u0650$/u, replace: "\u0650و\u0650" },

  // ا + ُ = او
  { pattern: /ا \u064F$/u, replace: "او" },
  // ا + ِ = اي
  { pattern: /ا \u0650$/u, replace: "اي" },

  // ي + َ = ِ + يَ
  { pattern: /ي \u064E$/u, replace: "\u0650يَ" },
  // ي + ُ = ِ + يُ
  { pattern: /ي \u064F$/u, replace: "\u0650يُ" },

  // و + َ = ُ + وَ
  { pattern: /و \u064E$/u, replace: "\u064Fوَ" },
  // و + ِ = ُ + وِ
  { pattern: /و \u0650$/u, replace: "\u064Fوِ" },

  // اء + َ = اءَ
  { pattern: /اء \u064E$/u, replace: "اءَ" },
  // اءَ + . = اءً
  { pattern: /اءَ \.$/u, replace: "اءً" },
  // َ + . = اً
  { pattern: /\u064E \.$/u, replace: "اً" },
  // أَ + . = أً
  { pattern: /أَ \.$/u, replace: "أً" },

  // ةَ + . = ةً
  { pattern: /ةَ \.$/u, replace: "ةً" },
  // ا + َ + . = اً
  { pattern: /ا \u064E \.$/u, replace: "اً" },

  // ُ + . = ٌ
  { pattern: /\u064F \.$/u, replace: "ٌ" },
  // ِ + . = ٍ
  { pattern: /\u0650 \.$/u, replace: "ٍ" },

  // ِ + ء = ِ + ئ
  { pattern: /\u0650 ء$/u, replace: "\u0650ئ" },
  // ُ + ء = ُ + ؤ
  { pattern: /\u064F ء$/u, replace: "\u064Fؤ" },
  // ؤ + ِ = ئِ
  { pattern: /ؤ \u0650$/u, replace: "ئِ" },
  // ؤ + َ = ؤَ
  { pattern: /ؤ \u064E$/u, replace: "ؤَ" },
  // ؤ + ُ = ؤُ
  { pattern: /ؤ \u064F$/u, replace: "ؤُ" },
  // َ + ء = َ + أ
  { pattern: /\u064E ء$/u, replace: "\u064Eأ" },
  // َ + أ + ِ = َ + ئِ
  { pattern: /\u064E أ \u0650$/u, replace: "\u064Eئِ" },
  // َ + أ + ُ = َ + ؤُ
  { pattern: /\u064E أ \u064F$/u, replace: "\u064Eؤُ" },
  // َ + أ + َ = َ + أَ
  { pattern: /\u064E أ \u064E$/u, replace: "\u064Eأَ" },
  // ِ + ء = ِ + ئ
  { pattern: /\u0650 ء$/u, replace: "\u0650ئ" },
  // ا + ء = اء
  { pattern: /ا ء$/u, replace: "اء" },
  // اء + َ = اءَ
  { pattern: /اء \u064E$/u, replace: "اءَ" },
  // اءَ + َ = اءا
  { pattern: /اءَ \u064E$/u, replace: "اءا" },
  // ي + ء = ئ
  { pattern: /ي ء$/u, replace: "ئ" },
  // و + ء = ؤ
  { pattern: /و ء$/u, replace: "ؤ" },
  // ؤ + َ = ؤَ
  { pattern: /ؤ \u064E$/u, replace: "ؤَ" },
  // ؤَ + َ = ؤا
  { pattern: /ؤَ \u064E$/u, replace: "ؤا" },
  // ء + َ = أَ
  { pattern: /ء \u064E$/u, replace: "أَ" },
  // ء + ُ = ؤُ
  { pattern: /ء \u064F$/u, replace: "ؤُ" },
  // ء + ِ = ئِ
  { pattern: /ء \u0650$/u, replace: "ئِ" },
  // اء + ُ +  = اءُ
  { pattern: /اء \u064F $/u, replace: "اءُ" },
  // اء + ِ +  = اءِ
  { pattern: /اء \u0650 $/u, replace: "اءِ" },

  // ا + َ = ا + َ
  { pattern: /ا \u064E$/u, replace: "ا \u064E" },
  // ا + ُ = او
  { pattern: /ا \u064F$/u, replace: "او" },
  // ا + ِ = اي
  { pattern: /ا \u0650$/u, replace: "اي" },

  // ِ + َ = يَ
  { pattern: /\u0650 \u064E$/u, replace: "يَ" },
  // ِ + ُ = يُ
  { pattern: /\u0650 \u064F$/u, replace: "يُ" },

  // ؤ + ُ = ؤُ
  { pattern: /ؤ \u064F$/u, replace: "ؤُ" },
  // َ + ء = َ + أ
  { pattern: /\u064E ء$/u, replace: "\u064Eأ" },
  // َ + أ + ِ = َ + ئِ
  { pattern: /\u064E أ \u0650$/u, replace: "\u064Eئِ" },
  // َ + أ + ُ = َ + ؤُ
  { pattern: /\u064E أ \u064F$/u, replace: "\u064Eؤُ" },
  // َ + أ + َ = َ + أَ
  { pattern: /\u064E أ \u064E$/u, replace: "\u064Eأَ" },

  // ا + . = ى
  { pattern: /ا \.$/u, replace: "ى" },
  // ُ + و +  = وا
  { pattern: /\u064F و $/u, replace: "وا" },

  // َ + . = أَن
  { pattern: /\u064E \.$/u, replace: "أَن" },
  // ِ + . = إِن
  { pattern: /\u0650 \.$/u, replace: "إِن" },
  // ُ + . = أُن
  { pattern: /\u064F \.$/u, replace: "أُن" },

  // ل + ح = الح
  { pattern: /ل ح$/u, replace: "الح" },
  // ل + ه = اله
  { pattern: /ل ه$/u, replace: "اله" },
  // ل + ع = الع
  { pattern: /ل ع$/u, replace: "الع" },
  // ل + ف = الف
  { pattern: /ل ف$/u, replace: "الف" },
  // ل + ق = الق
  { pattern: /ل ق$/u, replace: "الق" },
  // ل + ص = الص
  { pattern: /ل ص$/u, replace: "الص" },
  // ل + ك = الك
  { pattern: /ل ك$/u, replace: "الك" },
  // ل + م = الم
  { pattern: /ل م$/u, replace: "الم" },
  // ل + ن = الن
  { pattern: /ل ن$/u, replace: "الن" },
  // ل + ء = الء
  { pattern: /ل ء$/u, replace: "الء" },
  // ل + ٮ = الٮ
  { pattern: /ل ٮ$/u, replace: "الٮ" },
  // ل + ل = الل
  { pattern: /ل ل$/u, replace: "الل" },
  // ل + ي = الي
  { pattern: /ل ي$/u, replace: "الي" },
  // ل + س = الس
  { pattern: /ل س$/u, replace: "الس" },
  // ل + ر = الر
  { pattern: /ل ر$/u, replace: "الر" },
  // ل + د = الد
  { pattern: /ل د$/u, replace: "الد" },
  // ل + ط = الط
  { pattern: /ل ط$/u, replace: "الط" },
  // ل + ث = الث
  { pattern: /ل ث$/u, replace: "الث" },
  // ل + ص = الص
  { pattern: /ل ص$/u, replace: "الص" },
  // ل + ض = الض
  { pattern: /ل ض$/u, replace: "الض" },
  // ل + ن = الن
  { pattern: /ل ن$/u, replace: "الن" },
  // ل + ت = الت
  { pattern: /ل ت$/u, replace: "الت" },
  // ل + ل = الل
  { pattern: /ل ل$/u, replace: "الل" },
  // ل + س = الس
  { pattern: /ل س$/u, replace: "الس" },
  // ل + ش = الش
  { pattern: /ل ش$/u, replace: "الش" },
  // ل + ر = الر
  { pattern: /ل ر$/u, replace: "الر" },
  // ل + ز = الز
  { pattern: /ل ز$/u, replace: "الز" },
  // ل + د = الد
  { pattern: /ل د$/u, replace: "الد" },
  // ل + ذ = الذ
  { pattern: /ل ذ$/u, replace: "الذ" },
  // ل + ط = الط
  { pattern: /ل ط$/u, replace: "الط" },
  // ل + ظ = الظ
  { pattern: /ل ظ$/u, replace: "الظ" },
  // ل + ٮ = الٮ
  { pattern: /ل ٮ$/u, replace: "الٮ" },

  // ثّ = الثّ
  { pattern: /ثّ$/u, replace: "الثّ" },
  // صّ = الصّ
  { pattern: /صّ$/u, replace: "الصّ" },
  // ضّ = الضّ
  { pattern: /ضّ$/u, replace: "الضّ" },
  // نّ = النّ
  { pattern: /نّ$/u, replace: "النّ" },
  // تّ = التّ
  { pattern: /تّ$/u, replace: "التّ" },
  // لّ = الل
  { pattern: /لّ$/u, replace: "الل" },
  // سّ = السّ
  { pattern: /سّ$/u, replace: "السّ" },
  // شّ = الشّ
  { pattern: /شّ$/u, replace: "الشّ" },
  // رّ = الرّ
  { pattern: /رّ$/u, replace: "الرّ" },
  // زّ = الزّ
  { pattern: /زّ$/u, replace: "الزّ" },
  // دّ = الدّ
  { pattern: /دّ$/u, replace: "الدّ" },
  // ذّ = الذّ
  { pattern: /ذّ$/u, replace: "الذّ" },
  // طّ = الطّ
  { pattern: /طّ$/u, replace: "الطّ" },
  // ظّ = الظّ
  { pattern: /ظّ$/u, replace: "الظّ" },
  // ٮّ = الٮّ
  { pattern: /ٮّ$/u, replace: "الٮّ" },

  // عَمر +  = عَمرو
  { pattern: /عَمر $/u, replace: "عَمرو" },
  // أُلائك = أولئِك
  { pattern: /أُلائك$/u, replace: "أولئِك" },
  // أُلو = أُولو
  { pattern: /أُلو$/u, replace: "أُولو" },
  // أُلي = أُولي
  { pattern: /أُلي$/u, replace: "أُولي" },
  // اللّاه = اللَّه
  { pattern: /اللّاه$/u, replace: "اللَّه" },
  // الرَحمان = الرَحمن
  { pattern: /الرَحمان$/u, replace: "الرَحمن" },
  // إِلاه = إِله
  { pattern: /إِلاه$/u, replace: "إِله" },
  // لاكِن = لكن
  { pattern: /لاكِن$/u, replace: "لكِن" },
  // هاذا = هذا
  { pattern: /هاذا$/u, replace: "هذا" },
  // ذالِك = ذلِك
  { pattern: /ذالِك$/u, replace: "ذلِك" },
  // هاؤُلاء = هؤُلاء
  { pattern: /هاؤُلاء$/u, replace: "هؤُلاء" },
  // هاذِه = هذِه
  { pattern: /هاذِه$/u, replace: "هذِه" },
  // هاأَنا = هأَنا
  { pattern: /هاأَنا$/u, replace: "هأَنا" },
  // هاأَنتُم = هأَنتُم
  { pattern: /هاأَنتُم$/u, replace: "هأَنتُم" },

  // عَبد + ل = عَبدال
  { pattern: /عَبد ل$/u, replace: "عَبدال" },
  // عَبد + لّ = عَبدالل
  { pattern: /عَبد لّ$/u, replace: "عَبدالل" },
  // عَبدُ + ل = عَبدُال
  { pattern: /عَبدُ ل$/u, replace: "عَبدُال" },
  // عَبدُ + لّ = عَبدُالل
  { pattern: /عَبدُ لّ$/u, replace: "عَبدُالل" },
  // عَبدَ + ل = عَبدَال
  { pattern: /عَبدَ ل$/u, replace: "عَبدَال" },
  // عَبدَ + لّ = عَبدَالل
  { pattern: /عَبدَ لّ$/u, replace: "عَبدَالل" },
  // عَبدِ + ل = عَبدِال
  { pattern: /عَبدِ ل$/u, replace: "عَبدِال" },
  // عَبدِ + لّ = عَبدِالل
  { pattern: /عَبدِ لّ$/u, replace: "عَبدِالل" },
  // عَبدَ + دّ = عَبدَالدّ
  { pattern: /عَبدَ دّ$/u, replace: "عَبدَالدّ" },
  // عَبدَ + زّ = عَبدَالزّ
  { pattern: /عَبدَ زّ$/u, replace: "عَبدَالزّ" },
  // عَبدَ + طّ = عَبدَالطّ
  { pattern: /عَبدَ طّ$/u, replace: "عَبدَالطّ" },
  // عَبدَ + نّ = عَبدَالنّ
  { pattern: /عَبدَ نّ$/u, replace: "عَبدَالنّ" },
  // عَبدَ + سّ = عَبدَالسّ
  { pattern: /عَبدَ سّ$/u, replace: "عَبدَالسّ" },
  // عَبدَ + صّ = عَبدَالصّ
  { pattern: /عَبدَ صّ$/u, replace: "عَبدَالصّ" },
  // عَبدَ + رّ = عَبدَالرّ
  { pattern: /عَبدَ رّ$/u, replace: "عَبدَالرّ" },
  // عَبدَ + شّ = عَبدَالشّ
  { pattern: /عَبدَ شّ$/u, replace: "عَبدَالشّ" },
  // عَبدَ + تّ = عَبدَالتّ
  { pattern: /عَبدَ تّ$/u, replace: "عَبدَالتّ" },
  // عَبدَ + ثّ = عَبدَالثّ
  { pattern: /عَبدَ ثّ$/u, replace: "عَبدَالثّ" },
  // عَبدَ + ذّ = عَبدَالذّ
  { pattern: /عَبدَ ذّ$/u, replace: "عَبدَالذّ" },
  // عَبدَ + ضّ = عَبدَالضّ
  { pattern: /عَبدَ ضّ$/u, replace: "عَبدَالضّ" },
  // عَبدَ + ظّ = عَبدَالظّ
  { pattern: /عَبدَ ظّ$/u, replace: "عَبدَالظّ" },
  // عَبدُ + دّ = عَبدُالدّ
  { pattern: /عَبدُ دّ$/u, replace: "عَبدُالدّ" },
  // عَبدُ + زّ = عَبدُالزّ
  { pattern: /عَبدُ زّ$/u, replace: "عَبدُالزّ" },
  // عَبدُ + طّ = عَبدُالطّ
  { pattern: /عَبدُ طّ$/u, replace: "عَبدُالطّ" },
  // عَبدُ + نّ = عَبدُالنّ
  { pattern: /عَبدُ نّ$/u, replace: "عَبدُالنّ" },
  // عَبدُ + سّ = عَبدُالسّ
  { pattern: /عَبدُ سّ$/u, replace: "عَبدُالسّ" },
  // عَبدُ + صّ = عَبدُالصّ
  { pattern: /عَبدُ صّ$/u, replace: "عَبدُالصّ" },
  // عَبدُ + رّ = عَبدُالرّ
  { pattern: /عَبدُ رّ$/u, replace: "عَبدُالرّ" },
  // عَبدُ + شّ = عَبدُالشّ
  { pattern: /عَبدُ شّ$/u, replace: "عَبدُالشّ" },
  // عَبدُ + تّ = عَبدُالتّ
  { pattern: /عَبدُ تّ$/u, replace: "عَبدُالتّ" },
  // عَبدُ + ثّ = عَبدُالثّ
  { pattern: /عَبدُ ثّ$/u, replace: "عَبدُالثّ" },
  // عَبدُ + ذّ = عَبدُالذّ
  { pattern: /عَبدُ ذّ$/u, replace: "عَبدُالذّ" },
  // عَبدُ + ضّ = عَبدُالضّ
  { pattern: /عَبدُ ضّ$/u, replace: "عَبدُالضّ" },
  // عَبدُ + ظّ = عَبدُالظّ
  { pattern: /عَبدُ ظّ$/u, replace: "عَبدُالظّ" },
  // عَبدِ + دّ = عَبدِالدّ
  { pattern: /عَبدِ دّ$/u, replace: "عَبدِالدّ" },
  // عَبدِ + زّ = عَبدِالزّ
  { pattern: /عَبدِ زّ$/u, replace: "عَبدِالزّ" },
  // عَبدِ + طّ = عَبدِالطّ
  { pattern: /عَبدِ طّ$/u, replace: "عَبدِالطّ" },
  // عَبدِ + نّ = عَبدِالنّ
  { pattern: /عَبدِ نّ$/u, replace: "عَبدِالنّ" },
  // عَبدِ + سّ = عَبدِالسّ
  { pattern: /عَبدِ سّ$/u, replace: "عَبدِالسّ" },
  // عَبدِ + صّ = عَبدِالصّ
  { pattern: /عَبدِ صّ$/u, replace: "عَبدِالصّ" },
  // عَبدِ + رّ = عَبدِالرّ
  { pattern: /عَبدِ رّ$/u, replace: "عَبدِالرّ" },
  // عَبدِ + شّ = عَبدِالشّ
  { pattern: /عَبدِ شّ$/u, replace: "عَبدِالشّ" },
  // عَبدِ + تّ = عَبدِالتّ
  { pattern: /عَبدِ تّ$/u, replace: "عَبدِالتّ" },
  // عَبدِ + ثّ = عَبدِالثّ
  { pattern: /عَبدِ ثّ$/u, replace: "عَبدِالثّ" },
  // عَبدِ + ذّ = عَبدِالذّ
  { pattern: /عَبدِ ذّ$/u, replace: "عَبدِالذّ" },
  // عَبدِ + ضّ = عَبدِالضّ
  { pattern: /عَبدِ ضّ$/u, replace: "عَبدِالضّ" },
  // عَبدِ + ظّ = عَبدِالظّ
  { pattern: /عَبدِ ظّ$/u, replace: "عَبدِالظّ" },
  // عَبدال + ء = عَبدالء
  { pattern: /عَبدال ء$/u, replace: "عَبدالء" },
  // عَبدالء + َ = عَبدالأَ
  { pattern: /عَبدالء \u064E$/u, replace: "عَبدالأَ" },
  // عَبدالأَ + َ = عَبدالآ
  { pattern: /عَبدالأَ \u064E$/u, replace: "عَبدالآ" },
  // عَبدالء + ُ = عَبدالأُ
  { pattern: /عَبدالء \u064F$/u, replace: "عَبدالأُ" },
  // عَبدالء + ِ = عَبدالإِ
  { pattern: /عَبدالء \u0650$/u, replace: "عَبدالإِ" },
  // اللا + ه = اللّه
  { pattern: /اللا ه$/u, replace: "اللّه" },

  //  + =،
  { pattern: / $/u, replace: "،" },
  // ، + ، = .
  { pattern: /، ،$/u, replace: "." },

  // ه + . = ة
  { pattern: /ه \.$/u, replace: "ة" },
];
