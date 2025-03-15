// Character transformations (immediate)
export const CHAR_TRANSFORMATIONS: Array<{
  pattern: RegExp;
  replace: string;
}> = [
  // --------------------------------------------------
  // Prefix transformations (A + B/D/F → A + C/E/G)
  // --------------------------------------------------
  // Longer prefixes first to prevent partial matching
  { pattern: /(وَكَال)ءَ$/u, replace: "$1أَ" },
  { pattern: /(وَكَال)ءُ$/u, replace: "$1أُ" },
  { pattern: /(وَكَال)ءِ$/u, replace: "$1إِ" },

  { pattern: /(فَكَال)ءَ$/u, replace: "$1أَ" },
  { pattern: /(فَكَال)ءُ$/u, replace: "$1أُ" },
  { pattern: /(فَكَال)ءِ$/u, replace: "$1إِ" },

  { pattern: /(وَكَبِ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(وَكَبِ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(وَكَبِ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(وَبِال)ءَ$/u, replace: "$1أَ" },
  { pattern: /(وَبِال)ءُ$/u, replace: "$1أُ" },
  { pattern: /(وَبِال)ءِ$/u, replace: "$1إِ" },

  { pattern: /(فَبِال)ءَ$/u, replace: "$1أَ" },
  { pattern: /(فَبِال)ءُ$/u, replace: "$1أُ" },
  { pattern: /(فَبِال)ءِ$/u, replace: "$1إِ" },

  { pattern: /(أَبِال)ءَ$/u, replace: "$1أَ" },
  { pattern: /(أَبِال)ءُ$/u, replace: "$1أُ" },
  { pattern: /(أَبِال)ءِ$/u, replace: "$1إِ" },

  { pattern: /(بِال)ءَ$/u, replace: "$1أَ" },
  { pattern: /(بِال)ءُ$/u, replace: "$1أُ" },
  { pattern: /(بِال)ءِ$/u, replace: "$1إِ" },

  { pattern: /(فَوَال)ءَ$/u, replace: "$1أَ" },
  { pattern: /(فَوَال)ءُ$/u, replace: "$1أُ" },
  { pattern: /(فَوَال)ءِ$/u, replace: "$1إِ" },

  { pattern: /(كَال)ءَ$/u, replace: "$1أَ" },
  { pattern: /(كَال)ءُ$/u, replace: "$1أُ" },
  { pattern: /(كَال)ءِ$/u, replace: "$1إِ" },

  { pattern: /(وَكَ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(وَكَ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(وَكَ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(فَال)ءَ$/u, replace: "$1أَ" },
  { pattern: /(فَال)ءُ$/u, replace: "$1أُ" },
  { pattern: /(فَال)ءِ$/u, replace: "$1إِ" },

  { pattern: /(كَلِ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(كَلِ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(كَلِ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(كَبِ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(كَبِ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(كَبِ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(وَلِ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(وَلِ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(وَلِ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(أَلِ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(أَلِ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(أَلِ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(لِل)ءَ$/u, replace: "$1أَ" },
  { pattern: /(لِل)ءُ$/u, replace: "$1أُ" },
  { pattern: /(لِل)ءِ$/u, replace: "$1إِ" },

  { pattern: /(فَلِ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(فَلِ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(فَلِ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(فَبِ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(فَبِ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(فَبِ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(وَبِ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(وَبِ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(وَبِ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(أَبِ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(أَبِ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(أَبِ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(بِ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(بِ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(بِ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(لِ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(لِ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(لِ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(وَكَال)ءَ$/u, replace: "$1أَ" },
  { pattern: /(وَكَال)ءُ$/u, replace: "$1أُ" },
  { pattern: /(وَكَال)ءِ$/u, replace: "$1إِ" },

  { pattern: /(ال)ءَ$/u, replace: "$1أَ" },
  { pattern: /(ال)ءُ$/u, replace: "$1أُ" },
  { pattern: /(ال)ءِ$/u, replace: "$1إِ" },

  { pattern: /(كَ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(كَ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(كَ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(فَ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(فَ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(فَ)ءِ$/u, replace: "$1إِ" },

  { pattern: /(وَ)ءَ$/u, replace: "$1أَ" },
  { pattern: /(وَ)ءُ$/u, replace: "$1أُ" },
  { pattern: /(وَ)ءِ$/u, replace: "$1إِ" },

  // --------------------------------------------------
  // Consonant doubling (H + H → H + J)
  // --------------------------------------------------
  {
    pattern: /([جحخهعغفقثصضكمنتلبيسشورزدذطظچڤپگژ])\1$/u,
    replace: "$1ّ",
  },
];

// Space-triggered transformations (same patterns but with space)
export const SPACE_TRANSFORMATIONS = [
  ...CHAR_TRANSFORMATIONS.map(({ pattern, replace }) => ({
    pattern: new RegExp(pattern.source.replace(/\$$/u, " $"), "u"),
    replace: replace.replace(/\$1/g, "$1 "),
  })),

  // Additional space-specific rules
  { pattern: / \.$/u, replace: "،" },
  { pattern: /، ،$/u, replace: "." },
];
