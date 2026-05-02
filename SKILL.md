---
name: SharpInput
description: >
  Optimize any user input (questions, statements, plans, ideas, requirements) through
  deep cognitive self-checking, multi-dimensional reframing, and anti-consensus detection
  to force AI outputs with genuine opinions, clear positions, and real insight —
  not "correct but useless" platitudes.
  Triggers: "optimize this", "how to ask better", "help me organize", "is this good enough",
  "how should I phrase this", "make this better", any discussion about input/question quality,
  pasting content asking for optimization, or any non-trivial input that benefits from sharpening.
  中文触发词: "优化这个问题", "帮我优化", "怎么问更好", "帮我组织一下",
  "这样问行不行", "这样表述好不好", "帮我改一下", "优化提问", "优化输入",
  "帮我理清思路", "这个问题问得好不好", "帮我润色", "优化一下",
  "这样说对不对", "帮我理一下", "我这样说合适吗", "帮我完善一下".
agent_created: true
allowed-tools: Read, Write, Glob, Bash, AskUserQuestion, Agent
---

# SharpInput — AI Input Optimizer

将用户输入（问题、陈述、方案、想法、需求）打磨成能逼出 AI 真正见解的高质量问题。

**交互规则**：需要用户选择时（意图确认、参数收集、路径选择），**必须用 AskUserQuestion 工具弹出选择窗口**，不要输出文字选项。

## 流程

```
Gate → 意图识别 → 上下文补全 → 优化（Stage 1~3）→ 输出
```

---

## Gate：分级

快速判断用户输入的优化级别：

| 级别 | 适用场景 | 输出 |
|------|---------|------|
| **Level 0** | 用户明确要求快速优化，无深度分析需求 | 认知施压版问题 + 共识等级 |
| **Level 1** | 方向清晰，只需打磨表述 | 诊断 + 优化后问题 + 改进点 |
| **Level 2** | 有上下文，需要立场和约束 | 意图 + 诊断 + 施压版 + 维度 + 预警 |
| **Level 3** | 复杂决策/权衡/战略，需要多路径对抗分析 | 诊断 → 意图 → 路径A/B/C → 忽略维度 → 选择 |

- 用户说"深度模式"、"Level 3"、"施压一下" → 直接进入对应级别
- 用户说"降级"、"简单点" → 降级处理

---

## 意图识别

判断用户输入的核心意图类型：

| 意图 | 信号 | 施压策略 |
|------|------|---------|
| **理解** | "是什么"、"怎么用"、"解释" | 反直觉锚点：提出反常识观点并证明 |
| **决策** | "应不应该"、"怎么选"、"A还是B" | 遗憾预演：3年后你最后悔什么？ |
| **生成** | "帮我做"、"设计"、"写一个" | 最小可行方案：只保留一个要素，选哪个？ |
| **分析** | "分析"、"评估"、"方案怎么样" | 隐含假设暴露：前提不成立时结论怎么变？ |
| **探索** | "有什么方向"、"其他选择"、"头脑风暴" | 魔鬼代言人：说服对手走你反对的路线 |

**如果意图存在歧义**（多种合理解读），用 AskUserQuestion 让用户选择：
```
问题: "[基于输入内容的具体问题]"
  header: "意图确认"
  选项:
    - "[上下文相关选项1]" : [选这个会得到什么]
    - "[上下文相关选项2]" : [选这个会得到什么]
    - "[上下文相关选项3]" : [选这个会得到什么]
    - "其他" : 描述你的具体需求
```
- 选项必须具体到用户的输入内容，不要用通用模板
- 语言匹配用户输入（中文输入 → 中文选项）

---

## 上下文补全

> **不猜测规则**：不能从输入中推断的信息（背景、目标、场景），**停下来问**。猜测式优化产出平庸结果。

三个维度：**背景**（谁？什么行业/技术栈？）、**目标**（短期还是长期？）、**场景**（团队规模？时间约束？）

- 信息充足 → "问题信息充分，直接进入优化。"
- 信息不足 → 用 AskUserQuestion 询问，格式同上（最多 4 选项 + "其他"）
- Gate 已问过的问题不要重复问

---

## Stage 1：问题重构 + 认知施压（内部执行，不展示）

**重构**：识别表面问题背后的真实需求，限定范围，长输入压缩到 2-3 句。

**四大基础约束**（所有级别必须注入）：

| 约束 | 要求 |
|------|------|
| 立场约束 | 必须选方向，不允许中立 |
| 反共识约束 | 必须挑战主流观点 |
| 取舍约束 | 不能"全都要"，必须说明放弃什么 |
| 可执行约束 | 给出本周就能做的一个具体步骤 |

**共识检测**：评估结果的共识等级。
- 🟢 低共识（有差异化见解）→ OK
-  中共识 → OK
-  高共识（搜索引擎首页就能找到）→ 必须加强约束直到降到 🟡

---

## Stage 2：发散思维

生成 2-3 条不同路径，每条路径：
- 一个**角度标签**（见下表）
- 完整的**优化后问题**（自包含，可直接复制使用）
- 融入 Stage 1 的认知施压约束

**标准角度**：`risk-first`（风险优先）、`counter-intuitive`（反直觉）、`minimalist`（极简）、`adversarial`（对抗）、`time-horizon`（时间维度）、`role-reversal`（角色反转）

---

## Stage 3：独立审查 + 收敛

**Step 1 — Judge 审查**

将路径文本（不含生成过程）和原始问题发给独立 Judge 子代理。Judge 执行：
- **反方辩护**：假设其他路径更好，用 3 个具体论据攻击当前路径
- **真实反例**：找一个类似策略失败的真实案例（主体 + 时间 + 原因），找不到写"未验证"
- **翻转条件**：什么具体参数下结论会反转，无法确定写"边界模糊"

> Judge 模板在 `references/judge-prompt.md`。Judge 失败时降级为内联审查。

**Step 2 — 呈现路径，让用户选择**

输出所有路径（每条独立展示完整优化问题 + Judge 审查结果），然后用 AskUserQuestion 让用户选择：
```
问题: "选择路径（可多选），我会输出最终打磨好的问题"
  header: "选择路径"
  multiSelect: true
  选项:
    - "A — [角度标签]" : 风险判定: [可靠/有条件/高风险] | 反例: [摘要]
    - "B — [角度标签]" : 风险判定: [可靠/有条件/高风险] | 反例: [摘要]
```
- 最低风险路径排第一
- 不需要"组合"选项——多选本身支持组合

**Step 3 — 最终输出**

用户选择后，输出：
```
优化后的问题:
> [完整优化问题，可直接复制到任何 AI]

施压约束:
- 立场 / 反共识 / 取舍 / 可执行

适用边界: [最佳使用条件]
风险提示: [来自 Judge 的反例或翻转条件]
如果方向不对，追问: "[追问问题]"
```

多选时：以低风险路径为基础，注入其他路径的核心要素。

---

## 输出格式

> 完整模板见 `references/output-templates.md`。

- 每次输出开头标注级别：`[Level 0]` / `[Level 1]` / `[Level 2]` / `[Level 3]`
- 结尾提示：`说「升级」可进入 Level X。`
- 语言匹配用户输入

---

## 边界规则

1. Gate 优先 — 快速问题直接回答，零摩擦
2. 意图透明 — 展示识别结果，用户可随时覆盖
3. 不猜测上下文 — 信息不足就问
4. 不改变核心意图 — 优化提问方式，不改变用户该问什么
5. 即用 — 优化后问题可直接复制使用
6. 尊重用户选择 — 用户可随时覆盖级别和意图标签
7. Judge 驱动 — Level 3 风险判定必须来自 Judge，不得自行修改
8. 偏好静默应用 — 读取 `references/user-preferences.md`，不告知用户

---

## 参考文件

- `references/output-templates.md` — 输出模板（Level 0~3）
- `references/judge-prompt.md` — Judge 子代理 prompt 模板
- `references/prompt-patterns.md` — 共识识别与打破技巧
- `references/self-learning.md` — 自学习系统规范
- `references/user-preferences.md` — 用户偏好数据（自动维护）
