import { mkdir, readFile, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const catalogDir = path.join(rootDir, "catalog");
const generatedDir = path.join(rootDir, "generated");
const blueprintPath = path.join(catalogDir, "blueprints.json");
const canonPath = path.join(catalogDir, "canon.json");
const packagePath = path.join(rootDir, "package.json");
const readmePath = path.join(rootDir, "README.md");
const grimoirePath = path.join(rootDir, "GRIMOIRE.md");
const dspyDir = path.join(catalogDir, "dspy");
const asciiArtDir = path.join(catalogDir, "ascii-art");
const asciiArtOverridesDir = path.join(asciiArtDir, "overrides");
const dspyEvalSummaryPath = path.join(dspyDir, "dspy_eval_summary.json");
const baselineEvalSummaryPath = path.join(dspyDir, "baseline_eval_summary.json");
const dspyRouterArtifactPath = path.join(dspyDir, "dspy_category_router.json");
const forcecageOptimizedEvalPath = path.join(
  catalogDir,
  "gepa",
  "spells",
  "forcecage",
  "optimized_eval.json"
);

const openclawDir = path.join(generatedDir, "openclaw");
const hermesDir = path.join(generatedDir, "hermes");

const dspySpotlightSlugs = [
  "awaken",
  "animate-objects",
  "dimension-door",
  "foresight",
  "symbol",
  "project-image"
];

const categoryThemeTags = {
  "investigation-and-preparation": ["analysis", "discovery", "translation", "preflight"],
  "actions-access-and-automation": ["execution", "automation", "access", "actuation"],
  "monitoring-and-protection": ["observability", "monitoring", "guardrails", "privacy"],
  "messaging-and-coordination": ["messaging", "coordination", "handoffs", "rhetoric"],
  "repair-and-recovery": ["recovery", "repair", "triage", "stabilization"],
  "simulation-and-staging": ["simulation", "staging", "mockup", "testing"],
  "influence-and-behavior": ["influence", "behavior", "attention", "engagement"],
  "containment-and-intervention": ["containment", "intervention", "disruption", "safety"]
};

const envTagMap = {
  HA_TOKEN: "home-assistant",
  HA_URL: "home-assistant",
  SLACK_TOKEN: "slack"
};

function yamlString(value) {
  return JSON.stringify(value);
}

function clampDescription(value, maxLength = 1024) {
  if (value.length <= maxLength) {
    return value;
  }

  return `${value.slice(0, maxLength - 1).trimEnd()}…`;
}

async function readOptionalJson(targetPath) {
  try {
    return JSON.parse(await readFile(targetPath, "utf8"));
  } catch (error) {
    if (error && typeof error === "object" && "code" in error && error.code === "ENOENT") {
      return null;
    }
    throw error;
  }
}

async function readOptionalText(targetPath) {
  try {
    return await readFile(targetPath, "utf8");
  } catch (error) {
    if (error && typeof error === "object" && "code" in error && error.code === "ENOENT") {
      return null;
    }
    throw error;
  }
}

function renderSection(title, items, ordered = false) {
  const marker = ordered ? (index) => `${index + 1}.` : () => "-";
  return [`## ${title}`, "", ...items.map((item, index) => `${marker(index)} ${item}`), ""].join("\n");
}

function renderOpenClawFrontmatter(entry) {
  const lines = [
    "---",
    `name: ${entry.slug}`,
    `description: ${yamlString(entry.description)}`
  ];

  if (entry.openclaw) {
    if (typeof entry.openclaw.always === "boolean") {
      lines.push(`always: ${entry.openclaw.always}`);
    }
    if (typeof entry.openclaw.user_invocable === "boolean") {
      lines.push(`user-invocable: ${entry.openclaw.user_invocable}`);
    }
    if (typeof entry.openclaw.disable_model_invocation === "boolean") {
      lines.push(`disable-model-invocation: ${entry.openclaw.disable_model_invocation}`);
    }
    if (entry.openclaw.homepage) {
      lines.push(`homepage: ${yamlString(entry.openclaw.homepage)}`);
    }
    if (entry.openclaw.requires) {
      lines.push("metadata:");
      lines.push("  openclaw:");
      lines.push("    requires:");
      if (entry.openclaw.requires.env?.length) {
        lines.push("      env:");
        for (const envVar of entry.openclaw.requires.env) {
          lines.push(`        - ${envVar}`);
        }
      }
      if (entry.openclaw.requires.bins?.length) {
        lines.push("      bins:");
        for (const bin of entry.openclaw.requires.bins) {
          lines.push(`        - ${bin}`);
        }
      }
      if (entry.openclaw.primaryEnv) {
        lines.push(`    primaryEnv: ${entry.openclaw.primaryEnv}`);
      }
      if (entry.openclaw.emoji) {
        lines.push(`    emoji: ${yamlString(entry.openclaw.emoji)}`);
      }
    }
  }

  lines.push("---");
  return lines.join("\n");
}

function renderOpenClawSkillMd(entry, canon) {
  return [
    renderOpenClawFrontmatter(entry),
    "",
    `# ${entry.name}`,
    "",
    entry.tagline,
    "",
    "## Overview",
    "",
    `${entry.name} is interpreted here as a ${entry.literalness} ${entry.kind} with a ${entry.reality_tier} execution model.`,
    "",
    `Canonical source: ${canon.name} (${canon.kind})`,
    "",
    "Provider target: OpenClaw",
    "",
    renderSection("When To Use", entry.when_to_use),
    renderSection("Workflow", entry.workflow, true),
    renderSection("Deliverables", entry.deliverables),
    renderSection("Guardrails", entry.guardrails),
    "## Default Invocation",
    "",
    entry.default_prompt,
    ""
  ].join("\n");
}

function buildHermesTags(entry, category) {
  const tags = new Set([
    entry.kind,
    entry.reality_tier,
    entry.literalness,
    category.slug,
    ...categoryThemeTags[category.slug]
  ]);

  if (entry.openclaw?.requires) {
    tags.add("integration");

    for (const envVar of entry.openclaw.requires.env ?? []) {
      const mapped = envTagMap[envVar];
      if (mapped) {
        tags.add(mapped);
      }
    }
  }

  return [...tags];
}

function renderHermesFrontmatter(entry, category, repoMeta) {
  const lines = [
    "---",
    `name: ${entry.slug}`,
    `description: ${yamlString(clampDescription(entry.description))}`,
    `version: ${yamlString(repoMeta.version)}`,
    `author: ${yamlString(repoMeta.author)}`,
    `license: ${yamlString(repoMeta.license)}`,
    `compatibility: ${yamlString("Hermes Agent skills system")}`,
    "metadata:",
    "  hermes:",
    "    tags:"
  ];

  for (const tag of buildHermesTags(entry, category)) {
    lines.push(`      - ${tag}`);
  }

  if (repoMeta.homepage) {
    lines.push(`    homepage: ${yamlString(repoMeta.homepage)}`);
  }
  lines.push("---");

  return lines.join("\n");
}

function renderHermesPrerequisites(entry) {
  const lines = [];

  if (entry.openclaw?.requires?.env?.length) {
    lines.push(
      `Environment variables available to Hermes: ${entry.openclaw.requires.env
        .map((envVar) => `\`${envVar}\``)
        .join(", ")}.`
    );
  }

  if (entry.openclaw?.primaryEnv) {
    lines.push(`Primary credential or token: \`${entry.openclaw.primaryEnv}\`.`);
  }

  if (entry.openclaw?.requires?.bins?.length) {
    lines.push(
      `Binaries on PATH: ${entry.openclaw.requires.bins.map((bin) => `\`${bin}\``).join(", ")}.`
    );
  }

  if (lines.length === 0) {
    lines.push("No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.");
  }

  return lines;
}

function renderHermesSetup(entry) {
  if (!entry.openclaw?.requires) {
    return "";
  }

  const steps = [
    "Confirm the required environment variables are available inside the active Hermes runtime, not just in a shell profile.",
    "Verify the required binaries resolve on PATH before you rely on them in a procedure.",
    "Choose a non-production or low-risk target first if the skill can page, unlock, alert, or touch a live integration."
  ];

  return renderSection("Setup", steps, true);
}

function buildHermesProcedure(entry) {
  const procedure = [
    "Restate the target, the success condition, and any no-touch boundaries before taking action.",
    ...entry.workflow,
    "Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly."
  ];

  if (entry.literalness === "literal") {
    procedure.splice(
      procedure.length - 1,
      0,
      "Stop for explicit confirmation before taking a live action that changes access, triggers an alert, or touches a real system boundary."
    );
  }

  return procedure;
}

function buildRealityBoundary(entry) {
  if (entry.reality_tier === "shipping-now") {
    if (entry.literalness === "literal") {
      return "Treat the live action surface as real operational work, not decorative lore.";
    }
    if (entry.literalness === "hybrid") {
      return "Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.";
    }
    return "Keep the metaphor anchored to a real mechanism instead of drifting into lore.";
  }

  if (entry.reality_tier === "prototype") {
    return "Call out the glue, permissions, or missing infrastructure before you imply this is fully operational.";
  }

  return "Label this as speculative and do not present it as a working runtime capability.";
}

function buildHermesGuardrails(entry) {
  const guardrails = [buildRealityBoundary(entry), ...entry.guardrails];

  if (entry.openclaw?.requires) {
    guardrails.push("Do not rely on a live integration until credentials, target scope, and rollback expectations are verified.");
  }

  return guardrails;
}

function buildHermesVerification(entry) {
  const checks = [
    "Check that the result includes every deliverable promised above.",
    "Check that confirmed facts, assumptions, and inferences are visibly separated."
  ];

  if (entry.literalness === "literal") {
    checks.push("Check that the exact live target, confirmation gate, and rollback or recovery path are explicit.");
  } else if (entry.literalness === "hybrid") {
    checks.push("Check which parts are concrete actions versus framing, so the user can tell what is real now.");
  } else {
    checks.push("Check that the metaphor still maps cleanly to a real operational mechanism.");
  }

  if (entry.reality_tier !== "shipping-now") {
    checks.push("Check that any missing glue code, permissions, or future work is labeled before the skill is treated as ready.");
  }

  if (entry.openclaw?.requires) {
    checks.push("Check the required environment variables and binaries in the active Hermes runtime before trusting the procedure on a live target.");
  }

  return checks;
}

function buildExampleInvocation(entry) {
  const prefix = new RegExp(`^Use \\$${entry.slug} to\\s+`, "i");
  const invocation = entry.default_prompt.replace(prefix, "").replace(/\.$/, "");
  return `/${entry.slug} ${invocation}`;
}

function renderHermesSigil(entry, asciiArtBySlug) {
  const art = asciiArtBySlug.get(entry.slug)?.trimEnd();
  if (!art) {
    return "";
  }

  return ["## Sigil", "", "```text", art, "```", ""].join("\n");
}

function renderHermesSkillMd(entry, canon, category, repoMeta, asciiArtBySlug) {
  return [
    renderHermesFrontmatter(entry, category, repoMeta),
    "",
    `# ${entry.name}`,
    "",
    entry.tagline,
    "",
    renderHermesSigil(entry, asciiArtBySlug),
    "## What This Skill Does",
    "",
    entry.description,
    "",
    `In this grimoire, ${entry.name} is treated as a ${entry.literalness} ${entry.kind} with a ${entry.reality_tier} delivery profile.`,
    "",
    `Canonical reference input: ${canon.name} (${canon.kind}).`,
    "",
    renderSection("When To Use", entry.when_to_use),
    renderSection("Prerequisites", renderHermesPrerequisites(entry)),
    renderHermesSetup(entry),
    renderSection("Procedure", buildHermesProcedure(entry), true),
    renderSection("Deliverables", entry.deliverables),
    renderSection("Pitfalls / Guardrails", buildHermesGuardrails(entry)),
    renderSection("Verification", buildHermesVerification(entry)),
    "## Example Invocation",
    "",
    "```text",
    buildExampleInvocation(entry),
    "```",
    ""
  ]
    .filter(Boolean)
    .join("\n");
}

function renderHermesCategoryDescription(category) {
  return [
    "---",
    `description: ${yamlString(category.description)}`,
    "---",
    "",
    `# ${category.title}`,
    "",
    category.description,
    "",
    "This category is part of Wizards of the Ghosts, a free unofficial fan project built from original reinterpretations of public fantasy spell and skill names.",
    ""
  ].join("\n");
}

function markdownLink(label, href) {
  return `[${label}](${href})`;
}

function renderBadges(...values) {
  return values.map((value) => `\`${value}\``).join(" ");
}

function renderCodeList(values) {
  const rendered = values.map((value) => `\`${value}\``);

  if (rendered.length <= 1) {
    return rendered[0] ?? "";
  }

  if (rendered.length === 2) {
    return `${rendered[0]} and ${rendered[1]}`;
  }

  return `${rendered.slice(0, -1).join(", ")}, and ${rendered.at(-1)}`;
}

function renderRootDocPreamble() {
  return "<!-- Generated by scripts/render-skills.mjs. Edit catalog/blueprints.json or renderer source instead. -->";
}

function hermesSkillDocPath(categorySlug, entrySlug) {
  return `generated/hermes/${categorySlug}/${entrySlug}/SKILL.md`;
}

function buildDiscoveryContext(blueprints, canon) {
  const hermesSurface = blueprints.surfaces?.hermes;
  if (!hermesSurface?.categories?.length) {
    throw new Error("catalog/blueprints.json is missing surfaces.hermes.categories");
  }
  if (!hermesSurface.discovery) {
    throw new Error("catalog/blueprints.json is missing surfaces.hermes.discovery");
  }

  const entryBySlug = new Map(blueprints.entries.map((entry) => [entry.slug, entry]));
  const categoryBySlug = new Map(hermesSurface.categories.map((category) => [category.slug, category]));
  const categoryByEntrySlug = new Map();

  for (const category of hermesSurface.categories) {
    for (const entrySlug of category.entry_slugs) {
      if (categoryByEntrySlug.has(entrySlug)) {
        throw new Error(`Hermes browse docs found duplicate category assignment for ${entrySlug}`);
      }
      categoryByEntrySlug.set(entrySlug, category.slug);
    }
  }

  const hermesEntries = blueprints.entries.filter((entry) => entry.provider_targets.includes("hermes"));
  const hermesEntrySlugs = new Set(hermesEntries.map((entry) => entry.slug));

  function resolveHermesEntry(slug) {
    if (!hermesEntrySlugs.has(slug)) {
      throw new Error(`Hermes discovery references a non-Hermes entry: ${slug}`);
    }

    const entry = entryBySlug.get(slug);
    if (!entry) {
      throw new Error(`Hermes discovery references an unknown entry: ${slug}`);
    }

    return entry;
  }

  const featuredEntries = hermesSurface.discovery.featured_entry_slugs.map(resolveHermesEntry);
  const refusedEntries = hermesSurface.refused_entry_slugs.map((slug) => {
    const entry = entryBySlug.get(slug);
    if (!entry) {
      throw new Error(`Hermes refused entry is missing from blueprints.entries: ${slug}`);
    }

    return entry;
  });
  const browsePaths = hermesSurface.discovery.browse_paths.map((browsePath) => {
    const category = categoryBySlug.get(browsePath.category_slug);
    if (!category) {
      throw new Error(`Hermes browse path references unknown category: ${browsePath.category_slug}`);
    }

    const entries = browsePath.entry_slugs.map(resolveHermesEntry);
    for (const entry of entries) {
      if (categoryByEntrySlug.get(entry.slug) !== category.slug) {
        throw new Error(
          `Hermes browse path ${browsePath.slug} includes ${entry.slug}, which is not in ${category.slug}`
        );
      }
    }

    return {
      ...browsePath,
      category,
      entries
    };
  });

  const browsePathByCategorySlug = new Map(browsePaths.map((browsePath) => [browsePath.category.slug, browsePath]));
  for (const category of hermesSurface.categories) {
    if (!browsePathByCategorySlug.has(category.slug)) {
      throw new Error(`Hermes browse docs are missing a browse path for ${category.slug}`);
    }
  }

  const canonCounts = canon.entries.reduce((counts, entry) => {
    counts[entry.kind] = (counts[entry.kind] ?? 0) + 1;
    return counts;
  }, {});

  return {
    hermesSurface,
    entryBySlug,
    categoryByEntrySlug,
    featuredEntries,
    refusedEntries,
    browsePaths,
    browsePathByCategorySlug,
    hermesCount: hermesEntries.length,
    canonCount: canon.entries.length,
    refusedCount: hermesSurface.refused_entry_slugs.length,
    spellCount: canonCounts.spell ?? 0,
    skillCount: canonCounts.skill ?? 0
  };
}

function renderHermesEntryReference(entry, categoryByEntrySlug) {
  const categorySlug = categoryByEntrySlug.get(entry.slug);
  if (!categorySlug) {
    throw new Error(`Missing Hermes category for ${entry.slug}`);
  }

  return markdownLink(entry.name, hermesSkillDocPath(categorySlug, entry.slug));
}

function renderFeaturedShelf(entries, categoryByEntrySlug) {
  return entries.map(
    (entry, index) =>
      `${index + 1}. ${renderHermesEntryReference(entry, categoryByEntrySlug)} ${renderBadges(
        entry.reality_tier,
        entry.literalness
      )} - ${entry.tagline}`
  );
}

function renderAsciiBanner(hermesCount) {
  return [
    "```",
    "    ╔═══════════════════════════════════════════════════╗",
    "    ║                                                   ║",
    "    ║    W I Z A R D S   O F   T H E   G H O S T S     ║",
    "    ║                                                   ║",
    `    ║      ${String(hermesCount).padStart(3)} spells for the ghost in the machine      ║`,
    "    ║                                                   ║",
    "    ╚═══════════════════════════════════════════════════╝",
    "```"
  ].join("\n");
}

function renderSpellCircle(categories) {
  const catMap = new Map(categories.map((c) => [c.slug, c]));
  const inv = catMap.get("investigation-and-preparation");
  const act = catMap.get("actions-access-and-automation");
  const mon = catMap.get("monitoring-and-protection");
  const msg = catMap.get("messaging-and-coordination");
  const rep = catMap.get("repair-and-recovery");
  const sim = catMap.get("simulation-and-staging");
  const inf = catMap.get("influence-and-behavior");
  const con = catMap.get("containment-and-intervention");
  const columnWidth = 20;
  const columns = (left, center, right) =>
    `    │ ${left.padEnd(columnWidth)} ${center.padEnd(columnWidth)} ${right.padEnd(columnWidth)} │`;

  return [
    "```",
    "    ┌────────────────────────────────────────────────────────────────────┐",
    columns(`Simulation (${sim.entry_slugs.length})`, `Investigation (${inv.entry_slugs.length})`, `Actions (${act.entry_slugs.length})`),
    columns(`Influence (${inf.entry_slugs.length})`, "GHOST IN THE MACHINE", `Monitoring (${mon.entry_slugs.length})`),
    columns(`Containment (${con.entry_slugs.length})`, `Repair (${rep.entry_slugs.length})`, `Messaging (${msg.entry_slugs.length})`),
    "    └────────────────────────────────────────────────────────────────────┘",
    "```"
  ].join("\n");
}

function renderSpellCards(entries, categoryByEntrySlug) {
  const rows = [];
  for (let i = 0; i < entries.length; i += 2) {
    const left = entries[i];
    const right = entries[i + 1];

    const card = (entry) => {
      const emoji = entry.openclaw?.emoji || "";
      const catSlug = categoryByEntrySlug.get(entry.slug);
      const link = markdownLink(entry.name, hermesSkillDocPath(catSlug, entry.slug));
      return `${emoji} **${link}** — ${entry.tagline}`;
    };

    if (right) {
      rows.push(`| ${card(left)} | ${card(right)} |`);
    } else {
      rows.push(`| ${card(left)} | |`);
    }
  }
  return [
    "| | |",
    "|---|---|",
    ...rows
  ].join("\n");
}

function formatPercent(ratio) {
  return `${(ratio * 100).toFixed(1)}%`;
}

function formatPoints(delta) {
  return `${delta >= 0 ? "+" : ""}${(delta * 100).toFixed(1)}pp`;
}

function buildDspyContext(blueprints, dspyEvalSummary, baselineEvalSummary, dspyRouterArtifact) {
  if (
    !dspyEvalSummary ||
    dspyEvalSummary.status !== "evaluated" ||
    !baselineEvalSummary ||
    baselineEvalSummary.status !== "evaluated"
  ) {
    return null;
  }

  const entryBySlug = new Map(blueprints.entries.map((entry) => [entry.slug, entry]));
  const spotlightEntries = dspySpotlightSlugs
    .map((slug) => entryBySlug.get(slug))
    .filter(Boolean);

  const bootstrappedDemos =
    dspyRouterArtifact?.predict?.demos?.filter((demo) => demo && demo.augmented).length ?? null;

  return {
    correct: dspyEvalSummary.correct,
    total: dspyEvalSummary.total_eval_rows,
    accuracy: dspyEvalSummary.accuracy,
    baselineCorrect: baselineEvalSummary.correct,
    baselineTotal: baselineEvalSummary.total_eval_rows,
    baselineAccuracy: baselineEvalSummary.accuracy,
    accuracyLift: dspyEvalSummary.accuracy - baselineEvalSummary.accuracy,
    bootstrappedDemos,
    categoryCount: Array.isArray(dspyRouterArtifact?.predict?.signature?.fields)
      ? dspyRouterArtifact.predict.signature.fields.at(-1)?.description
          ?.replace("One of: ", "")
          ?.split(", ")
          ?.filter(Boolean).length ?? 8
      : 8,
    spotlightEntries
  };
}

function buildGepaContext(blueprints, optimizedEvalSummary) {
  if (
    !optimizedEvalSummary ||
    optimizedEvalSummary.status !== "evaluated" ||
    typeof optimizedEvalSummary.delta !== "number" ||
    optimizedEvalSummary.delta <= 0
  ) {
    return null;
  }

  const entryBySlug = new Map(blueprints.entries.map((entry) => [entry.slug, entry]));
  const entry = entryBySlug.get(optimizedEvalSummary.slug);
  if (!entry) {
    return null;
  }

  return {
    entry,
    baselineAverageScore: optimizedEvalSummary.baseline_average_score,
    optimizedAverageScore: optimizedEvalSummary.optimized_average_score,
    delta: optimizedEvalSummary.delta
  };
}

function renderReadmeBrowseTable(browsePaths) {
  return [
    "| If you want to... | Start here | Hermes shelf |",
    "| --- | --- | --- |",
    ...browsePaths.map(
      (browsePath) => {
        const categoryByEntrySlug = new Map(
          browsePath.entries.map((entry) => [entry.slug, browsePath.category.slug])
        );

        return (
        `| ${browsePath.title} | ${browsePath.entries
          .map((entry) => renderHermesEntryReference(entry, categoryByEntrySlug))
          .join(", ")} | ${markdownLink(
          `${browsePath.category.title} (${browsePath.category.entry_slugs.length})`,
          `GRIMOIRE.md#${browsePath.category.slug}`
        )} |`
        );
      }
    )
  ].join("\n");
}

function renderGrimoireBrowsePaths(browsePaths, categoryByEntrySlug) {
  return browsePaths.flatMap((browsePath) => [
    `### ${browsePath.title}`,
    "",
    browsePath.description,
    "",
    `- Shelf: ${markdownLink(
      `${browsePath.category.title} (${browsePath.category.entry_slugs.length})`,
      `#${browsePath.category.slug}`
    )}`,
    `- Start with: ${browsePath.entries
      .map((entry) => renderHermesEntryReference(entry, categoryByEntrySlug))
      .join(", ")}`,
    ""
  ]);
}

function renderCategoryIndexEntry(entry, categoryByEntrySlug) {
  return `- ${renderHermesEntryReference(entry, categoryByEntrySlug)} ${renderBadges(
    entry.kind,
    entry.reality_tier,
    entry.literalness
  )} - ${entry.tagline}`;
}

function renderGrimoireCategory(category, browsePath, entryBySlug, categoryByEntrySlug) {
  const entries = category.entry_slugs.map((slug) => {
    const entry = entryBySlug.get(slug);
    if (!entry) {
      throw new Error(`Missing entry for ${slug}`);
    }
    return entry;
  });

  return [
    `<a id="${category.slug}"></a>`,
    `## ${category.title}`,
    "",
    category.description,
    "",
    `- Best for: ${browsePath.description}`,
    `- Start with: ${browsePath.entries
      .map((entry) => renderHermesEntryReference(entry, categoryByEntrySlug))
      .join(", ")}`,
    "",
    "<details>",
    `<summary>See all ${category.entry_slugs.length} skills in this shelf</summary>`,
    "",
    ...entries.map((entry) => renderCategoryIndexEntry(entry, categoryByEntrySlug)),
    "",
    "</details>",
    ""
  ].join("\n");
}

function renderReadme(blueprints, canon, dspy, gepa) {
  const discovery = buildDiscoveryContext(blueprints, canon);

  return [
    renderRootDocPreamble(),
    "",
    renderAsciiBanner(discovery.hermesCount),
    "",
    "Unofficial Hermes Agent skill pack built from fantasy spell and skill names.",
    "",
    "Not affiliated with or endorsed by Wizards of the Coast.",
    "",
    renderSpellCircle(discovery.hermesSurface.categories),
    "",
    "`wizardsoftheghosts` turns public fifth-edition spell and skill names into a product-shaped Hermes skill pack for investigation, automation, monitoring, messaging, repair, staging, and tightly scoped intervention.",
    "",
    "## Quick Install",
    "",
    "```bash",
    "npm run expand:blueprints",
    "npm run build:skills",
    "HERMES_HOME=$PWD/.hermes npm run install:hermes-skills",
    "```",
    "",
    "Or install into your default Hermes home:",
    "",
    "```bash",
    "npm run install:hermes-skills",
    "```",
    "",
    "## Hermes Expectations",
    "",
    "- Hermes discovers installed skills from `~/.hermes/skills` or `$HERMES_HOME/skills`; `npm run install:hermes-skills` copies the generated docs there.",
    "- The installable Hermes surface lives in `generated/hermes/`. Those files are procedural markdown with YAML frontmatter, not executable plugins by themselves.",
    "- Most of this pack is best used as reasoning, investigation, planning, triage, or operating-mode scaffolding inside a normal Hermes session.",
    "- In practice, skills like `detect-magic`, `mage-hand`, `zone-of-truth`, `feather-fall`, and `unseen-servant` work especially well as direct Hermes prompts.",
    "- Some skills mention env vars, APIs, or external systems, but this repo does not currently ship a dedicated Hermes integration layer for Home Assistant, Slack, or other services. Those procedures become real only if your Hermes environment already has the matching tools, credentials, and permissions.",
    "",
    "## What Ships",
    "",
    `- \`${discovery.hermesCount}\` Hermes skills drawn from \`${discovery.canonCount}\` public canon names (\`${discovery.spellCount}\` spells, \`${discovery.skillCount}\` skills)`,
    `- \`${discovery.hermesSurface.categories.length}\` Hermes shelves for progressive discovery instead of one giant list`,
    `- \`${discovery.featuredEntries.length}\` featured entry points plus \`${discovery.browsePaths.length}\` intent-driven browse paths on GitHub`,
    `- public low-risk Hermes surface with \`${discovery.refusedCount}\` refused coercion and memory spells kept off release`,
    "",
    "## Best First Skills",
    "",
    renderSpellCards(discovery.featuredEntries, discovery.categoryByEntrySlug),
    "",
    ...(gepa
      ? [
          `Recent GEPA upgrade: ${renderHermesEntryReference(
            gepa.entry,
            discovery.categoryByEntrySlug
          )} was promoted after a Codex-backed spell-level run improved full eval from \`${formatPercent(
            gepa.baselineAverageScore
          )}\` to \`${formatPercent(gepa.optimizedAverageScore)}\` (\`${formatPoints(
            gepa.delta
          )}\`). The upgraded copy is sharper about tested containment boundaries, outside-the-cage observation, and explicit release conditions before anything descends.`,
          ""
        ]
      : []),
    "Need badges, browse paths, or the bigger picture? Open [GRIMOIRE.md](GRIMOIRE.md) for the full browse layer.",
    "",
    "## Find Your Shelf",
    "",
    renderReadmeBrowseTable(discovery.browsePaths),
    "",
    "## Browse Deeper",
    "",
    `- [GRIMOIRE.md](GRIMOIRE.md) for the featured shelf, browse paths, and full linked category index`,
    "- `generated/hermes/<category>/<skill>/SKILL.md` after `npm run build:skills` for the exact procedural skill docs Hermes installs",
    "- `generated/openclaw/` for the separate OpenClaw-oriented output surface generated from the same source material",
    "- `catalog/blueprints.json` plus `scripts/render-skills.mjs` for the source-of-truth and renderer",
    "",
    "## Build From Source",
    "",
    "Source of truth:",
    "",
    "1. `catalog/canon.json`",
    "2. `catalog/blueprints.json`",
    "3. `scripts/expand-blueprints.mjs`",
    "4. `scripts/render-skills.mjs`",
    "",
    "Default workflow:",
    "",
    "```bash",
    "npm run sync:canon",
    "npm run expand:blueprints",
    "npm run build:skills",
    "npm run export:linear",
    "```",
    "",
    "Or:",
    "",
    "```bash",
    "npm run bootstrap",
    "```",
    "",
    "## Verification",
    "",
    "```bash",
    "npm run verify",
    "```",
    "",
    "`npm run verify` checks the generated Hermes and OpenClaw surfaces, then performs sandbox installs into temporary Hermes and Codex homes so you can catch packaging drift before release.",
    "",
    "## DSPy Router",
    "",
    "The repo ships two Hermes routing paths under [`catalog/dspy/`](catalog/dspy/): a deterministic lexical baseline and an optional DSPy category router.",
    "",
    ...(dspy
      ? [
          `- Current held-out result: \`${dspy.correct}/${dspy.total}\` = \`${formatPercent(
            dspy.accuracy
          )}\` with the Codex-backed DSPy router`,
          `- Baseline comparison: \`${dspy.baselineCorrect}/${dspy.baselineTotal}\` = \`${formatPercent(
            dspy.baselineAccuracy
          )}\` for the lexical router, a \`${formatPoints(dspy.accuracyLift)}\` lift for DSPy`,
          `- Current scope: \`${dspy.categoryCount}\`-way Hermes category routing from plain-English prompts into the right shelf`,
          dspy.bootstrappedDemos
            ? `- Optimized prompt core: \`${dspy.bootstrappedDemos}\` bootstrapped few-shot demos selected by DSPy`
            : "- Optimized prompt core: bootstrapped few-shot demos selected by DSPy",
          ""
        ]
      : [
          "- The lexical baseline is deterministic and local-only.",
          "- The DSPy path stays optional and requires both the `dspy` package and an explicit backend configuration.",
          ""
        ]),
    "This makes the pack materially easier to use from plain language. You no longer need to know the spell name first to land on the right shelf.",
    "",
    ...(dspy?.spotlightEntries?.length
      ? [
          "Spells that became more practically valuable once plain-English routing started working:",
          "",
          renderSpellCards(dspy.spotlightEntries, discovery.categoryByEntrySlug),
          ""
        ]
      : []),
    "Set up the Python side in a repo-local virtualenv:",
    "",
    "```bash",
    "uv venv .venv",
    "uv pip install --python .venv/bin/python -r requirements-dspy.txt",
    "```",
    "",
    "Baseline-only flow:",
    "",
    "```bash",
    "npm run dspy:validate",
    "npm run dspy:baseline",
    "```",
    "",
    "Codex-backed DSPy flow:",
    "",
    "```bash",
    "export DSPY_MODEL=codex-exec/default",
    "export DSPY_TEMPERATURE=0",
    "export DSPY_MAX_TOKENS=256",
    "",
    "bash scripts/dspy_full_run.sh",
    "```",
    "",
    "This shells out to local `codex exec` for each DSPy inference. It remains slower than an OpenAI-compatible HTTP backend, but the full compile+eval path is now proven practical as an unattended background job. See [`catalog/dspy/README.md`](catalog/dspy/README.md) and [`docs/dspy-router-runbook.md`](docs/dspy-router-runbook.md) for artifact details and the exact runbook.",
    "",
    "## Safety and IP",
    "",
    `The public Hermes surface intentionally refuses ${renderCodeList(
      discovery.refusedEntries.map((entry) => entry.name)
    )}.`,
    "",
    "Original code and writing in this repo are released under `CC0-1.0`. That does not grant rights in Wizards of the Coast IP, trademarks, logos, artwork, or official rules text. This repo stays free, unofficial, and clearly separate from any official Wizards product line.",
    "",
    "See [LEGAL.md](LEGAL.md) for the current fan-content and IP posture.",
    ""
  ].join("\n");
}

function renderGrimoire(blueprints, canon, dspy) {
  const discovery = buildDiscoveryContext(blueprints, canon);

  return [
    renderRootDocPreamble(),
    "",
    "# Grimoire",
    "",
    "`GRIMOIRE.md` is the repo-facing browse layer for the Hermes skill pack: a tight starter shelf up top, intent-driven routes in the middle, and a full linked category index only when you open it.",
    "",
    "## At a Glance",
    "",
    `- \`${discovery.hermesCount}\` Hermes skills from \`${discovery.canonCount}\` public canon names`,
    `- \`${discovery.spellCount}\` spell names and \`${discovery.skillCount}\` skill names reinterpreted as software-facing agent skills`,
    `- \`${discovery.hermesSurface.categories.length}\` Hermes shelves with repo-facing browse docs and locally generated install docs`,
    `- \`${discovery.refusedCount}\` coercion and memory spells intentionally kept off the public Hermes surface`,
    "",
    "If you're new, start with the featured shelf. If you already know the kind of job you have, use the browse paths. Open the category details only when you want the full spellbook.",
    "",
    "The sigils mean two things: `shipping-now` / `prototype` / `speculative` tell you how honest the runtime claim is, while `metaphorical` / `hybrid` / `literal` tell you how closely the software behavior matches the fantasy effect.",
    "",
    "For Hermes users, read these as installable procedures, not bundled executables. Many of the strongest entries are reasoning modes or operator checklists; any skill that touches a real external system still depends on whatever tools, permissions, and integrations your Hermes session already has.",
    "",
    "Need the exact install docs? Run `npm run build:skills` locally and open `generated/hermes/<category>/<skill>/SKILL.md`.",
    "",
    ...(dspy
      ? [
          "## DSPy-Enabled Discovery",
          "",
          `The current Codex-backed DSPy router scores \`${dspy.correct}/${dspy.total}\` = \`${formatPercent(
            dspy.accuracy
          )}\` on held-out Hermes category routing, ahead of the lexical baseline by \`${formatPoints(
            dspy.accuracyLift
          )}\`. In practice that means more people can reach the right shelf from natural language instead of memorizing the spellbook first.`,
          "",
          ...(dspy.spotlightEntries?.length
            ? [
                "The biggest discoverability upgrade lands on less obvious but high-value entries:",
                "",
                ...dspy.spotlightEntries.map(
                  (entry) =>
                    `- ${renderHermesEntryReference(entry, discovery.categoryByEntrySlug)} ${renderBadges(
                      entry.reality_tier,
                      entry.literalness
                    )} - ${entry.tagline}`
                ),
                ""
              ]
            : []),
          "For the measured artifacts and runbook, open [`catalog/dspy/README.md`](catalog/dspy/README.md) and [`docs/dspy-router-runbook.md`](docs/dspy-router-runbook.md).",
          ""
        ]
      : []),
    '<a id="featured-shelf"></a>',
    "## Featured Shelf",
    "",
    ...renderFeaturedShelf(discovery.featuredEntries, discovery.categoryByEntrySlug),
    "",
    '<a id="browse-paths"></a>',
    "## Browse Paths",
    "",
    ...renderGrimoireBrowsePaths(discovery.browsePaths, discovery.categoryByEntrySlug),
    '<a id="full-category-index"></a>',
    "## Browse by Category",
    "",
    "Each shelf below starts with a few strong entry points. Open the details block only when you want the full list.",
    "",
    ...discovery.hermesSurface.categories.map((category) =>
      renderGrimoireCategory(
        category,
        discovery.browsePathByCategorySlug.get(category.slug),
        discovery.entryBySlug,
        discovery.categoryByEntrySlug
      )
    ),
    "## Public Surface Guardrails",
    "",
    "The public Hermes surface intentionally does not ship:",
    "",
    ...discovery.refusedEntries.map((entry) => `- \`${entry.name}\``),
    "",
    "This remains a free unofficial fan project built from original reinterpretations, not an official Wizards release. See [LEGAL.md](LEGAL.md) for the repo's current IP posture.",
    ""
  ].join("\n");
}

async function writeOpenClawEntry(entry, canon) {
  const skillDir = path.join(openclawDir, entry.slug);
  await mkdir(skillDir, { recursive: true });
  await writeFile(path.join(skillDir, "SKILL.md"), `${renderOpenClawSkillMd(entry, canon)}\n`);
}

async function writeHermesCategory(category) {
  const categoryDir = path.join(hermesDir, category.slug);
  await mkdir(categoryDir, { recursive: true });
  await writeFile(path.join(categoryDir, "DESCRIPTION.md"), `${renderHermesCategoryDescription(category)}\n`);
}

async function writeHermesEntry(entry, canon, category, repoMeta, asciiArtBySlug) {
  const skillDir = path.join(hermesDir, category.slug, entry.slug);
  await mkdir(skillDir, { recursive: true });
  await writeFile(
    path.join(skillDir, "SKILL.md"),
    `${renderHermesSkillMd(entry, canon, category, repoMeta, asciiArtBySlug)}\n`
  );
}

async function writeDiscoveryDocs(blueprints, canon, dspy, gepa) {
  await Promise.all([
    writeFile(readmePath, `${renderReadme(blueprints, canon, dspy, gepa)}\n`),
    writeFile(grimoirePath, `${renderGrimoire(blueprints, canon, dspy)}\n`)
  ]);
}

async function main() {
  const [
    blueprints,
    canon,
    packageJson,
    dspyEvalSummary,
    baselineEvalSummary,
    dspyRouterArtifact,
    forcecageOptimizedEval
  ] = await Promise.all([
    readFile(blueprintPath, "utf8").then((content) => JSON.parse(content)),
    readFile(canonPath, "utf8").then((content) => JSON.parse(content)),
    readFile(packagePath, "utf8").then((content) => JSON.parse(content)),
    readOptionalJson(dspyEvalSummaryPath),
    readOptionalJson(baselineEvalSummaryPath),
    readOptionalJson(dspyRouterArtifactPath),
    readOptionalJson(forcecageOptimizedEvalPath)
  ]);

  const asciiArtBySlug = new Map(
    (
      await Promise.all(
        blueprints.entries.map(async (entry) => {
          const art = await readOptionalText(path.join(asciiArtOverridesDir, `${entry.slug}.txt`));
          return [entry.slug, art];
        })
      )
    ).filter(([, art]) => Boolean(art?.trim()))
  );

  const canonById = new Map(canon.entries.map((entry) => [entry.id, entry]));
  const hermesSurface = blueprints.surfaces?.hermes;

  if (!hermesSurface?.categories?.length) {
    throw new Error("catalog/blueprints.json is missing surfaces.hermes.categories");
  }

  const hermesCategories = hermesSurface.categories;
  const hermesCategoryBySlug = new Map(hermesCategories.map((category) => [category.slug, category]));
  const hermesEntryCategory = new Map();

  for (const category of hermesCategories) {
    for (const entrySlug of category.entry_slugs) {
      if (hermesEntryCategory.has(entrySlug)) {
        throw new Error(`${entrySlug} is assigned to multiple Hermes categories`);
      }
      hermesEntryCategory.set(entrySlug, category.slug);
    }
  }

  await rm(generatedDir, { recursive: true, force: true });
  await mkdir(openclawDir, { recursive: true });
  await mkdir(hermesDir, { recursive: true });

  for (const category of hermesCategories) {
    await writeHermesCategory(category);
  }

  const repoMeta = {
    author: "Wizards of the Ghosts",
    homepage: packageJson.homepage,
    license: packageJson.license ?? "CC0-1.0",
    version: packageJson.version ?? "1.0.0"
  };

  let openclawCount = 0;
  let hermesCount = 0;

  for (const entry of blueprints.entries) {
    if (!canonById.has(entry.canonical_id)) {
      throw new Error(`${entry.slug}: canonical_id ${entry.canonical_id} not found in catalog/canon.json`);
    }

    const canonicalEntry = canonById.get(entry.canonical_id);

    if (entry.provider_targets.includes("openclaw")) {
      await writeOpenClawEntry(entry, canonicalEntry);
      openclawCount += 1;
    }

    if (entry.provider_targets.includes("hermes")) {
      const categorySlug = hermesEntryCategory.get(entry.slug);
      if (!categorySlug) {
        throw new Error(`${entry.slug}: missing Hermes category assignment`);
      }

      const category = hermesCategoryBySlug.get(categorySlug);
      await writeHermesEntry(entry, canonicalEntry, category, repoMeta, asciiArtBySlug);
      hermesCount += 1;
    }
  }

  const dspy = buildDspyContext(blueprints, dspyEvalSummary, baselineEvalSummary, dspyRouterArtifact);
  const gepa = buildGepaContext(blueprints, forcecageOptimizedEval);

  await writeDiscoveryDocs(blueprints, canon, dspy, gepa);

  console.log(`Rendered ${openclawCount} OpenClaw skills into ${openclawDir}`);
  console.log(`Rendered ${hermesCount} Hermes skills into ${hermesDir}`);
  console.log(`Rendered discovery docs into ${readmePath} and ${grimoirePath}`);
}

await main();
