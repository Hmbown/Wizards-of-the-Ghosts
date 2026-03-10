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

const openclawDir = path.join(generatedDir, "openclaw");
const hermesDir = path.join(generatedDir, "hermes");

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

  lines.push(`    homepage: ${yamlString(repoMeta.homepage)}`);
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

function renderHermesSkillMd(entry, canon, category, repoMeta) {
  return [
    renderHermesFrontmatter(entry, category, repoMeta),
    "",
    `# ${entry.name}`,
    "",
    entry.tagline,
    "",
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

async function writeHermesEntry(entry, canon, category, repoMeta) {
  const skillDir = path.join(hermesDir, category.slug, entry.slug);
  await mkdir(skillDir, { recursive: true });
  await writeFile(
    path.join(skillDir, "SKILL.md"),
    `${renderHermesSkillMd(entry, canon, category, repoMeta)}\n`
  );
}

async function main() {
  const [blueprints, canon, packageJson] = await Promise.all([
    readFile(blueprintPath, "utf8").then((content) => JSON.parse(content)),
    readFile(canonPath, "utf8").then((content) => JSON.parse(content)),
    readFile(packagePath, "utf8").then((content) => JSON.parse(content))
  ]);

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
      await writeHermesEntry(entry, canonicalEntry, category, repoMeta);
      hermesCount += 1;
    }
  }

  console.log(`Rendered ${openclawCount} OpenClaw skills into ${openclawDir}`);
  console.log(`Rendered ${hermesCount} Hermes skills into ${hermesDir}`);
}

await main();
