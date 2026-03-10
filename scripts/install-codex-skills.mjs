import { mkdir, readdir, readlink, symlink, lstat, unlink } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(scriptDir, '..');
const sourceRoot = path.join(repoRoot, 'generated', 'openclaw');
const legacyGeneratedRoots = [
  path.join(repoRoot, 'generated', 'openai'),
  path.join(repoRoot, 'generated', 'openclaw')
];
const codexHome = process.env.CODEX_HOME ?? path.join(process.env.HOME ?? '', '.codex');
const destinationRoot = path.join(codexHome, 'skills');

if (!process.env.HOME && !process.env.CODEX_HOME) {
  throw new Error('HOME or CODEX_HOME must be set to install Codex skills.');
}

const entries = await readdir(sourceRoot, { withFileTypes: true });
const skillDirs = entries
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name)
  .sort();

await mkdir(destinationRoot, { recursive: true });

const created = [];
const relinked = [];
const unchanged = [];
const conflicts = [];

for (const skillName of skillDirs) {
  const sourceDir = path.join(sourceRoot, skillName);
  const skillFile = path.join(sourceDir, 'SKILL.md');
  const destinationDir = path.join(destinationRoot, skillName);

  try {
    await lstat(skillFile);
  } catch {
    continue;
  }

  try {
    const stat = await lstat(destinationDir);
    if (!stat.isSymbolicLink()) {
      conflicts.push(`${skillName}: destination exists and is not a symlink`);
      continue;
    }

    const target = await readlink(destinationDir);
    const resolvedTarget = path.resolve(path.dirname(destinationDir), target);
    if (resolvedTarget === sourceDir) {
      unchanged.push(skillName);
      continue;
    }

    if (
      legacyGeneratedRoots.some(
        (root) => resolvedTarget === root || resolvedTarget.startsWith(`${root}${path.sep}`)
      )
    ) {
      await unlink(destinationDir);
      await symlink(sourceDir, destinationDir, 'dir');
      relinked.push(skillName);
      continue;
    }

    conflicts.push(`${skillName}: symlink points to ${resolvedTarget}`);
    continue;
  } catch (error) {
    if (error?.code !== 'ENOENT') {
      throw error;
    }
  }

  await symlink(sourceDir, destinationDir, 'dir');
  created.push(skillName);
}

console.log(`Codex skill source: ${sourceRoot}`);
console.log(`Codex skill destination: ${destinationRoot}`);
console.log(`Generated spell skills detected: ${skillDirs.length}`);
console.log(`Created links: ${created.length}`);
console.log(`Repointed legacy links: ${relinked.length}`);
console.log(`Already linked: ${unchanged.length}`);
console.log(`Conflicts: ${conflicts.length}`);

if (created.length > 0) {
  console.log(`First created: ${created.slice(0, 10).join(', ')}`);
}

if (relinked.length > 0) {
  console.log(`First repointed: ${relinked.slice(0, 10).join(', ')}`);
}

if (conflicts.length > 0) {
  console.error('Conflicts:');
  for (const conflict of conflicts) {
    console.error(`- ${conflict}`);
  }
  process.exitCode = 1;
} else {
  console.log('Restart Codex to pick up new skills.');
}
