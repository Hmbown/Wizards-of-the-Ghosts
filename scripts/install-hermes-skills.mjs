import { cp, lstat, mkdir, readFile, readdir, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(scriptDir, "..");
const sourceRoot = path.join(repoRoot, "generated", "hermes");
const hermesHome = process.env.HERMES_HOME ?? path.join(process.env.HOME ?? "", ".hermes");
const destinationRoot = path.join(hermesHome, "skills");
const manifestPath = path.join(destinationRoot, ".wizardsoftheghosts-manifest.json");

if (!process.env.HOME && !process.env.HERMES_HOME) {
  throw new Error("HOME or HERMES_HOME must be set to install Hermes skills.");
}

async function pathExists(targetPath) {
  try {
    await lstat(targetPath);
    return true;
  } catch (error) {
    if (error?.code === "ENOENT") {
      return false;
    }
    throw error;
  }
}

async function loadManifest() {
  if (!(await pathExists(manifestPath))) {
    return { paths: [] };
  }

  return JSON.parse(await readFile(manifestPath, "utf8"));
}

async function collectInstallItems() {
  const items = [];
  const categories = await readdir(sourceRoot, { withFileTypes: true });

  for (const categoryEntry of categories) {
    if (!categoryEntry.isDirectory()) {
      continue;
    }

    const categoryDir = path.join(sourceRoot, categoryEntry.name);
    const descriptionPath = path.join(categoryDir, "DESCRIPTION.md");
    if (await pathExists(descriptionPath)) {
      items.push({ relativePath: path.join(categoryEntry.name, "DESCRIPTION.md"), type: "file" });
    }

    const skillEntries = await readdir(categoryDir, { withFileTypes: true });
    for (const skillEntry of skillEntries) {
      if (!skillEntry.isDirectory()) {
        continue;
      }

      const skillDir = path.join(categoryDir, skillEntry.name);
      if (await pathExists(path.join(skillDir, "SKILL.md"))) {
        items.push({ relativePath: path.join(categoryEntry.name, skillEntry.name), type: "dir" });
      }
    }
  }

  return items.sort((left, right) => left.relativePath.localeCompare(right.relativePath));
}

async function removeIfEmpty(targetPath) {
  if (!(await pathExists(targetPath))) {
    return false;
  }

  const entries = await readdir(targetPath);
  if (entries.length > 0) {
    return false;
  }

  await rm(targetPath, { recursive: true, force: true });
  return true;
}

const sourceExists = await pathExists(sourceRoot);
if (!sourceExists) {
  throw new Error(`Hermes skill source not found at ${sourceRoot}. Run npm run build:skills first.`);
}

await mkdir(destinationRoot, { recursive: true });

const previousManifest = await loadManifest();
const currentItems = await collectInstallItems();
const currentPaths = new Set(currentItems.map((item) => item.relativePath));
const previousManagedCategories = new Set(
  (previousManifest.paths ?? []).map((relativePath) => relativePath.split(path.sep)[0]).filter(Boolean)
);
const currentManagedCategories = new Set(
  currentItems.map((item) => item.relativePath.split(path.sep)[0]).filter(Boolean)
);

for (const relativePath of [...(previousManifest.paths ?? [])].sort((left, right) => right.length - left.length)) {
  if (currentPaths.has(relativePath)) {
    continue;
  }

  const targetPath = path.join(destinationRoot, relativePath);
  await rm(targetPath, { recursive: true, force: true });
}

for (const categoryName of previousManagedCategories) {
  if (currentManagedCategories.has(categoryName)) {
    continue;
  }

  await removeIfEmpty(path.join(destinationRoot, categoryName));
}

const created = [];
const refreshed = [];
const conflicts = [];
const installedPaths = [];

for (const item of currentItems) {
  const sourcePath = path.join(sourceRoot, item.relativePath);
  const destinationPath = path.join(destinationRoot, item.relativePath);
  const previouslyManaged = (previousManifest.paths ?? []).includes(item.relativePath);

  if (previouslyManaged) {
    await rm(destinationPath, { recursive: true, force: true });
  } else if (await pathExists(destinationPath)) {
    conflicts.push(`${item.relativePath}: destination already exists`);
    continue;
  }

  await mkdir(path.dirname(destinationPath), { recursive: true });
  await cp(sourcePath, destinationPath, { force: false, recursive: item.type === "dir" });
  installedPaths.push(item.relativePath);

  if (previouslyManaged) {
    refreshed.push(item.relativePath);
  } else {
    created.push(item.relativePath);
  }
}

for (const entry of await readdir(destinationRoot, { withFileTypes: true })) {
  if (!entry.isDirectory()) {
    continue;
  }

  await removeIfEmpty(path.join(destinationRoot, entry.name));
}

await writeFile(
  manifestPath,
  `${JSON.stringify(
    {
      generated_at: new Date().toISOString(),
      source_root: sourceRoot,
      paths: installedPaths
    },
    null,
    2
  )}\n`
);

console.log(`Hermes skill source: ${sourceRoot}`);
console.log(`Hermes skill destination: ${destinationRoot}`);
console.log(`Generated Hermes install items detected: ${currentItems.length}`);
console.log(`Created items: ${created.length}`);
console.log(`Refreshed items: ${refreshed.length}`);
console.log(`Conflicts: ${conflicts.length}`);

if (created.length > 0) {
  console.log(`First created: ${created.slice(0, 10).join(", ")}`);
}

if (refreshed.length > 0) {
  console.log(`First refreshed: ${refreshed.slice(0, 10).join(", ")}`);
}

if (conflicts.length > 0) {
  console.error("Conflicts:");
  for (const conflict of conflicts) {
    console.error(`- ${conflict}`);
  }
  process.exitCode = 1;
} else {
  console.log("Run hermes skills list or restart Hermes to pick up the new skills.");
}
