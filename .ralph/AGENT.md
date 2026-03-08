# Ralph Agent Configuration

## Build Instructions

```bash
# Build skill folders from blueprints
npm run build:skills
```

## Test Instructions

```bash
# Validate blueprints against schema
npm run validate

# Build and check output
npm run build:skills
```

## Export Instructions

```bash
# Export Linear seed files
npm run export:linear
```

## Key Commands

```bash
# Check entry count
node -e "const b = require('./catalog/blueprints.json'); console.log(b.entries.length + ' entries')"

# Find entries by slug pattern
node -e "const b = require('./catalog/blueprints.json'); b.entries.filter(e => e.slug.includes('PATTERN')).forEach(e => console.log(e.slug))"
```

## Notes
- Source of truth: `catalog/blueprints.json`
- Build output: `generated/` (345 folders)
- Always run `npm run build:skills` after editing blueprints
- Schema: `catalog/blueprints.schema.json`
