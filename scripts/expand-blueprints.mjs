import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const canonPath = path.join(rootDir, "catalog", "canon.json");
const blueprintPath = path.join(rootDir, "catalog", "blueprints.json");

const archetypes = {
  analysis: {
    reality_tier: "shipping-now",
    literalness: "metaphorical",
    include_openclaw: true,
    tagline: "Interrogate opaque systems until the hidden mechanism becomes legible.",
    description: "Use this skill when the situation is unclear and you need evidence-backed visibility before acting.",
    when_to_use: [
      "You need to inspect an unfamiliar system, artifact, or trail of signals.",
      "Clues exist, but they need interpretation before they become useful.",
      "The goal is understanding, not just extraction."
    ],
    workflow: [
      "Collect the highest-signal evidence first.",
      "Map structure, dependencies, and surprising behavior.",
      "Separate confirmed observations from inference.",
      "Return the clearest explanation plus the next decisive check."
    ],
    deliverables: [
      "A concise explanation of what is going on.",
      "A short list of risks, unknowns, or anomalies.",
      "A recommended next move."
    ],
    guardrails: [
      "Do not overclaim certainty when the evidence is partial.",
      "Keep observation and interpretation visibly separate."
    ],
    short_description: "Inspect opaque systems and surface what matters",
    default_prompt: (slug) =>
      `Use $${slug} to inspect this situation, surface the highest-signal evidence, and tell me what matters next.`
  },
  translation: {
    reality_tier: "shipping-now",
    literalness: "metaphorical",
    include_openclaw: true,
    tagline: "Translate unfamiliar language, notation, or protocol into usable meaning.",
    description: "Use this skill when the words are visible but the real meaning is trapped inside a dialect, jargon set, or unfamiliar format.",
    when_to_use: [
      "A team, tool, or text uses language that blocks progress.",
      "You need interpretation, not just literal substitution.",
      "Technical nuance matters and cannot be flattened away."
    ],
    workflow: [
      "Identify the source language, jargon, or protocol.",
      "Translate the surface form into clear operational meaning.",
      "Preserve important technical distinctions.",
      "Return the translation with ambiguity called out explicitly."
    ],
    deliverables: [
      "A plain-language rendering of the source material.",
      "A glossary of the important terms of art.",
      "A note on ambiguity or missing context."
    ],
    guardrails: [
      "Do not erase technical nuance for the sake of simplicity.",
      "Flag ambiguity instead of guessing silently."
    ],
    short_description: "Translate unfamiliar language into usable meaning",
    default_prompt: (slug) =>
      `Use $${slug} to translate this language, jargon, or protocol into clear operational English.`
  },
  communication: {
    reality_tier: "shipping-now",
    literalness: "metaphorical",
    include_openclaw: true,
    tagline: "Move meaning across distance, context, or boundaries without losing intent.",
    description: "Use this skill when the core problem is transporting a message cleanly from one place, person, or system to another.",
    when_to_use: [
      "A message needs to cross time, distance, or context shifts.",
      "You need better signal transfer, not just more words.",
      "The receiver needs the right framing as well as the content."
    ],
    workflow: [
      "Clarify the sender, receiver, and intended effect.",
      "Compress the signal to what the receiver actually needs.",
      "Preserve intent and key constraints while removing noise.",
      "Return the message in the form most likely to survive the handoff."
    ],
    deliverables: [
      "A message or handoff artifact fit for the destination.",
      "A short note on what context was preserved or omitted.",
      "Any assumptions that the receiver will need."
    ],
    guardrails: [
      "Do not smuggle in claims the sender cannot support.",
      "Do not confuse compression with omission of critical constraints."
    ],
    short_description: "Move meaning cleanly across distance and context",
    default_prompt: (slug) =>
      `Use $${slug} to carry this message across contexts without losing the important meaning.`
  },
  manipulation: {
    reality_tier: "shipping-now",
    literalness: "hybrid",
    include_openclaw: true,
    tagline: "Move, edit, or actuate digital objects with precision and low blast radius.",
    description: "Use this skill when a small, exact manipulation is more valuable than a broad rewrite or a heavy-handed intervention.",
    when_to_use: [
      "You need a delicate change across files, records, or tools.",
      "A task is mostly about precision, not scale.",
      "The correct move is to touch the minimum viable surface."
    ],
    workflow: [
      "Identify the exact object or state that needs manipulation.",
      "Choose the smallest viable tool or action surface.",
      "Apply the change with a clear before-and-after description.",
      "Return the touched surfaces and the nearby constraints."
    ],
    deliverables: [
      "A minimal, targeted change or actuation plan.",
      "A short audit trail of what moved.",
      "A note on what was intentionally left untouched."
    ],
    guardrails: [
      "Avoid broad destructive actions when a narrow one will do.",
      "Preserve unrelated state and user work."
    ],
    short_description: "Manipulate digital objects with precise control",
    default_prompt: (slug) =>
      `Use $${slug} to make the smallest precise change that solves this problem and show exactly what moved.`
  },
  restoration: {
    reality_tier: "shipping-now",
    literalness: "metaphorical",
    include_openclaw: true,
    tagline: "Repair broken state and restore working order without losing critical context.",
    description: "Use this skill when the important thing is recovery, stabilization, or healing from damage, drift, or corruption.",
    when_to_use: [
      "A system, file, workflow, or plan is degraded or broken.",
      "You need recovery rather than net-new creation.",
      "The priority is getting back to a working state safely."
    ],
    workflow: [
      "Assess what is damaged, missing, or degraded.",
      "Choose the least risky path back to a stable state.",
      "Restore function while preserving useful context.",
      "Return the repaired state and any residual weakness."
    ],
    deliverables: [
      "A recovery or remediation plan.",
      "A restored artifact or state description.",
      "Residual risks and follow-up checks."
    ],
    guardrails: [
      "Do not overwrite healthy state while fixing damaged state.",
      "Be explicit about what could not be restored."
    ],
    short_description: "Repair broken state and restore working order",
    default_prompt: (slug) =>
      `Use $${slug} to repair this broken state, restore function, and tell me what is still fragile.`
  },
  mobility: {
    reality_tier: "shipping-now",
    literalness: "metaphorical",
    include_openclaw: true,
    tagline: "Move work, context, or systems across boundaries with minimal friction.",
    description: "Use this skill when the challenge is crossing distance, interfaces, or states cleanly and safely.",
    when_to_use: [
      "You need to route work across tools, teams, or environments.",
      "The problem is transition, handoff, or movement.",
      "You want the shortest safe path from here to there."
    ],
    workflow: [
      "Define the current position, the destination, and the constraints.",
      "Choose the lowest-friction viable route.",
      "Make the transition explicit and reversible where possible.",
      "Return the route, prerequisites, and boundary conditions."
    ],
    deliverables: [
      "A path or routing plan.",
      "A list of prerequisites and checkpoints.",
      "A note on transition risks."
    ],
    guardrails: [
      "Do not skip prerequisite states or access controls.",
      "Call out irreversible jumps before taking them."
    ],
    short_description: "Route work across boundaries with low friction",
    default_prompt: (slug) =>
      `Use $${slug} to figure out the cleanest route from the current state to the destination with clear constraints.`
  },
  simulation: {
    reality_tier: "shipping-now",
    literalness: "hybrid",
    include_openclaw: true,
    tagline: "Create convincing simulated scenes, states, or previews for reasoning and communication.",
    description: "Use this skill when the fastest way to understand or explain something is to construct a faithful simulation, mockup, or staged view.",
    when_to_use: [
      "A hypothetical state is easier to reason about than raw abstraction.",
      "You need a mockup, preview, or synthetic scene.",
      "Presentation matters, but truthfulness still matters more."
    ],
    workflow: [
      "Define which parts of reality need to be preserved in the simulation.",
      "Construct the minimum convincing model, mockup, or staged representation.",
      "Make the assumptions and simplifications explicit.",
      "Return the simulation plus what it should not be mistaken for."
    ],
    deliverables: [
      "A mockup, preview, or synthetic representation.",
      "A list of assumptions and simplifications.",
      "A note on where the model stops matching reality."
    ],
    guardrails: [
      "Do not present simulations as direct measurements or proofs.",
      "Make the boundary between representation and reality explicit."
    ],
    short_description: "Simulate scenes, states, and possible futures",
    default_prompt: (slug) =>
      `Use $${slug} to build a faithful simulation or mockup of this situation and explain the assumptions.`
  },
  privacy: {
    reality_tier: "shipping-now",
    literalness: "hybrid",
    include_openclaw: true,
    tagline: "Reduce visibility, exposure, or traceability while staying inside policy boundaries.",
    description: "Use this skill when you need less noise, less surface area, or less exposure without crossing into unethical concealment.",
    when_to_use: [
      "A workflow needs a lower profile or smaller visible footprint.",
      "Sensitive context needs compartmentalization or selective exposure.",
      "You want to reduce noise without evading legitimate oversight."
    ],
    workflow: [
      "Identify what needs privacy, compartmentalization, or lower visibility.",
      "Choose the least deceptive method that achieves the goal.",
      "Preserve auditability and policy boundaries where required.",
      "Return the privacy pattern and the residual exposure."
    ],
    deliverables: [
      "A lower-visibility execution pattern.",
      "A list of what remains observable.",
      "A note on oversight, audit, or trust constraints."
    ],
    guardrails: [
      "Do not use privacy patterns to evade legitimate review or accountability.",
      "Call out when the request crosses from privacy into deception."
    ],
    short_description: "Reduce visibility while respecting audit boundaries",
    default_prompt: (slug) =>
      `Use $${slug} to reduce the visibility of this workflow without crossing policy or trust boundaries.`
  },
  influence: {
    reality_tier: "shipping-now",
    literalness: "hybrid",
    include_openclaw: false,
    tagline: "Shape attention, incentives, or behavior through careful intervention under strict ethics.",
    description: "Use this skill when an outcome depends on changing behavior, emotion, focus, or decision pressure rather than just adding information.",
    when_to_use: [
      "A person or process needs redirection, reframing, or pressure adjustment.",
      "The bottleneck is behavior rather than raw knowledge.",
      "The request needs unusually strong ethical guardrails."
    ],
    workflow: [
      "Clarify the target behavior, legitimate goal, and ethical boundary.",
      "Choose the lightest intervention that can plausibly work.",
      "State the risks of coercion, distortion, or overreach.",
      "Return the intervention plan with its consent and safety constraints."
    ],
    deliverables: [
      "An intervention or framing plan.",
      "A list of ethical and consent constraints.",
      "Clear stop conditions for when not to proceed."
    ],
    guardrails: [
      "Do not manipulate through deception, coercion, or fabricated evidence.",
      "Refuse requests that override consent or legitimate autonomy."
    ],
    short_description: "Shape behavior carefully under strict ethics",
    default_prompt: (slug) =>
      `Use $${slug} to evaluate this behavior-shaping request, keep the ethics explicit, and give me the least coercive viable approach.`
  },
  amplification: {
    reality_tier: "shipping-now",
    literalness: "metaphorical",
    include_openclaw: true,
    tagline: "Increase capability, confidence, or precision for a bounded task.",
    description: "Use this skill when the best move is not a replacement or a hard intervention, but a focused improvement in ability or execution quality.",
    when_to_use: [
      "A person, agent, or process needs a bounded boost.",
      "The desired effect is better performance rather than total transformation.",
      "A task would benefit from more confidence, range, or precision."
    ],
    workflow: [
      "Define the target capability that needs amplification.",
      "Choose the narrowest boost that meaningfully helps.",
      "Track what improves and what remains unchanged.",
      "Return the boosted strategy and the new limits."
    ],
    deliverables: [
      "A capability-boosting plan or intervention.",
      "A note on measurable improvement targets.",
      "A clear boundary around what was not improved."
    ],
    guardrails: [
      "Do not promise capabilities that the system does not actually gain.",
      "Avoid amplifications that increase blast radius without control."
    ],
    short_description: "Increase capability, confidence, or precision",
    default_prompt: (slug) =>
      `Use $${slug} to improve this capability in a bounded way and tell me what actually gets better.`
  },
  warding: {
    reality_tier: "shipping-now",
    literalness: "literal",
    include_openclaw: true,
    tagline: "Define guards, boundaries, and protective triggers around valuable systems.",
    description: "Use this skill when the right move is to wrap something in explicit boundaries, protections, or alerting behavior.",
    when_to_use: [
      "A system or workflow needs a defensive boundary.",
      "You want a trigger, tripwire, or protection layer.",
      "Safety is improved by a well-defined guard rather than constant vigilance."
    ],
    workflow: [
      "Identify the protected asset and the boundary that matters.",
      "Choose the guard, trigger, or protective mechanism.",
      "Make escalation, ownership, and rollback explicit.",
      "Return the boundary design and its failure modes."
    ],
    deliverables: [
      "A concrete protection or guard design.",
      "Trigger conditions and response paths.",
      "A note on noise, blind spots, or bypass risk."
    ],
    guardrails: [
      "Do not create noisy defenses with no owner or response path.",
      "Do not claim coverage where significant blind spots remain."
    ],
    short_description: "Define boundaries, guards, and protective triggers",
    default_prompt: (slug) =>
      `Use $${slug} to design a protective boundary around this asset and make the trigger conditions explicit.`
  },
  containment: {
    reality_tier: "shipping-now",
    literalness: "literal",
    include_openclaw: false,
    tagline: "Constrain risky processes, actors, or effects inside hard boundaries.",
    description: "Use this skill when something needs to be paused, boxed in, or strongly limited to reduce harm or blast radius.",
    when_to_use: [
      "A process, behavior, or effect needs strict containment.",
      "The safest move is to stop spread rather than optimize flow.",
      "Risk is dominated by what happens if the thing keeps moving."
    ],
    workflow: [
      "Identify the thing being constrained and the reason for containment.",
      "Choose the smallest boundary that still meaningfully reduces risk.",
      "Define release conditions, owners, and escape paths.",
      "Return the containment plan and the tradeoffs it creates."
    ],
    deliverables: [
      "A boundary or quarantine design.",
      "Release criteria and operators.",
      "Known tradeoffs and residual risk."
    ],
    guardrails: [
      "Do not contain things indefinitely without a review path.",
      "Do not use containment language to justify abusive control."
    ],
    short_description: "Constrain risky processes inside hard boundaries",
    default_prompt: (slug) =>
      `Use $${slug} to design a hard boundary around this risky process and explain how it can be safely released.`
  },
  disruption: {
    reality_tier: "prototype",
    literalness: "literal",
    include_openclaw: false,
    tagline: "Trigger forceful effects only behind explicit safety gates and narrow scopes.",
    description: "Use this skill when the desired action is intentionally high-impact, loud, or disruptive and therefore needs strong control surfaces.",
    when_to_use: [
      "A strong effect or interruption is genuinely part of the plan.",
      "A visible or forceful action would change the state of the system quickly.",
      "The request needs hard boundaries, confirmations, and rollback planning."
    ],
    workflow: [
      "Identify the effect surface, target, and intended blast radius.",
      "Require explicit confirmation and a narrow execution scope.",
      "Design rollback, shutdown, or compensation paths where possible.",
      "Return the controlled action plan and its risks."
    ],
    deliverables: [
      "A tightly scoped high-impact action plan.",
      "Confirmation and rollback requirements.",
      "A list of the most dangerous failure modes."
    ],
    guardrails: [
      "Never improvise dangerous or irreversible real-world actions.",
      "Refuse requests that lack a clear safety envelope."
    ],
    short_description: "Trigger forceful effects behind safety controls",
    default_prompt: (slug) =>
      `Use $${slug} to design a tightly controlled high-impact action, but stop for hard safety checks before anything irreversible.`
  },
  transformation: {
    reality_tier: "shipping-now",
    literalness: "hybrid",
    include_openclaw: true,
    tagline: "Refactor identity, structure, or capabilities into a new operational form.",
    description: "Use this skill when the problem is not a small fix or a simple boost, but a meaningful change in form, role, or structure.",
    when_to_use: [
      "A system or artifact needs a meaningful change in shape or role.",
      "Incremental edits are not enough to meet the goal.",
      "The work needs a before-and-after transformation, not just optimization."
    ],
    workflow: [
      "Define the current form, target form, and invariant constraints.",
      "Plan the transformation in controlled stages.",
      "Track what changes identity and what must remain stable.",
      "Return the transformed design plus migration risks."
    ],
    deliverables: [
      "A transformation or refactor plan.",
      "A description of preserved invariants.",
      "Migration or rollback considerations."
    ],
    guardrails: [
      "Do not lose core invariants while changing the form.",
      "Be explicit when a transformation is effectively irreversible."
    ],
    short_description: "Refactor identity, structure, or capabilities",
    default_prompt: (slug) =>
      `Use $${slug} to transform this system into a new form while preserving the important invariants.`
  },
  nature: {
    reality_tier: "shipping-now",
    literalness: "metaphorical",
    include_openclaw: true,
    tagline: "Work with living systems, environments, and nonhuman signals rather than forcing them flat.",
    description: "Use this skill when the domain behaves more like an ecosystem than a deterministic machine and you need to act with that grain.",
    when_to_use: [
      "The system behaves like an environment, organism, or living network.",
      "Signals are indirect and need ecological rather than purely mechanical interpretation.",
      "The right move is cultivation, observation, or respectful interfacing."
    ],
    workflow: [
      "Map the living or environmental context first.",
      "Identify the real signals, cycles, or actors in play.",
      "Choose an intervention that works with the system rather than against it.",
      "Return the proposed interaction and its ecological tradeoffs."
    ],
    deliverables: [
      "A field-aware operating plan.",
      "A list of the key signals or actors involved.",
      "Risks of over-intervention or misread signals."
    ],
    guardrails: [
      "Do not flatten complex living systems into simplistic assumptions.",
      "Call out when observation is safer than intervention."
    ],
    short_description: "Work with living systems and environment signals",
    default_prompt: (slug) =>
      `Use $${slug} to interface with this living or environmental system in a way that respects its real signals.`
  },
  fieldwork: {
    reality_tier: "shipping-now",
    literalness: "metaphorical",
    include_openclaw: true,
    tagline: "Operate effectively in messy real-world contexts where conditions are not perfectly controlled.",
    description: "Use this skill when good work depends on situational judgment, embodied constraints, or practical navigation through imperfect terrain.",
    when_to_use: [
      "The environment is noisy, incomplete, or physically constrained.",
      "Success depends on practical judgment under uncertainty.",
      "A tidy abstract answer will miss the real operating conditions."
    ],
    workflow: [
      "Establish the terrain, actors, and practical constraints.",
      "Choose the approach that fits the actual conditions rather than the idealized version.",
      "Adapt the plan as new signals arrive from the field.",
      "Return the field-ready approach and its likely failure points."
    ],
    deliverables: [
      "A practical, context-aware plan.",
      "A list of assumptions most likely to fail in the field.",
      "Fallbacks for messy real conditions."
    ],
    guardrails: [
      "Do not confuse a neat plan with a field-ready plan.",
      "Make the real-world constraints explicit."
    ],
    short_description: "Operate effectively in messy real-world contexts",
    default_prompt: (slug) =>
      `Use $${slug} to adapt this plan to real-world conditions and tell me where it will actually break.`
  },
  rhetoric: {
    reality_tier: "shipping-now",
    literalness: "metaphorical",
    include_openclaw: true,
    tagline: "Move people with audience-aware language, tone, and framing.",
    description: "Use this skill when success depends on delivery, audience fit, and social context rather than raw correctness alone.",
    when_to_use: [
      "You need buy-in, clarity, or audience-aware framing.",
      "The work is partly persuasive, performative, or relational.",
      "A technically correct answer will fail without better delivery."
    ],
    workflow: [
      "Identify the audience, their incentives, and the decision threshold.",
      "Choose the tone and framing that best fit that audience.",
      "Build the message around concrete value and credible tradeoffs.",
      "Return the draft and the reasoning it relies on."
    ],
    deliverables: [
      "A tuned message or performance plan.",
      "Likely objections and how to address them.",
      "A note on which claims need evidence."
    ],
    guardrails: [
      "Do not use rhetoric to conceal weak evidence or false claims.",
      "Call out when the request crosses from persuasion into manipulation."
    ],
    short_description: "Move people with audience-aware language and tone",
    default_prompt: (slug) =>
      `Use $${slug} to tune this message for the target audience and make the case credibly.`
  },
  execution: {
    reality_tier: "shipping-now",
    literalness: "metaphorical",
    include_openclaw: true,
    tagline: "Perform precise actions under real constraints without wasting motion.",
    description: "Use this skill when performance depends on timing, coordination, dexterity, or disciplined execution rather than just planning.",
    when_to_use: [
      "The task rewards timing, coordination, or precision.",
      "A small execution mistake would matter.",
      "The work needs practical finesse, not just analysis."
    ],
    workflow: [
      "Break the task into the smallest decisive motions.",
      "Optimize for timing, stability, and wasted motion.",
      "Execute with clear checkpoints and recovery paths.",
      "Return the move set and the critical moments."
    ],
    deliverables: [
      "A precise execution plan.",
      "Key checkpoints and failure points.",
      "A short note on how to recover from small mistakes."
    ],
    guardrails: [
      "Do not overcomplicate a task that rewards clean fundamentals.",
      "Name the tight tolerances instead of hiding them."
    ],
    short_description: "Perform precise actions under real constraints",
    default_prompt: (slug) =>
      `Use $${slug} to break this into clean, precise moves and tell me where execution will be tight.`
  }
};

function slugify(name) {
  return name
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function addGroup(map, archetype, names) {
  for (const name of names) {
    if (map.has(name)) {
      throw new Error(`Duplicate archetype mapping for ${name}`);
    }
    map.set(name, archetype);
  }
}

function buildNameMap() {
  const map = new Map();

  addGroup(map, "execution", ["Acrobatics", "Athletics", "Sleight of Hand"]);
  addGroup(map, "fieldwork", ["Animal Handling", "Medicine", "Survival"]);
  addGroup(map, "analysis", [
    "Arcana",
    "Detect Magic",
    "Foresight",
    "History",
    "Identify",
    "Insight",
    "Investigation",
    "Nature",
    "Perception",
    "Religion"
  ]);
  addGroup(map, "rhetoric", ["Deception", "Intimidation", "Performance", "Persuasion"]);
  addGroup(map, "translation", ["Comprehend Languages", "Tongues"]);

  addGroup(map, "nature", [
    "Animal Friendship",
    "Awaken",
    "Locate Animals or Plants",
    "Plant Growth",
    "Speak with Animals",
    "Speak with Plants"
  ]);
  addGroup(map, "communication", [
    "Animal Messenger",
    "Dream",
    "Illusory Script",
    "Message",
    "Sending",
    "Speak with Dead",
    "Zone of Truth"
  ]);
  addGroup(map, "manipulation", [
    "Animate Objects",
    "Dancing Lights",
    "Knock",
    "Light",
    "Magic Mouth",
    "Mage Hand",
    "Mending",
    "Mordenkainen’s Sword",
    "Planar Binding",
    "Prestidigitation",
    "Unseen Servant"
  ]);
  addGroup(map, "influence", [
    "Bane",
    "Bestow Curse",
    "Calm Emotions",
    "Charm Person",
    "Compulsion",
    "Confusion",
    "Dominate Monster",
    "Dominate Person",
    "Enthrall",
    "Fear",
    "Geas",
    "Glibness",
    "Heroism",
    "Hold Monster",
    "Hold Person",
    "Hypnotic Pattern",
    "Otto’s Irresistible Dance",
    "Sleep",
    "Suggestion",
    "Mass Suggestion",
    "Modify Memory",
    "Vicious Mockery"
  ]);
  addGroup(map, "analysis", [
    "Clairvoyance",
    "Detect Thoughts",
    "Faerie Fire",
    "Find the Path",
    "Legend Lore",
    "Locate Creature",
    "Locate Object",
    "Scrying",
    "See Invisibility",
    "True Seeing"
  ]);
  addGroup(map, "restoration", [
    "Cure Wounds",
    "Greater Restoration",
    "Healing Word",
    "Lesser Restoration",
    "Mass Cure Wounds",
    "Raise Dead",
    "Regenerate",
    "Resurrection"
  ]);
  addGroup(map, "mobility", [
    "Dimension Door",
    "Etherealness",
    "Feather Fall",
    "Freedom of Movement",
    "Longstrider",
    "Teleport",
    "Teleportation Circle"
  ]);
  addGroup(map, "privacy", [
    "Disguise Self",
    "Greater Invisibility",
    "Invisibility",
    "Mind Blank",
    "Mislead",
    "Nondetection",
    "Seeming",
    "Silence",
    "Stealth"
  ]);
  addGroup(map, "simulation", [
    "Hallucinatory Terrain",
    "Major Image",
    "Mirage Arcane",
    "Minor Illusion",
    "Programmed Illusion",
    "Project Image",
    "Silent Image"
  ]);
  addGroup(map, "amplification", ["Enhance Ability", "True Strike"]);
  addGroup(map, "warding", ["Dispel Magic", "Glyph of Warding", "Guards and Wards", "Symbol"]);
  addGroup(map, "containment", ["Blindness/Deafness", "Forcecage"]);
  addGroup(map, "disruption", [
    "Eyebite",
    "Feeblemind",
    "Heat Metal",
    "Power Word Kill",
    "Power Word Stun",
    "Shatter",
    "Stinking Cloud",
    "Thunderwave"
  ]);
  addGroup(map, "transformation", ["Polymorph", "True Polymorph"]);

  return map;
}

const restrictedOpenClawNames = new Set([
  "Blindness/Deafness",
  "Bane",
  "Bestow Curse",
  "Charm Person",
  "Compulsion",
  "Confusion",
  "Deception",
  "Disguise Self",
  "Dominate Monster",
  "Dominate Person",
  "Eyebite",
  "Fear",
  "Feeblemind",
  "Forcecage",
  "Geas",
  "Glibness",
  "Hold Monster",
  "Hold Person",
  "Hypnotic Pattern",
  "Intimidation",
  "Mass Suggestion",
  "Mislead",
  "Modify Memory",
  "Otto’s Irresistible Dance",
  "Planar Binding",
  "Power Word Kill",
  "Power Word Stun",
  "Seeming",
  "Shatter",
  "Silence",
  "Sleep",
  "Stinking Cloud",
  "Suggestion",
  "Thunderwave",
  "True Polymorph",
  "Zone of Truth"
]);

const defaultRefusedHermesSlugs = [
  "compulsion",
  "dominate-monster",
  "dominate-person",
  "geas",
  "modify-memory"
];

const hermesCategoryDefinitions = [
  {
    slug: "investigation-and-preparation",
    title: "Investigation and Preparation",
    description:
      "Inspection, translation, verification, preflight, and context-loading skills for understanding a situation and setting up the next move before acting."
  },
  {
    slug: "actions-access-and-automation",
    title: "Actions, Access, and Automation",
    description:
      "Precise manipulation, access resolution, automation, migration, and interface-lift skills for changing systems with minimal blast radius."
  },
  {
    slug: "monitoring-and-protection",
    title: "Monitoring and Protection",
    description:
      "Observability, alerting, guards, and privacy controls that keep systems watchful without excess noise."
  },
  {
    slug: "messaging-and-coordination",
    title: "Messaging and Coordination",
    description:
      "Communication, briefings, scheduling, rhetoric, and audience-aware coordination across people, agents, and systems."
  },
  {
    slug: "repair-and-recovery",
    title: "Repair and Recovery",
    description:
      "Triage, repair, recovery, and stabilization for broken state, degraded systems, and fragile operating conditions."
  },
  {
    slug: "simulation-and-staging",
    title: "Simulation and Staging",
    description:
      "Mockups, staged environments, synthetic artifacts, and demo-ready representations for reasoning, testing, and rehearsal."
  },
  {
    slug: "influence-and-behavior",
    title: "Influence and Behavior",
    description:
      "Attention design, behavior shaping, and social intervention skills with strict ethical guardrails and consent requirements."
  },
  {
    slug: "containment-and-intervention",
    title: "Containment and Intervention",
    description:
      "Containment, capability reduction, throttling, and high-impact interventions that need explicit approval, narrow scope, and clear rollback."
  }
];

const hermesCategoryByArchetype = new Map([
  ["analysis", "investigation-and-preparation"],
  ["translation", "investigation-and-preparation"],
  ["amplification", "investigation-and-preparation"],
  ["execution", "actions-access-and-automation"],
  ["manipulation", "actions-access-and-automation"],
  ["mobility", "actions-access-and-automation"],
  ["transformation", "actions-access-and-automation"],
  ["warding", "monitoring-and-protection"],
  ["privacy", "monitoring-and-protection"],
  ["communication", "messaging-and-coordination"],
  ["rhetoric", "messaging-and-coordination"],
  ["restoration", "repair-and-recovery"],
  ["fieldwork", "repair-and-recovery"],
  ["simulation", "simulation-and-staging"],
  ["nature", "investigation-and-preparation"],
  ["containment", "containment-and-intervention"],
  ["disruption", "containment-and-intervention"],
  ["influence", "influence-and-behavior"]
]);

const hermesCategoryOverrides = new Map([
  ["attune", "investigation-and-preparation"],
  ["dancing-lights", "monitoring-and-protection"],
  ["deception", "simulation-and-staging"],
  ["animal-friendship", "actions-access-and-automation"],
  ["awaken", "actions-access-and-automation"],
  ["etherealness", "investigation-and-preparation"],
  ["feather-fall", "repair-and-recovery"],
  ["plant-growth", "influence-and-behavior"],
  ["light", "monitoring-and-protection"],
  ["magic-mouth", "messaging-and-coordination"],
  ["mending", "repair-and-recovery"],
  ["scrying", "monitoring-and-protection"],
  ["speak-with-animals", "monitoring-and-protection"],
  ["speak-with-dead", "investigation-and-preparation"],
  ["zone-of-truth", "investigation-and-preparation"]
]);

const defaultHermesDiscovery = {
  featured_entry_slugs: [
    "detect-magic",
    "identify",
    "comprehend-languages",
    "investigation",
    "mage-hand",
    "glyph-of-warding",
    "dream",
    "feather-fall"
  ],
  browse_paths: [
    {
      slug: "figure-out-what-youre-looking-at",
      title: "Figure out what you're looking at",
      description:
        "Start here when the repo, workflow, or system is unfamiliar and you need the real shape before you touch it.",
      category_slug: "investigation-and-preparation",
      entry_slugs: ["detect-magic", "identify", "investigation", "comprehend-languages"]
    },
    {
      slug: "change-the-system-without-a-battleaxe",
      title: "Change the system without a battleaxe",
      description:
        "Use this shelf when dexterity, careful edits, and bounded automation matter more than force.",
      category_slug: "actions-access-and-automation",
      entry_slugs: ["mage-hand", "sleight-of-hand", "unseen-servant", "awaken"]
    },
    {
      slug: "light-up-the-black-box",
      title: "Light up the black box",
      description:
        "Reach for these when you need lightweight observability, tripwires, or clearer signals before the room gets loud.",
      category_slug: "monitoring-and-protection",
      entry_slugs: ["dancing-lights", "light", "glyph-of-warding", "scrying"]
    },
    {
      slug: "get-the-right-message-to-the-right-place",
      title: "Get the right message to the right place",
      description:
        "These are the comms and coordination spells for briefings, triggers, routing, and asynchronous delivery.",
      category_slug: "messaging-and-coordination",
      entry_slugs: ["message", "sending", "dream", "magic-mouth"]
    },
    {
      slug: "stop-the-bleeding",
      title: "Stop the bleeding",
      description:
        "Open this shelf when something is already degraded and the next move is triage, repair, or graceful descent.",
      category_slug: "repair-and-recovery",
      entry_slugs: ["cure-wounds", "mending", "feather-fall", "animal-handling"]
    },
    {
      slug: "mock-it-before-you-ship-it",
      title: "Mock it before you ship it",
      description:
        "Use the staging shelf when the fastest path to clarity is a demo, rehearsal, simulation, or synthetic artifact.",
      category_slug: "simulation-and-staging",
      entry_slugs: ["minor-illusion", "major-image", "deception", "programmed-illusion"]
    },
    {
      slug: "handle-people-with-care",
      title: "Handle people with care",
      description:
        "These are the ethically sharp spells for de-escalation, morale, attention, and behavior with guardrails on.",
      category_slug: "influence-and-behavior",
      entry_slugs: ["calm-emotions", "heroism", "fear", "plant-growth"]
    },
    {
      slug: "box-in-blast-radius",
      title: "Box in blast radius",
      description:
        "Reach here when the job is containment, capability reduction, or an emergency stop under narrow control.",
      category_slug: "containment-and-intervention",
      entry_slugs: ["forcecage", "blindness-deafness", "feeblemind", "power-word-stun"]
    }
  ]
};

const providerOrder = ["openai", "claude", "openclaw", "hermes"];

function providerTargetsFor(entry, archetypeKey) {
  const archetype = archetypes[archetypeKey];
  const providers = ["openai", "claude"];

  if (
    archetype.include_openclaw &&
    archetype.reality_tier === "shipping-now" &&
    !restrictedOpenClawNames.has(entry.name)
  ) {
    providers.push("openclaw");
    providers.push("hermes");
  }

  return providers;
}

function normalizeProviderTargets(entry, refusedHermesSlugs) {
  const providers = new Set(entry.provider_targets);

  if (refusedHermesSlugs.has(entry.slug)) {
    providers.delete("hermes");
  } else if (providers.has("openclaw") || providers.has("hermes")) {
    providers.add("hermes");
  }

  return providerOrder.filter((provider) => providers.has(provider));
}

function hermesCategoryForEntry(entry, nameMap) {
  const override = hermesCategoryOverrides.get(entry.slug);
  if (override) {
    return override;
  }

  const archetype = nameMap.get(entry.name);
  const category = hermesCategoryByArchetype.get(archetype);

  if (!category) {
    throw new Error(`No Hermes category mapping for ${entry.name} (${entry.slug})`);
  }

  return category;
}

function normalizeHermesDiscovery(discovery, hermesEntries, categoryEntrySetBySlug) {
  const resolved = structuredClone(discovery ?? defaultHermesDiscovery);
  const hermesEntrySlugs = new Set(hermesEntries.map((entry) => entry.slug));

  if (!Array.isArray(resolved.featured_entry_slugs) || resolved.featured_entry_slugs.length === 0) {
    throw new Error("Hermes discovery must define featured_entry_slugs");
  }

  for (const slug of resolved.featured_entry_slugs) {
    if (!hermesEntrySlugs.has(slug)) {
      throw new Error(`Hermes discovery featured entry is not on the Hermes surface: ${slug}`);
    }
  }

  if (!Array.isArray(resolved.browse_paths) || resolved.browse_paths.length === 0) {
    throw new Error("Hermes discovery must define browse_paths");
  }

  const seenBrowsePathSlugs = new Set();
  const seenCategorySlugs = new Set();

  for (const browsePath of resolved.browse_paths) {
    if (seenBrowsePathSlugs.has(browsePath.slug)) {
      throw new Error(`Duplicate Hermes browse path slug: ${browsePath.slug}`);
    }
    seenBrowsePathSlugs.add(browsePath.slug);

    if (seenCategorySlugs.has(browsePath.category_slug)) {
      throw new Error(
        `Hermes browse paths must map one path per category; duplicate category ${browsePath.category_slug}`
      );
    }
    seenCategorySlugs.add(browsePath.category_slug);

    const categoryEntries = categoryEntrySetBySlug.get(browsePath.category_slug);
    if (!categoryEntries) {
      throw new Error(`Hermes browse path references unknown category: ${browsePath.category_slug}`);
    }

    if (!Array.isArray(browsePath.entry_slugs) || browsePath.entry_slugs.length === 0) {
      throw new Error(`Hermes browse path ${browsePath.slug} must define entry_slugs`);
    }

    for (const slug of browsePath.entry_slugs) {
      if (!hermesEntrySlugs.has(slug)) {
        throw new Error(`Hermes browse path entry is not on the Hermes surface: ${slug}`);
      }
      if (!categoryEntries.has(slug)) {
        throw new Error(
          `Hermes browse path ${browsePath.slug} includes ${slug}, which is not in ${browsePath.category_slug}`
        );
      }
    }
  }

  const missingCategoryCoverage = [...categoryEntrySetBySlug.keys()].filter(
    (categorySlug) => !seenCategorySlugs.has(categorySlug)
  );
  if (missingCategoryCoverage.length > 0) {
    throw new Error(
      `Hermes browse paths are missing categories: ${missingCategoryCoverage.join(", ")}`
    );
  }

  return resolved;
}

function buildHermesSurface(entries, nameMap, surfaceConfig = {}) {
  const hermesEntries = entries.filter((entry) => entry.provider_targets.includes("hermes"));
  const assigned = new Set();

  const categories = hermesCategoryDefinitions
    .map((definition) => {
      const entrySlugs = hermesEntries
        .filter((entry) => hermesCategoryForEntry(entry, nameMap) === definition.slug)
        .sort((left, right) => left.name.localeCompare(right.name))
        .map((entry) => {
          assigned.add(entry.slug);
          return entry.slug;
        });

      if (entrySlugs.length === 0) {
        return null;
      }

      return {
        slug: definition.slug,
        title: definition.title,
        description: definition.description,
        entry_slugs: entrySlugs
      };
    })
    .filter(Boolean);

  const categoryEntrySetBySlug = new Map(
    categories.map((category) => [category.slug, new Set(category.entry_slugs)])
  );
  const unassigned = hermesEntries.filter((entry) => !assigned.has(entry.slug));
  if (unassigned.length > 0) {
    throw new Error(
      `Hermes categories missing entries: ${unassigned.map((entry) => entry.slug).join(", ")}`
    );
  }

  return {
    release_surface: "public-low-risk",
    refused_entry_slugs: [...new Set(surfaceConfig.refused_entry_slugs ?? defaultRefusedHermesSlugs)].sort(),
    discovery: normalizeHermesDiscovery(
      surfaceConfig.discovery,
      hermesEntries,
      categoryEntrySetBySlug
    ),
    categories
  };
}

function openclawConfigFor(entry, providers) {
  if (!providers.includes("openclaw")) {
    return undefined;
  }

  return { user_invocable: true };
}

function buildStub(entry, archetypeKey) {
  const archetype = archetypes[archetypeKey];
  const providers = providerTargetsFor(entry, archetypeKey);
  const slug = entry.slug || slugify(entry.name);

  const blueprint = {
    slug,
    name: entry.name,
    kind: entry.kind,
    canonical_id: entry.id,
    provider_targets: providers,
    reality_tier: archetype.reality_tier,
    literalness: archetype.literalness,
    tagline: archetype.tagline,
    description: archetype.description,
    when_to_use: archetype.when_to_use,
    workflow: archetype.workflow,
    deliverables: archetype.deliverables,
    guardrails: archetype.guardrails,
    default_prompt: archetype.default_prompt(slug),
    openai: {
      short_description: archetype.short_description
    }
  };

  const openclaw = openclawConfigFor(entry, providers);
  if (openclaw) {
    blueprint.openclaw = openclaw;
  }

  return blueprint;
}

async function main() {
  const canon = JSON.parse(await readFile(canonPath, "utf8"));
  const blueprints = JSON.parse(await readFile(blueprintPath, "utf8"));
  const curatedById = new Map(blueprints.entries.map((entry) => [entry.canonical_id, entry]));
  const nameMap = buildNameMap();
  const refusedHermesSlugs = new Set(
    blueprints.surfaces?.hermes?.refused_entry_slugs ?? defaultRefusedHermesSlugs
  );

  const missingCanon = canon.entries.filter((entry) => !curatedById.has(entry.id));
  const unmapped = missingCanon.filter((entry) => !nameMap.has(entry.name));

  if (unmapped.length > 0) {
    throw new Error(
      `Missing archetype mappings for: ${unmapped.map((entry) => entry.name).join(", ")}`
    );
  }

  const generated = missingCanon.map((entry) => buildStub(entry, nameMap.get(entry.name)));
  const merged = [...blueprints.entries, ...generated]
    .map((entry) => ({
      ...entry,
      provider_targets: normalizeProviderTargets(entry, refusedHermesSlugs)
    }))
    .sort((left, right) => {
    if (left.kind !== right.kind) {
      return left.kind.localeCompare(right.kind);
    }
    return left.name.localeCompare(right.name);
  });

  const nextPayload = {
    schema_version: Math.max(blueprints.schema_version ?? 1, 3),
    surfaces: {
      hermes: buildHermesSurface(merged, nameMap, blueprints.surfaces?.hermes)
    },
    entries: merged
  };

  await writeFile(blueprintPath, `${JSON.stringify(nextPayload, null, 2)}\n`);

  console.log(
    `Expanded ${generated.length} missing canon entries into ${blueprintPath}; total entries: ${merged.length}`
  );
}

await main();
