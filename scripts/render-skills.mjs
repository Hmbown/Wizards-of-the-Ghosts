import { mkdir, readFile, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const catalogDir = path.join(rootDir, "catalog");
const generatedDir = path.join(rootDir, "generated");
const blueprintPath = path.join(catalogDir, "blueprints.json");
const canonPath = path.join(catalogDir, "canon.json");

const providerDir = path.join(generatedDir, "openclaw");

function yamlString(value) {
  return JSON.stringify(value);
}

function titleCase(slug) {
  return slug
    .split("-")
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}

function renderFrontmatter(entry) {
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

function renderSection(title, items, ordered = false) {
  const marker = ordered ? (index) => `${index + 1}.` : () => "-";
  return [`## ${title}`, "", ...items.map((item, index) => `${marker(index)} ${item}`), ""].join("\n");
}

function renderSkillMd(entry, canon, provider) {
  const header = renderFrontmatter(entry);

  return [
    header,
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

async function writeOpenClawEntry(entry, canon) {
  const skillDir = path.join(providerDir, entry.slug);
  await mkdir(skillDir, { recursive: true });
  await writeFile(path.join(skillDir, "SKILL.md"), `${renderSkillMd(entry, canon, "openclaw")}\n`);
}

async function main() {
  const blueprints = JSON.parse(await readFile(blueprintPath, "utf8"));
  const canon = JSON.parse(await readFile(canonPath, "utf8"));
  const canonById = new Map(canon.entries.map((entry) => [entry.id, entry]));

  await rm(generatedDir, { recursive: true, force: true });
  await mkdir(generatedDir, { recursive: true });
  await mkdir(providerDir, { recursive: true });

  let renderedCount = 0;

  for (const entry of blueprints.entries) {
    if (!canonById.has(entry.canonical_id)) {
      throw new Error(`${entry.slug}: canonical_id ${entry.canonical_id} not found in catalog/canon.json`);
    }

    const canonicalEntry = canonById.get(entry.canonical_id);

    if (entry.provider_targets.includes("openclaw")) {
      await writeOpenClawEntry(entry, canonicalEntry);
      renderedCount += 1;
    }
  }

  console.log(`Rendered ${renderedCount} OpenClaw skills into ${providerDir}`);
}

await main();
