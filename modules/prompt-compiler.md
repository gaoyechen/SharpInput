---
name: sharpinput-prompt-compiler
description: Use when SharpInput has enough intent and context to compile the user's weak input into a stronger copy-ready prompt.
---

# Prompt Compiler

Compile the upgraded prompt. This is the core transformation step.

## Inputs

- `target_input`
- `primary_intent`
- `secondary_intent`
- `scenario`
- `known_context`
- `missing_fields`
- `clarified_dimensions`
- `pressure_requirements`

## Must Include

- role or perspective
- task goal
- relevant context
- constraints
- judgment criteria
- output format
- explicit ban on vague answers
- **reasoning-before-conclusion** (推理先行): the compiled prompt MUST instruct the AI to show its reasoning process before delivering any conclusion, recommendation, or result. If the user's original input puts conclusions first, reverse the order. Exception: Level 0 quick factual lookups where reasoning adds no value.

## Structured Prompt Template

The compiled prompt should follow this structure internally. Not every section is mandatory — include what the task needs:

```text
[Task instruction — first line, no heading, concise and direct]

[Detailed context and constraints as needed.]

# Steps
[Ordered reasoning steps the AI should follow before producing the final output. For decision tasks, include: gather facts → identify assumptions → evaluate alternatives → recommend. For analysis tasks: define scope → examine evidence → synthesize → conclude.]

# Output Format
[Specify format explicitly: table, bullet list, JSON, code block, essay, etc. Include length guidance and structural requirements.]

# Examples
[1-3 concrete examples when the task benefits from demonstration. Use [placeholders] for variable parts. Mark input/output boundaries clearly.]

# Notes
[Boundary conditions, edge cases, things the AI must NOT do, and any special handling rules.]
```

### Template Rules

- **Reasoning steps go before output format** — the AI must think before it formats.
- For **decision/comparison/analysis** prompts, `# Steps` is mandatory and must end with a synthesis/conclusion step.
- For **generation/creation** prompts, `# Steps` is optional but `# Output Format` and `# Examples` are recommended.
- For **quick factual** prompts (Level 0), the full template is overkill — a direct instruction with output format is sufficient.
- Use `# Notes` to ban generic answers, enforce constraints, and handle edge cases.
- Do NOT wrap the entire prompt in code blocks — keep it as natural prose with section headers.

## Output

```json
{
  "compiled_prompt_draft": "",
  "missing_placeholders": [],
  "compile_notes": []
}
```

## Rules

- Do not answer the underlying task.
- Use placeholders for missing but non-blocking fields.
- Make the prompt directly copyable.
- Avoid generic phrases such as "根据我的需求" unless the needs are specified.
- For decision prompts, force a recommendation and trade-off.
- For generation prompts, specify audience, output format, and acceptance criteria.
- **Reasoning-first enforcement**: If the task requires analysis, judgment, or comparison, the compiled prompt MUST include explicit reasoning steps (e.g., "先分析…再比较…最后给出结论"). Never let the AI jump straight to a conclusion.
- **Structured template compliance**: For Level 1+ prompts, use the Structured Prompt Template above. At minimum include `# Steps` (for reasoning) and `# Output Format`. Add `# Examples` and `# Notes` when they materially improve prompt quality.
