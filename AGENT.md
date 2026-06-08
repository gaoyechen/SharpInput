# SharpInput Agent

SharpInput Agent is the orchestration layer for the SharpInput skill system.

It decides whether SharpInput should trigger, normalizes input, routes to capability modules, preserves intent fidelity, scores prompt quality, and renders the final upgraded prompt.

## Core Principle

Agent manages flow. Modules manage capabilities.

The agent should never become a second monolithic skill. It should route to focused files only when needed.

## Flow

```text
user weak input
-> trigger decision
-> input normalization
-> gate level
-> intent detection
-> scenario detection
-> scenario slot elicitation or context completion
-> route selection
-> prompt compilation
-> pressure strategy when needed
-> intent fidelity check
-> quality scoring
-> judge review when needed
-> output rendering
-> feedback/self-learning
```

## Trigger Decision

Trigger when the user asks to improve the input, prompt, question, requirement, idea, plan, or message.

Do not trigger when the user asks for direct answering, coding, data analysis, file edits, or factual lookup.

Mixed intent rule:

```text
If the user both asks for a better prompt and seems to want the answer, ask:
"你是想让我直接回答这个问题，还是把它改成一个更好的 AI 提问？"
```

## Input Normalization

Extract:

- `raw_input`: full user message
- `target_input`: the part to optimize
- `user_instruction`: how the user wants it optimized
- `task_mode`: `prompt_optimization` unless user asks direct execution
- `ambiguity_level`: low, medium, high

Example:

```json
{
  "raw_input": "帮我优化一下这个问题：我想买电脑，应该怎么问 AI？",
  "target_input": "我想买电脑",
  "user_instruction": "优化成更好的 AI 提问",
  "task_mode": "prompt_optimization",
  "ambiguity_level": "low"
}
```

## Route Map

| Path | Use When | Modules |
|------|----------|---------|
| Quick Rewrite | Level 0/1, simple optimization | intent-detection -> prompt-compiler -> output-renderer |
| Clarify First | vague subjective input | intent-detection -> scenario-detection -> scenario-slot-elicitation -> description-clarifier -> prompt-compiler -> output-renderer |
| Pressure Prompt | needs stance/trade-off/comparison | intent-detection -> context-completion -> prompt-compiler -> pressure-strategy -> output-renderer |
| Judge Mode | high risk, Level 3, multi-path, review requested | intent-detection -> scenario-detection -> context-completion -> prompt-compiler -> pressure-strategy -> judge-review -> output-renderer |

## Handoff Discipline

Every module reads and updates the handoff object in `references/handoff-contract.md`.

Never pass only prose between modules when structured fields exist. Natural language handoff loses context and causes rule drift.

## Feedback Loop

| User Feedback | Return To |
|--------------|-----------|
| "偏了" | intent-detection |
| "没问到关键点" | scenario-slot-elicitation |
| "不够具体" | context-completion |
| "太普通" | pressure-strategy |
| "太复杂" | gate level downgrade |
| "太强硬" | pressure-strategy with lower pressure |
| "不是这个场景" | scenario-detection |
| "可以直接用" | self-learning |

## Final Acceptance

The agent succeeds only if the final response includes a complete upgraded prompt and does not directly solve the user's original task.
