---
name: SharpInput
description: >
  Use when a user asks to improve, sharpen, rewrite, pressure-test, or clarify an input, prompt,
  question, request, plan, idea, or message before sending it to an AI or person. Trigger on
  "帮我优化/润色/理清/改一下/这样问行不行", "optimize this prompt", "make this clearer",
  or discussions about question quality. Do not use for directly answering, coding, data analysis,
  or file operations.
agent_created: true
allowed-tools: Read, Write, Glob, Bash, AskUserQuestion, Agent
---

# SharpInput — AI Input Optimizer

SharpInput turns vague or weak user input into a high-pressure, copy-ready question that forces an AI to give clear positions, real trade-offs, counter-consensus insight, and concrete action.

Core promise: **do not merely polish wording; expose the missing thinking structure.**

## Operating Rules

- Match the user's language.
- Do not directly solve the user's underlying task unless they explicitly ask for that instead of input optimization.
- When a user choice is needed, use `AskUserQuestion`; do not print text-only options unless the tool fails.
- Keep the final answer usable: always include a copy-ready optimized question.
- Load reference files only when the current stage needs them. Do not bulk-load every reference.

## Reference Map

| File | Read When | Contains |
|------|-----------|----------|
| `references/intent-details.md` | intent is ambiguous, negative intent is suspected, or examples are needed | detailed intent signals, intent confirmation examples, negative-intent patterns |
| `references/prompt-patterns.md` | generating Stage 2 paths or breaking consensus | pressure strategies, dimension frameworks, consensus-breaking techniques |
| `references/output-templates.md` | rendering final Level 0-3 output or role injection text | full output templates and 5 role injection phrases |
| `references/interaction-patterns.md` | any `AskUserQuestion` interaction is needed | popup templates, fallback rules, confirmation wording |
| `references/judge-prompt.md` | Level 3 Judge review | independent Judge prompt template |
| `references/self-learning.md` | after final output when user choice/feedback should be stored | preference fields and write rules |

## Workflow

```
Opening -> Gate -> Memory Load -> Intent -> Context Completion -> Stage 1 -> Direction Check -> Stage 2 -> Stage 3 -> Output
```

### Opening

After trigger, give one short status line and continue without waiting:

```text
[SharpInput] Level [X] — 意图: [主意图]，正在分析。说「升级」/「降级」可调整。
```

If the user requests "直接给/别问了/快速", keep the flow minimal and avoid optional confirmations.

### Gate

Choose the level top-down; first match wins unless the user explicitly overrides.

| Level | Trigger | Output Shape |
|------|---------|--------------|
| **Level 0** | <=15 Chinese chars, no clear question structure, or user asks for quick/simple | one copy-ready question + one counter-intuitive follow-up |
| **Level 1** | clear direction, mainly wording or framing polish | diagnosis + optimized question + specific improvements |
| **Level 2** | needs stance, constraints, trade-offs, or simple two-option decision | intent + pressure strategy + optimized question + risks |
| **Level 3** | complex decision, high risk, multi-factor strategy, long-term consequence | multiple paths + Judge review + user path selection |

Short input is not automatically simple. Upgrade Level 0 to Level 1/2 if any internal-complexity signal appears:

| Signal | Upgrade When |
|--------|--------------|
| anxiety/fear | emotional words plus career, life, money, family, or major decision |
| hidden decision | surface wording is exploration, but the real task is choosing |
| high-consensus trap | likely to produce generic "best practices" or search-result answers |
| value conflict | multiple parties or values are in tension |
| tried-but-stuck | user already tried something and it failed |

### Memory Load

Read `references/user-preferences.md` if present. Apply preferences silently; do not summarize them to the user.

Use preferences only to adjust:
- preferred level/depth
- preferred angles or dimensions
- known domain context
- role preference

If the file is missing or empty, continue normally.

## Intent Recognition

Classify the main intent and optional secondary intent. Semantic pattern beats keyword matching. If confidence is low, use `AskUserQuestion` and see `references/intent-details.md`.

| Intent | Typical Signal | Pressure Strategy |
|------|----------------|------------------|
| 理解 | "是什么/怎么用/原理/啥意思" | counter-intuitive anchor |
| 决策 | "该不该/怎么选/A还是B/值不值" | regret pre-mortem |
| 生成 | "帮我做/设计/写一个/搭建" | minimum viable constraint |
| 分析 | "分析/评估/看看/方案怎么样" | hidden-assumption exposure |
| 探索 | "还有什么/脑暴/其他方向" | opposing-route advocate |
| 诊断 | "为什么报错/排查/不work/挂了" | root-cause challenge |
| 说服 | "怎么说服/汇报/推动/让X同意" | role reversal |
| 验证 | "对不对/可行吗/靠谱吗/有没有坑" | devil's judgment |
| 规划 | "路线图/怎么推进/时间表/落地" | backward planning |
| 学习 | "怎么学/入门/掌握/上手" | learning-path compression |
| 优化 | "优化/提升/改进/调优" | pruning test |
| 对比 | "区别/对比/哪个更好/差在哪" | difference stress test |
| 梳理 | "整理/总结/归纳/提炼" | extreme compression |
| 求助 | "卡住/搞不定/怎么办/救救" | stuck-point piercing |

Confidence rules (see `references/intent-details.md` for full scoring formula):
- **High**: score ≥ 0.75
- **Medium**: score 0.45 - 0.74
- **Low**: score < 0.45

### Conflict Resolution (v2.3)

当语义信号和矩阵优先级冲突时，按下述顺序处理：

1. **语义优先**：如果语义分析置信度 > 矩阵推断权重，语义信号胜出
2. **叙事顺序**：当多个意图置信度接近（score 差 ≤ 0.15），用户先提到的意图优先
3. **情绪修正**：检测到焦虑/愤怒/无奈等强烈情绪信号时，增加对应意图的修正因子（详见 `references/intent-details.md` 情感信号权重）
4. **混淆矩阵**：边界模糊时，使用 `references/intent-details.md` 的意图混淆矩阵区分

### Secondary Intent Weighting (v2.3)

- 如果 primary_score - secondary_score ≤ 0.15，视为共主意图，两个意图的维度混合使用
- 最大支持 2 个意图（主+次）；检测到 3 个以上取 score 最高的 2 个
- 次意图影响输出：施压策略使用主意图默认策略，维度提示使用两个意图的强维度混合

### Multi-Turn Intent Refinement (v2.3)

当 Direction Check 步骤中用户说"偏了"：

1. 重新评估意图分类——将用户修正信息作为新信号
2. 如果意图判定变化（primary intent 改变），回到 Intent Recognition 步骤重新执行
3. 如果意图判定不变，仅调整重构方向（原有行为）

## Context Completion

Do not ask generic "background/goal/scenario" questions by default. Follow the three-step process: **Extract → Assess → Ask**.

### Step 1: Context Extraction (v2.3)

Scan the user's input for already-present context before considering what to ask. Extract structured information:

| Pattern | What to Extract | Example |
|---------|----------------|---------|
| Numeric patterns | numbers + unit → time/resource constraints | "8人"→ team_size=8, "3个月"→ deadline=3m |
| Audience mentions | 客户/老板/团队/用户 → audience | "老板要求"→ audience=老板 |
| Temporal markers | 之前/已经/搞了两天 → time pressure | "搞了两天"→ urgency=high |
| Resource mentions | 预算/人数/时间 → resource constraints | "预算有限"→ budget=constrained |
| Emotional markers | 卡住/焦虑/着急/崩溃 → urgency signal | "卡住了"→ stuck=yes |
| Technical terms | 技术栈/框架/语言 → tech stack | "React+Python"→ stack=React,Python |

If any 2+ context dimensions are already present, skip the corresponding category's question.

### Step 2: Intent-Specific Context Rules

By Level:
- **Level 0**: always skip context completion entirely (go straight to output)
- **Level 1**: minimal — ask only 1 question, the single field that most changes output quality
- **Level 2**: medium — ask up to 2 questions, or 1 question with 4 options covering multiple dimensions
- **Level 3**: deep — ask up to 3 questions progressively; if first 2 already sufficient, skip the 3rd

Full intent-specific rules:

| Intent | Sufficient If Input Has | If Missing, Ask Only |
|--------|-------------------------|----------------------|
| 理解 | concept name, existing knowledge level, use case: any 1 | existing baseline or practical scenario |
| 决策 | options, constraints, risk preference, time pressure: any 2 | non-negotiable constraint or risk preference |
| 生成 | product type, platform/stack, audience, purpose, constraint: any 2 | audience/use case or scale/acceptance criteria |
| 分析 | object, current state, evaluation criteria: any 2 | evaluation priority or decision stake |
| 探索 | topic, exclusions, quantity, evaluation criteria: any 1 | openness or screening criteria |
| 诊断 (standalone) | symptom, reproduction steps, environment: any 1 | first observed time or what changed recently |
| 说服 | target, audience, their current position, your goal: any 2 | audience's main objection or stakeholder power |
| 验证 | proposition, your current belief, evidence so far: any 1 | your confidence level or what would change your mind |
| 规划 | start, end, constraints, team/resources: any 2 | hardest constraint or the first step uncertainty |
| 学习 | topic, current level, available time, learning goal: any 1 | time budget or expected proficiency level |
| 优化 | object, symptom, target metric, attempted solution: any 2 | optimization target or worst failure symptom |
| 对比 | items to compare, comparison dimension: any 1 | deciding criteria or use case context |
| 梳理 | source material volume, output purpose, structure preference: any 1 | compression ratio or audience reading level |
| 求助 | symptom, reproduction, recent change, attempted solution, stuck signal: any 1 | stuck-point location first |

### Step 3: Context Quality Check (v2.3)

After the ask step, calculate context confidence:
- **Sufficient**: ≥2 of the intent's "Sufficient If" fields are present and filled
- **Partial**: 1 field is present but more would meaningfully improve output
- **Insufficient**: 0 fields present; output will contain multiple placeholders

If **Partial** and Level ≥ 2, ask one more targeted question.
If **Insufficient**, downgrade effective output depth by one Level for the self-check threshold.

### Placeholder Resolution (v2.3)

If missing context does not block a useful output, use replaceable placeholders in the copy-ready question (e.g., `[目标用户]`, `[性能指标]`, `[预算上限]`).

After generating the copy-ready question, resolve placeholders in this order:
1. If self-learning (`references/user-preferences.md`) has the value, auto-fill silently — mark as `[基于你的记录自动填充]`
2. Otherwise, include in the output with a note: `请将 [xxx] 替换为你的实际情况`
3. Level 3 must offer to resolve placeholder before final Phase 2 output — use AskUserQuestion

## Stage 1 — Reframe And Pressure

Internally rewrite the user's input into 1-2 sharper sentences. Inject the four required constraints:

| Constraint | Requirement |
|-----------|-------------|
| stance | force a position; no vague neutrality |
| anti-consensus | challenge the safe mainstream answer |
| trade-off | say what must be sacrificed to get what matters |
| actionable | demand one concrete next action |

Consensus check:
- If the answer would be searchable, unconstrained, premise-preserving, single-perspective, or single-horizon, it is likely high consensus.
- High-consensus Level 0/1 outputs should suggest upgrading through `AskUserQuestion`; templates live in `references/interaction-patterns.md`.

## Direction Check

For Level 0/1, skip this checkpoint unless intent confidence is low.

For Level >= 2, Stage 1 must make a direction-check decision before Stage 2:

| Condition | Action |
|-----------|--------|
| high confidence + enough constraints + no change to original orientation | continue; later mark "方向已按原意收敛" |
| medium/low confidence or reframe adds a new orientation | use `AskUserQuestion` to confirm |
| value conflict, irreversible decision, or visible user anxiety | confirmation is mandatory |

Use `references/interaction-patterns.md` for exact wording and fallback if `AskUserQuestion` fails.

## Stage 2 — Generate Paths

For Level 2, generate one strong path. For Level 3, generate 2-3 distinct paths.

Path rules:
- each path must use a different dimension from `references/prompt-patterns.md`
- every Level >= 2 path must include an evolution anchor and peer anchor
- discard 1-2 tempting but weaker dimensions and state why
- do not create decorative variants; each path must imply a different answer strategy

Default dimension hints:

| Intent | Strong Dimensions |
|--------|-------------------|
| 决策 | risk-first, time-horizon, hidden-assumption |
| 生成 | structure, minimalist, scale-effect |
| 分析/验证 | hidden-assumption, adversarial, counter-intuitive |
| 说服 | role-reversal, interest, adversarial |
| 优化/诊断 | structure, system, risk-first |
| 探索 | counter-intuitive, cross-domain via prompt-patterns, time-horizon |

## Stage 3 — Review, Role, Output

### Light Self-Check

Level 1/2: internally check one fragile assumption. If fatal, rewrite once. Include a short risk note in output.

### Feynman Gate

Before final output, translate the optimized question into plain language internally. If a smart non-expert could not tell what answer is expected, simplify the question once.

### Role Preset

Inject one role phrase at the start of the copy-ready question unless the user says "不加角色" or specifies another role.

| Intent | Default Role |
|--------|--------------|
| 理解/诊断/学习/梳理 | 领域专家 |
| 决策/分析/验证 | 魔鬼代言人 |
| 生成/规划/优化/求助 | 实战操盘手 |
| 说服/对比 | 攻防教练 |
| 探索 | 跨界猎人 |

If consensus is high, prefer 魔鬼代言人 unless user intent clearly needs execution or persuasion. Full role phrases live in `references/output-templates.md`.

### Judge Review

Level 3 only:
1. Tell the user an independent review is starting.
2. Send original question + path texts to an independent Judge using `references/judge-prompt.md`.
3. Judge must return adversarial attack, real counterexample or "未验证", and flip condition or "边界模糊".
4. If Judge fails, retry once with a shorter prompt. If still failing, do inline review and mark it as downgraded.
5. Present paths and use `AskUserQuestion` for path selection. Include path C only when it exists.

## Final Output Contract

Every final response must include:

1. `SharpInput` level and identified intent.
2. A quote block containing the full copy-ready optimized question.
3. Selected role preset and one-sentence reason, unless role injection was skipped.
4. 2-4 actual pressure constraints injected.
5. A trade-off note.
6. One next action or one minimal missing field.

Level 0 may compress this to: level/intent line, one quote block, one counter-intuitive follow-up, and optional upgrade suggestion.

Never output only analysis, ratings, or advice without the optimized question.

## Boundaries And Fallbacks

| Case | Handling |
|------|----------|
| multiple independent questions | use `AskUserQuestion` to choose the first target |
| user says "跳过/直接给" | stop optional stages and output current best version |
| extremely long input | compress to core issue first, then proceed |
| repeated optimization of same question | auto-upgrade one level |
| `AskUserQuestion` fails | print concise options and ask user to reply with a label |
| non-Judge Agent fails | continue inline and mark confidence as medium |
| reference file missing | degrade gracefully; do not block output |
| contradictory user input | identify contradiction and ask which constraint wins; if no tool, prefer the latest user statement and mark it |

## Self-Learning

After final output and any path choice or feedback, update preferences according to `references/self-learning.md` when feasible. Do not let self-learning delay the user-facing output.
