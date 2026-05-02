# Output Templates

Output templates for all SharpInput forcing levels. Read this file when rendering output.

---

## Adaptive Output Rules

Templates below are the **default** format. Apply these adaptive rules:

**Level display (mandatory)**: Every output must start with the current Level on its own line: `[Level 0]` / `[Level 1]` / `[Level 2]` / `[Level 3]`. This lets the user know which level they're at and whether to upgrade.

**Summary mode (Level 3 default)**: Level 3 output is long. By default, render a **compact version**:
- Show: Level → Intent Recognition → Multi-Path table → Selection Prompt
- Collapse Adversarial Report into one-line credibility+key-risk per path
- Collapse Dimensions into a single combined list
- User can say "expand" or "full report" to see full adversarial analysis before selecting

**Progressive disclosure (all levels)**: If the user says "stop" or "just give me the question" at any stage, skip remaining stages and output whatever is ready.

**Language adaptation**: Output template placeholders should follow the user's language. If the user writes in Chinese, use Chinese placeholders; if in English, use English.

**Focus mode**: If the user specifies a focus (e.g., "only show me the adversarial part" or "skip the diagnosis"), output only the requested sections.

---

## Level 0 Output (Rapid Forcing)

```
[Level 0]

> [Optimized question with base four constraints injected (stance + anti-consensus + trade-off + actionability), ready to copy-paste]

Consensus Level: [low/medium/high]
说「升级」可进入 Level 1~3。
```

---

## Level 1 Output (Light Optimization)

```
[Level 1]

诊断: [1-2 sentences: core intent + main flaw]

优化后:
> [Optimized question text, ready to copy-paste]

改进点: [What specifically changed]
说「升级」可进入 Level 2/3。
```

---

## Level 2 Output (Medium Forcing)

```
[Level 2]

意图: [Explain/Decision/Generate/Analyze/Explore]（如有次意图也列出）
施压策略: [primary strategy] + [secondary supplement]

诊断: [2-3 sentences: core intent + main flaw + what mediocre answer you'd likely get]

优化后:
> [Optimized question with base four constraints + deep forcing layer, ready to copy-paste]

施压详情:
- 立场约束: [what stance was forced]
- 反共识约束: [what mainstream view to challenge]
- 权衡约束: [what to sacrifice for what]
- 可执行约束: [what concrete first step is required]
- 深度施压: [which additional dimension was injected]

共识度: [low/medium/high]

被忽略的维度:
1. [Dimension]: [why it matters]
2. [Dimension]: [why it matters]

一句话警告: [biggest pitfall without optimization]
说「升级」可进入 Level 3。
```

---

## Level 3 Output (Deep Adversarial)

Level 3 has three output phases: **Phase 1** (Analysis) is shown automatically, **Phase 2** (Selection Prompt) follows immediately, and **Phase 3** (Final Output) is shown after the user selects or combines a path.

### Phase 1: Analysis

```
[Level 3]

意图: [Explain/Decision/Generate/Analyze/Explore]（如有次意图也列出）
施压策略: [primary strategy] + [secondary supplement]

诊断: [2-3 sentences: core intent + main flaw + what mediocre answer you'd likely get]

路径对比:
| 路径 | 角度 | 方案概述 | 共识度 | 可信度 |
|------|------|---------|--------|--------|
| A | [angle tag] | [one-sentence] | [low/med/high] | 高 |
| B | [angle tag] | [one-sentence] | [low/med/high] | 中高 |
| C | [angle tag] | [one-sentence] | [low/med/high] | 中 |

每条路径的优化问题已包含全部施压约束（立场、反共识、权衡、可执行、深度施压）。

被忽略的维度:
1. [Dimension]: [why it matters]
2. [Dimension]: [why it matters]
```

**Summary mode**: Collapse the adversarial report below into one-line per path (credibility + key risk). User can say "expand" to see full details.

```
对抗审查（展开模式）:

路径 A:
| 假设 | 脆弱度 | 说明 |
|------|--------|------|
| [Assumption] | [high/med/low] | [why] |
最弱假设: [what] — [impact if overturned]
反例: [counter-example]
失效条件: 环境 [X] / 规模 [X] / 时间 [X]

路径 B: [同上]
路径 C: [同上]
```

### Phase 2: Selection Prompt

Use the **AskUserQuestion** tool to present clickable path options. Generate one option per path from the multi-path table, with the highest-credibility path listed first. Include a "Combine" option for custom combinations.

**AskUserQuestion parameters:**
- `question`: "选择一条路径，我会输出最终打磨好的问题"
- `header`: "选择路径"
- `options`: One per path (label = "Letter — angle tag", description = one-line summary + credibility)
- Last option: label "组合", description "混搭多条路径元素，选择 Other 描述你想要的组合"

**Fallback (if tool unavailable):**
```
选择一条路径，我会输出最终打磨好的问题:

A — [one-line summary]
B — [one-line summary]
C — [one-line summary]
组合 — 如"A的角度 + B的约束"（最多 3 条）

如果犹豫: 路径 [X] 可信度最高，适用范围最广。
```

### Phase 3: Final Output (after user selection)

```
已选择: [Path X / Combination description]

优化后的问题:
> [Full polished question — clean, ready to copy-paste into any AI]

施压约束:
- [Stance Constraint]
- [Anti-Consensus Constraint]
- [Trade-off Constraint]
- [Actionability Constraint]

适用边界: [under what conditions this works best]
风险提示: [top risk]
如果回答方向不对，追问: "[follow-up question]"

优化质量: 清晰度 [0-2]/2 | 具体性 [0-2]/2 | 完整性 [0-2]/2 | 可执行性 [0-2]/2 | 鲁棒性 [0-2]/2
```

Self-learning note: After outputting the final question, silently record user preference data and append optional feedback line:

```
拿到回答后，如果方向不对回复「方向偏了」；如果很好回复「很好」。
```
