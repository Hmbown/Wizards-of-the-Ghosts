import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const catalogDir = path.join(rootDir, "catalog");
const blueprintsPath = path.join(catalogDir, "blueprints.json");
const canonPath = path.join(catalogDir, "canon.json");
const jsonOutputPath = path.join(catalogDir, "linear-seed.json");
const csvOutputPath = path.join(catalogDir, "linear-seed.csv");

function csvEscape(value) {
  const text = String(value ?? "");
  if (/[",\n]/.test(text)) {
    return `"${text.replace(/"/g, "\"\"")}"`;
  }
  return text;
}

function buildDescription(entry, canon) {
  const providers = entry.provider_targets.join(", ");
  const lines = [
    `## Spellbook Entry`,
    ``,
    `- Kind: ${entry.kind}`,
    `- Canonical source: ${canon.name}`,
    `- Canonical source URL: ${canon.source_url}`,
    `- Reality tier: ${entry.reality_tier}`,
    `- Literalness: ${entry.literalness}`,
    `- Provider targets: ${providers}`,
    ``,
    `## Tagline`,
    ``,
    entry.tagline,
    ``,
    `## Current Interpretation`,
    ``,
    entry.description,
    ``,
    `## Default Invocation`,
    ``,
    entry.default_prompt,
    ``,
    `## Initial Done When`,
    ``,
    `- The blueprint is reviewed for naming, tier, and provider targets`,
    `- The provider-specific skill output renders cleanly`,
    `- Any safety concerns are called out explicitly`
  ];

  return lines.join("\n");
}

function buildLabels(entry) {
  const labels = ["ai"];

  if (entry.kind === "spell") {
    labels.push("type:feature");
  } else {
    labels.push("docs");
  }

  if (entry.provider_targets.includes("openclaw")) {
    labels.push("automation");
  }

  if (entry.reality_tier !== "shipping-now") {
    labels.push("architecture");
  }

  if (entry.literalness === "literal") {
    labels.push("security");
  }

  return [...new Set(labels)];
}

function buildPriority(entry) {
  if (entry.reality_tier === "shipping-now" && entry.provider_targets.includes("openclaw")) {
    return 2;
  }
  if (entry.reality_tier === "shipping-now") {
    return 3;
  }
  return 4;
}

async function main() {
  const blueprints = JSON.parse(await readFile(blueprintsPath, "utf8"));
  const canon = JSON.parse(await readFile(canonPath, "utf8"));
  const canonById = new Map(canon.entries.map((entry) => [entry.id, entry]));

  const payload = blueprints.entries.map((entry) => {
    const canonical = canonById.get(entry.canonical_id);
    return {
      title: `${entry.name} (${entry.kind})`,
      slug: entry.slug,
      kind: entry.kind,
      canonical_id: entry.canonical_id,
      reality_tier: entry.reality_tier,
      literalness: entry.literalness,
      provider_targets: entry.provider_targets,
      priority: buildPriority(entry),
      labels: buildLabels(entry),
      description: buildDescription(entry, canonical)
    };
  });

  const csvHeader = [
    "title",
    "slug",
    "kind",
    "canonical_id",
    "reality_tier",
    "literalness",
    "provider_targets",
    "priority",
    "labels",
    "description"
  ];

  const csvRows = [
    csvHeader.join(","),
    ...payload.map((row) =>
      [
        row.title,
        row.slug,
        row.kind,
        row.canonical_id,
        row.reality_tier,
        row.literalness,
        row.provider_targets.join("|"),
        row.priority,
        row.labels.join("|"),
        row.description
      ]
        .map(csvEscape)
        .join(",")
    )
  ];

  await writeFile(jsonOutputPath, `${JSON.stringify({ entries: payload }, null, 2)}\n`);
  await writeFile(csvOutputPath, `${csvRows.join("\n")}\n`);

  console.log(
    `Exported ${payload.length} Linear seed rows to ${jsonOutputPath} and ${csvOutputPath}`
  );
}

await main();
