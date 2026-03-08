import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const catalogDir = path.join(rootDir, "catalog");
const outputPath = path.join(catalogDir, "canon.json");

const sources = {
  skills: {
    id: "skills-2024-free-rules",
    kind: "skill",
    source_version: "2024-free-rules",
    url: "https://www.dndbeyond.com/sources/dnd/free-rules/playing-the-game"
  },
  spells: {
    id: "spells-basic-rules-public-index",
    kind: "spell",
    source_version: "basic-rules-public-index",
    url: "https://www.dndbeyond.com/sources/basic-rules/spells"
  }
};

function decodeEntities(input) {
  return input
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, "\"")
    .replace(/&#39;/g, "'")
    .replace(/&nbsp;/g, " ")
    .replace(/&rsquo;/g, "'")
    .replace(/&ldquo;/g, "\"")
    .replace(/&rdquo;/g, "\"")
    .replace(/&mdash;/g, "-")
    .replace(/&ndash;/g, "-");
}

function stripTags(input) {
  return decodeEntities(input.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim());
}

function slugify(name) {
  return name
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

async function fetchHtml(url) {
  const response = await fetch(url, {
    headers: {
      "user-agent": "wizardsoftheghosts/0.1 (+https://linear.app/shannon-labs/project/wizardsoftheghosts-8ba40e9929da)"
    }
  });

  if (!response.ok) {
    throw new Error(`Failed to fetch ${url}: ${response.status}`);
  }

  return response.text();
}

function uniqueSorted(values) {
  return [...new Set(values)].sort((left, right) => left.localeCompare(right));
}

function extractSkills(html) {
  const matches = [...html.matchAll(/<a class="tooltip-hover skill-tooltip"[^>]*>(.*?)<\/a>/g)];
  return uniqueSorted(
    matches
      .map((match) => stripTags(match[1]))
      .filter(Boolean)
  );
}

function extractSpells(html) {
  const start = html.indexOf('class="compendium-spell-lists"');
  const end = html.indexOf("</blockquote>", start);

  if (start === -1 || end === -1) {
    throw new Error("Could not locate public spell list block");
  }

  const block = html.slice(start, end);
  const matches = [...block.matchAll(/<a [^>]*href="#[^"]+"[^>]*>(.*?)<\/a>/g)];

  return uniqueSorted(
    matches
      .map((match) => stripTags(match[1]))
      .filter(Boolean)
  );
}

function buildEntries(kind, names, source) {
  return names.map((name) => ({
    id: `${kind}-${slugify(name)}`,
    kind,
    name,
    slug: slugify(name),
    source_id: source.id,
    source_version: source.source_version,
    source_url: source.url
  }));
}

async function main() {
  const [skillsHtml, spellsHtml] = await Promise.all([
    fetchHtml(sources.skills.url),
    fetchHtml(sources.spells.url)
  ]);

  const skills = buildEntries("skill", extractSkills(skillsHtml), sources.skills);
  const spells = buildEntries("spell", extractSpells(spellsHtml), sources.spells);
  const entries = [...skills, ...spells];

  const payload = {
    generated_at: new Date().toISOString(),
    counts: {
      skills: skills.length,
      spells: spells.length,
      total: entries.length
    },
    sources: Object.values(sources),
    entries
  };

  await mkdir(catalogDir, { recursive: true });
  await writeFile(outputPath, `${JSON.stringify(payload, null, 2)}\n`);

  console.log(
    `Wrote ${outputPath} with ${payload.counts.skills} skills and ${payload.counts.spells} spells`
  );
}

await main();
