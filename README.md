# SharpInput

SharpInput is an AI input compiler. It upgrades weak, vague, subjective, or under-constrained user input into a copy-ready prompt that another AI can answer with more precision.

It does not directly solve the user's underlying task by default. Its job is to improve the input.

## What Changed

This version refactors SharpInput from a single heavy skill into an Agent-oriented system:

- `SKILL.md`: compact trigger and runtime checklist
- `AGENT.md`: orchestration flow, routing, and handoff discipline
- `skills/*/SKILL.md`: focused capability modules
- `references/*.md`: taxonomies, slot templates, rubrics, and output templates
- `examples/` and `tests/`: regression examples and quality checks
- `archive/SharpInput-v2.4.md`: archived monolithic version

## Core Principle

Agent manages flow. Skills manage capabilities.

SharpInput should route to focused modules only when needed. It should not become another monolithic prompt.

## Runtime Flow

```text
Trigger check
-> Input normalization
-> Gate Level 0-3
-> Intent detection
-> Scenario detection
-> Scenario slot elicitation or context completion
-> Route selection
-> Prompt compilation
-> Intent fidelity check
-> Prompt quality scoring
-> Optional Judge review
-> Output rendering
```

## When To Use

Use SharpInput when the user asks to improve the input itself:

- "帮我优化这个 prompt"
- "这个问题怎么问 AI 更好"
- "帮我润色/理清/改一下"
- "这样问行不行"
- "把这个需求改成一个更好的 AI 提问"

Do not use SharpInput when the user wants direct execution:

- coding or file edits
- factual lookup
- data analysis
- product recommendation answer
- direct debugging

If intent is mixed, clarify whether the user wants the answer or an upgraded prompt.

## Levels

| Level | Use When | Route |
|---|---|---|
| Level 0 | very small or quick rewrite | Quick Rewrite |
| Level 1 | clear intent, wording/structure improvement | Quick Rewrite or Clarify First |
| Level 2 | decision, comparison, optimization, trade-off | Pressure Prompt |
| Level 3 | high-risk, multi-path, strategy, requested review | Judge Mode |

## Key Concepts

### Intent Fidelity

The upgraded prompt must preserve the user's original goal. Do not add a conclusion, stance, or scenario the user did not provide.

### Scenario Slots

Known scenarios such as computer purchase, AI subscription choice, PRD generation, UI review, frontend demo generation, and learning plans use scenario-specific slots before generic questions.

### Default-Answer Stress Test

SharpInput may add pressure when generic answers would be weak. This is not forced contrarian behavior. The goal is to make the next AI explain trade-offs, failure conditions, and concrete next steps.

### Judge Review

Judge is reserved for Level 3, high-risk decisions, multi-path prompts, or explicit review requests. It checks intent fidelity, scenario fit, missing slots, pressure fit, and copy readiness.

## Project Structure

```text
SharpInput/
├── SKILL.md
├── AGENT.md
├── archive/
│   └── SharpInput-v2.4.md
├── skills/
│   ├── intent-detection/
│   ├── scenario-detection/
│   ├── scenario-slot-elicitation/
│   ├── context-completion/
│   ├── description-clarifier/
│   ├── prompt-compiler/
│   ├── pressure-strategy/
│   ├── judge-review/
│   └── output-renderer/
├── references/
│   ├── intent-taxonomy.md
│   ├── scenario-slot-templates.md
│   ├── prompt-patterns.md
│   ├── pressure-strategies.md
│   ├── output-templates.md
│   ├── judge-rubric.md
│   └── handoff-contract.md
├── examples/
└── tests/
```

## Quality Checks

Use `tests/regression-cases.md` after structural changes.

The final output must:

- identify Level, intent, scenario, and context status
- explain why the original input is weak
- include one complete upgraded prompt
- state what was added
- include a trade-off or risk note
- avoid directly solving the underlying task

## License

MIT
