# Output Templates

Output templates for all SharpInput forcing levels. Read this file before rendering output.

>  **GOLDEN RULE**: All selection prompts (path selection, intent clarification, parameter collection) **MUST use the `AskUserQuestion` tool**. **NEVER** output text-based "A / B / C" options — they are NOT clickable. Only a tool call produces an interactive dialog.

---

## Adaptive Output Rules

Templates below are the **default** format. Apply these adaptive rules:

**Level display (mandatory)**: Every output must start with the current Level on its own line: `[Level 0]` / `[Level 1]` / `[Level 2]` / `[Level 3]`. This lets the user know which level they're at and whether to upgrade.

**Level 3 output structure (Level 3 default)**: Level 3 output is structured as:
- Level → 诊断 → 意图 → 路径A（完整问题 + 可信度）→ 路径B → 路径C → 被忽略的维度 → 多选对话框
- **No comparison table** — each path is presented independently with its own optimized question and credibility summary
- User can select one or multiple paths via multi-select dialog
- User can say "expand" to see full adversarial analysis before selecting

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

Level 3 has two phases: **Phase 1** (Analysis + Paths + Selection) is shown in one go, and **Phase 2** (Final Output) is shown after the user selects paths.

### Phase 1: Analysis + Paths + Judge Results (Single Output)

The output follows this **strict order**: Level → 诊断 → 意图 → 路径A → 路径B → 路径C → 被忽略的维度 → 选择框。

**Do NOT show a comparison table.** Each path is presented independently with its own full optimized question and Judge 审查结果（反方攻击、反例、翻转条件、风险判定）。所有审查字段来自 Judge 子代理，主 Agent 不得自行修改。

```
[Level 3]

诊断: [2-3 sentences: core intent + main flaw + what mediocre answer you'd likely get]

意图: [Explain/Decision/Generate/Analyze/Explore]（如有次意图也列出）
施压策略: [primary strategy] + [secondary supplement]

路径 A — [angle tag]:
> [Full optimized question for path A, self-contained, ready to copy-paste]
反方最强攻击: [Judge 报告中 3 个反方论据的摘要，1 句话]
真实反例: [Judge 报告中的案例] 或 未验证
翻转条件: [Judge 报告中的翻转条件] 或 边界模糊
风险判定: [可靠 / 有条件 / 高风险]

路径 B — [angle tag]:
> [Full optimized question for path B, self-contained, ready to copy-paste]
反方最强攻击: [摘要]
真实反例: [案例] 或 未验证
翻转条件: [条件] 或 边界模糊
风险判定: [可靠 / 有条件 / 高风险]

路径 C — [angle tag]:
> [Full optimized question for path C, self-contained, ready to copy-paste]
反方最强攻击: [摘要]
真实反例: [案例] 或 未验证
翻转条件: [条件] 或 边界模糊
风险判定: [可靠 / 有条件 / 高风险]

被忽略的维度:
1. [Dimension]: [why it matters]
2. [Dimension]: [why it matters]
```

**Immediately after** the text output, present the **AskUserQuestion multi-select dialog**:

**AskUserQuestion parameters:**
- `question`: "选择路径（可多选），我会输出最终打磨好的问题"
- `header`: "选择路径"
- `multiSelect`: **true** — user can select multiple paths to combine
- `options`: One per path (label = "Letter — angle tag", description = 风险判定 + 反例摘要)
- **No "组合/Combine" option needed** — multi-select natively handles combination
- Place the **lowest-risk path first** (serves as recommendation hint)

**Example AskUserQuestion call (JSON, matches tool schema exactly):**
```json
{
  "questions": [
    {
      "question": "选择路径（可多选），我会输出最终打磨好的问题",
      "header": "选择路径",
      "multiSelect": true,
      "options": [
        {"label": "A — risk-first", "description": "风险判定: 可靠 | 反例: 未验证"},
        {"label": "B — counter-intuitive", "description": "风险判定: 有条件 | 反例: 某案例"},
        {"label": "C — time-horizon", "description": "风险判定: 高风险 | 反例: 某案例"}
      ]
    }
  ]
}
```

### Phase 2: Final Output (after user selection)

After the user selects one or multiple paths via the dialog:

**Single path selected:**
```
已选择: [Path X — angle tag]

优化后的问题:
> [Full polished question — clean, ready to copy-paste into any AI]

施压约束:
- [Stance Constraint]
- [Anti-Consensus Constraint]
- [Trade-off Constraint]
- [Actionability Constraint]

适用边界: [under what conditions this works best]
风险提示: [来自 Judge 报告的反例或翻转条件]
如果回答方向不对，追问: "[follow-up question]"
```

**Multiple paths selected (combination):**
```
已组合: [Path X + Path Y] — [brief description of what was merged]

融合策略: 以 [Path X] 为基础，注入 [Path Y] 的 [specific elements]

优化后的问题:
> [Full polished question — merged from selected paths, clean, ready to copy-paste]

施压约束:
- [Stance Constraint]
- [Anti-Consensus Constraint]
- [Trade-off Constraint]
- [Actionability Constraint]

适用边界: [under what conditions this works best]
风险提示: [来自 Judge 报告的反例或翻转条件]
如果回答方向不对，追问: "[follow-up question]"
```

**Combination mechanics (multi-select):**
- **2 paths selected**: Use the lower-risk path as base, inject the other's specified elements
- **3 paths selected (all)**: Use the lowest-risk path as base, inject the other two's strongest elements. Warn if over-constraining: "三条路径全组合可能导致约束过多，我会提取每条路径的核心要素而非全部内容。"
- **Conflict detection**: If combined elements contradict, flag it and suggest resolution

**Self-learning note**: After outputting the final question, silently record user preference data and append optional feedback line:

```
拿到回答后，如果方向不对回复「方向偏了」；如果很好回复「很好」。
```

---

## Interactive Dialog Patterns

### When to Use AskUserQuestion

SharpInput uses interactive dialogs in three scenarios:

1. **Gate Step 3 (Low Confidence)** — When intent classification confidence is low, present options for the user to clarify
2. **Context Completion** — When critical parameters (budget, timeline, scope, tech stack) are missing or ambiguous
3. **Stage 5 (Path Selection)** — Already implemented for path selection

### Standard Dialog Templates

**IMPORTANT**: All JSON examples below are complete and ready to use as tool call parameters. Call the AskUserQuestion tool directly with the JSON shown.

#### Budget Clarification
```json
{"questions": [{"question": "你的预算范围是？", "header": "预算", "options": [
  {"label": "1000-2000 元", "description": "入门级选择"},
  {"label": "2000-5000 元", "description": "中端选择"},
  {"label": "5000-9000 元", "description": "高端选择"},
  {"label": "其他", "description": "自定义预算范围"}
]}]}
```

#### Timeline Clarification
```json
{"questions": [{"question": "你期望的时间范围是？", "header": "时间", "options": [
  {"label": "1周内", "description": "紧急，需要快速交付"},
  {"label": "1个月内", "description": "中等节奏"},
  {"label": "3个月+", "description": "不急，可以深入打磨"},
  {"label": "其他", "description": "自定义时间范围"}
]}]}
```

#### Scope/Scale Clarification
```json
{"questions": [{"question": "你的问题规模是？", "header": "规模", "options": [
  {"label": "具体问题", "description": "单一、明确的问题点"},
  {"label": "系统性问题", "description": "涉及多个关联因素"},
  {"label": "战略性问题", "description": "长期、大方向的决策"}
]}]}
```

#### Technical vs Non-technical
```json
{"questions": [{"question": "你的问题更偏向哪个领域？", "header": "领域", "options": [
  {"label": "技术实现", "description": "代码、架构、工程相关"},
  {"label": "产品/业务", "description": "策略、增长、用户体验相关"},
  {"label": "个人决策", "description": "职业、生活、学习相关"}
]}]}
```

### Dialog Design Rules

1. **Max 4 options** — More than 4 overwhelms; use "Other" for overflow
2. **Always include "其他/Other"** — For custom values not covered by presets
3. **Description is mandatory** — Each option needs a one-line explanation
4. **Language match** — Dialog language must match user's input language
5. **No duplicate questions** — If Gate already asked, don't re-ask in Context Completion
6. **Record selection** — User's choice becomes context for all subsequent stages
