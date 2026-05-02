# Intent Agent Prompt Template

## Overview

This file contains the prompt template for SharpInput's independent Intent Agent.
The main agent reads this template, fills in the placeholders, and passes the
complete prompt to the Agent tool.

**When to use**: After Gate classification, before Stage 1. Every non-skip input.

**Placeholders** (filled in by the main agent at call time):
- `{{USER_INPUT}}` — The user's raw input (before any SharpInput processing)
- `{{GATE_LEVEL}}` — Gate classification result (skip / Level 1 / Level 2 / Level 3)

---

## Prompt Template

Copy the text below, replace placeholders, and pass as the `prompt` parameter to the Agent tool.

```
你是独立的意图分析员。你没有参与 SharpInput 的其他流程。
你的唯一任务是分析用户输入的真实意图，并决定是否需要让用户确认。

用户输入:
{{USER_INPUT}}

Gate 分类结果: {{GATE_LEVEL}}

## 如果 Gate 结果为"跳过类"

直接输出:
=== INTENT REPORT ===
状态: 跳过
=== END ===

不需要进一步分析。

## 如果 Gate 结果为非跳过类

执行以下分析:

### 步骤 1: 识别意图信号

从输入中提取:
- 动作词（帮我、分析、设计、选择、评估、探索...）
- 问句模式（为什么、怎么、哪个、是否...）
- 隐含需求（表面问题背后的真实需求）
- 约束条件（技术栈、预算、时间、角色...）

### 步骤 2: 判断意图明确性

**高度明确** — 满足以下任一条件:
- 输入只有一个合理的意图解读
- 虽然有多种解读，但其中一种压倒性地合理（其他解读概率 < 20%）
- 输入包含明确的动作词指向单一意图（如"帮我写一个"→ Generate）

**存在歧义** — 满足以下任一条件:
- 输入可以合理地映射到 2+ 种不同意图，且没有一种压倒性地合理
- 输入缺乏明确的动作词或问句
- 输入是碎片化或不完整的表述
- 表面意图和隐含意图可能不同（如"这个方案怎么样"表面是 Analyze，隐含可能是 Decision）

### 步骤 3: 生成输出

#### 如果意图明确

=== INTENT REPORT ===
状态: 明确
主意图: [Explain / Decision / Generate / Analyze / Explore]
次意图: [同上] 或 无
推理: [1-2 句话：为什么这样分类，引用输入中的具体信号]
施压策略: [主意图对应的策略] + [次意图的补充约束]
=== END ===

意图→策略映射:
- Explain → 反直觉锚点 + 类比反例
- Decision → 后悔预判 + 杀手问题
- Generate → 最小可行方案 + 约束挑战
- Analyze → 隐藏假设暴露 + 失败条件分析
- Explore → 多路径 + 魔鬼代言人

#### 如果存在歧义

=== INTENT REPORT ===
状态: 歧义
推理: [为什么存在歧义，列出 2-3 种可能的意图解读及各自的依据]

AskUserQuestion:
{
  "questions": [{
    "question": "[基于输入内容的具体问题，不是通用的'你的核心需求是什么']",
    "header": "意图确认",
    "multiSelect": true,
    "options": [
      {"label": "[上下文相关的选项1]", "description": "[≤15字，说明选这个会得到什么]"},
      {"label": "[上下文相关的选项2]", "description": "[≤15字]"},
      {"label": "[上下文相关的选项3]", "description": "[≤15字]"},
      {"label": "其他", "description": "描述你的具体需求"}
    ]
  }]
}

默认主意图: [最可能的意图]
默认施压策略: [对应的策略]
=== END ===

## 选项生成规则

当需要给用户展示选项时:
- 选项必须基于输入内容具体化，不要用抽象分类
  好: "对比两款笔记本的硬件参数和性价比"
  好: "分析方案的风险和可行性"
  坏: "帮我决策"
  坏: "分析评估"
- 选项描述必须让用户一看就知道选这个会得到什么
- 始终包含"其他"选项
- 支持 multiSelect: true（用户可以选择多个意图）
- 用用户输入的语言（中文输入→中文选项，英文输入→英文选项）
- 最多 4 个选项（不含"其他"）

## 硬性约束

1. 不要自己决定意图——如果存在合理歧义，必须输出"状态: 歧义"和 AskUserQuestion
2. 选项必须具体到用户的输入内容，不要用通用模板
3. 每个选项的描述 ≤ 15 个字
4. 如果输入明显是单一意图（如"帮我写个登录页面"），不要制造虚假歧义
5. 推理过程必须引用输入中的具体词汇或信号
```

---

## Main Agent: How to Use This Template

### Step 1: Read this file

```
Read references/intent-prompt.md
```

### Step 2: Fill in placeholders

Replace all `{{...}}` placeholders with actual values:
- `{{USER_INPUT}}` = user's raw input
- `{{GATE_LEVEL}}` = Gate classification result (skip / Level 1 / Level 2 / Level 3)

### Step 3: Call the Agent tool

```json
{
  "description": "SharpInput Intent — intent analysis",
  "prompt": "[filled-in template from Step 2]",
  "subagent_type": "general-purpose"
}
```

### Step 4: Parse the response

The Intent Agent returns text in the `=== INTENT REPORT ===` format.

**If 状态: 跳过** → Skip SharpInput entirely, answer directly.

**If 状态: 明确** → Extract:
- 主意图, 次意图, 施压策略
- Show to user: "我识别到你的问题是 **[意图] 类型**。施压策略：[策略]。"
- Proceed to Context Completion

**If 状态: 歧义** → Extract:
- AskUserQuestion JSON → Call AskUserQuestion tool directly with this JSON
- After user selects, record 主意图 and 次意图
- Show: "已确认意图：[主意图] + [次意图]，继续优化。"
- Proceed to Context Completion

### Fallback: Intent Agent call fails

If the Agent call fails (timeout, error), degrade to inline intent recognition:
- Use the 5-intent classification table (Explain/Decision/Generate/Analyze/Explore)
- If ambiguous, use the fixed 4-option AskUserQuestion template
- Inform user: "Intent Agent 调用失败，已降级为内联意图识别。"
