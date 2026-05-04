# SharpInput — AI 最强嘴替 / Input Optimizer

> 智能输入优化框架，通过 Opening → Gate（决策树判定级别）→ Memory Load（偏好加载）→ 意图识别 → 上下文补全 → Stage 1~3 优化（四大约束 + 多路径对抗 + Judge 审查）→ 自学习，强制 AI 产生立场、权衡和洞察。
>
> A cognitive forcing framework that sharpens any user input via Opening → Gate (decision tree) → Memory Load → Intent Recognition → Context Completion → Stage 1~3 Optimization (four constraints + multi-path adversarial + Judge review) → Self-learning, forcing AI into genuine opinions, real trade-offs, and actionable insight.

**[中文](#sharpinput--ai-输入优化器)** | **[English](#sharpinput--ai-input-optimizer)**

---

<!-- LANG:ZH-START -->

# SharpInput — AI 输入优化器

大多数人的输入方式，注定了 AI 只能给出中庸答案。SharpInput 通过 **Opening → Gate → Memory Load → 意���识别 → 上下文补全 → 优化（Stage 1~3）→ 输出 → 自学习**，强制 AI 产生立场、权衡和洞察，而非罗列教科书常识。

**不只是提问优化** — 问题陈述、需求描述、想法验证、方案评审，所有非简单查询类输入都能被优化。

## 核心理念

> **如果所有人都会给出同样的答案，那它不值得作为核心输出。**

- **逼 AI 选边站** — 不能中立，必须有立场
- **逼 AI 挑战共识** — 挑战主流观点并为其辩护
- **逼 AI 挖掘盲区** — 列出你自己都没想到的维度
- **逼 AI 做取舍** — 必须明确放弃什么来换取什么
- **逼 AI 给出可执行步骤** — 不是方向，不是框架，是一个具体行动
- **Level 0 差异化** — 3 秒内注入「一秒反问」，迫使 AI 跳出模板回答
- **独立审查** — Level 3 引入 Judge 子代理进行反方辩护 + 反例验证
- **自我学习** — 记录你的偏好和选择，越用越懂你

## 流程

```
Opening → Gate → Memory Load → 意图识别 → 上下文补全 → 优化（Stage 1~3）→ 输出
```

| 步骤 | 说明 |
|------|------|
| **Opening** | 触发后简要告知流程，降低认知摩擦 |
| **Gate** | 按决策树自动判定优化级别（Level 0~3） |
| **Memory Load** | 静默加载用户偏好，个性化后续流程 |
| **意图识别** | 判定核心意图（14类：理解/决策/生成/分析/探索/诊断/说服/验证/规划/学习/优化/对比/梳理/求助） |
| **上下文补全** | 按意图类型弹出专属选项帮助用户完善输入，信息充足则直接进入优化 |
| **Stage 1** | 问题重构 + 四大认知施压约束 + 共识检测 |
| **Stage 2** | 发散思维：2-3 条不同角度的优化路径（Level 2/3） |
| **Stage 3** | Judge 独立审查 + 路径选择 + 最终输出（Level 3） |

## Gate 决策树

自上而下匹配，命中即停：

```
输入 ≤ 15 字且无明显问题结构（无问号、无选项、无完整句子）？
  → YES: Level 0（快速施压）
  → NO: 继续

用户是否明确要求「快速」「简单」？
  → YES: Level 0
  → NO: 继续

问题方向清晰，只需打磨表述？
  → YES: Level 1（轻度优化）
  → NO: 继续

涉及选择/权衡，但选项 ≤ 2 个且约束条件单一？
  → YES: Level 2（中度施压，简化决策分析）
  → NO: 继续

涉及复杂选择/多因素交织/战略权衡？
  → YES: Level 3（深度对抗，多路径 + Judge 审查）
  → NO: Level 2（中度施压）
```

用户可随时说「深度模式」「降级」覆盖。

## 四级优化系统

| 等级 | 适用场景 | 输出 |
|------|---------|------|
| **Level 0** | 极短输入 / 要求快速 | 四大约束版问题 + 共识等级 + 一秒反问 |
| **Level 1** | 方向清晰，只需打磨表述 | 诊断 + 优化后问题 + 改进点 |
| **Level 2** | 有上下文，需要立场和约束 | 意图 + 诊断 + 施压版 + 维度 + 预警 |
| **Level 3** | 复杂决策/权衡/战略 | 诊断 → 意图 → 路径A/B/C → Judge审查 → 选择 |

**Level 0 的独特价值：** 不是简化版，而是在 3 秒内向原始问题注入一个反直觉反问（「你有没有想过 X 可能不是问题，Y 才是？」），这比直接复制原问题问 AI 有质的区别。

## 覆盖的输入类型

| 输入类型 | 示例 |
|---------|------|
| 对比分析 | "React和Vue哪个好" |
| 决策判断 | "我该不该跳槽" |
| 方案评估 | "这个架构怎么样" |
| 方向探索 | "还有什么方向" |
| 战略规划 | "怎么规划团队扩张" |
| 问题陈述 | "我们的转化率一直在下降" |
| 需求描述 | "帮我设计一个用户增长方案" |
| 想法验证 | "我觉得应该用微服务重构" |
| 方案评审 | "这是我的技术方案，帮我看看" |
| 极短输入 | "选A还是B？"（→ Level 0） |
| 纯吐槽 | "X 太难用了"（→ 隐式转化为挑战性问题） |

> 所有输入都会经过 Gate 判定级别，不存在「跳过优化」—— 简单输入走 Level 0 快速通道。

## 边界情况处理

| 输入类型 | 处理方式 |
|---------|---------|
| 极短输入（≤15 字） | → Level 0，不追问上下文 |
| 纯陈述/吐槽 | 转化为挑战性问题后正常优化 |
| 一次多条问题 | 让用户选择优先优化哪个 |
| 用户说「跳过」 | 即时输出已有内容 |
| 极长输入（>500 字） | 先压缩，再正常优化 |
| 同一问题重复触发 | 自动升级一级 |

## 四大认知施压约束

所有级别必须注入：

| 约束 | 要求 |
|------|------|
| **立场约束** | 必须选方向，不允许中立 |
| **反共识约束** | 必须挑战主流观点 |
| **取舍约束** | 不能"全都要"，必须说明放弃什么 |
| **可执行约束** | 给出本周就能做的一个具体步骤 |

## 意图识别

| 意图 | 信号 | 施压策略 |
|------|------|---------|
| **理解** | "是什么"、"怎么用"、"解释"、"啥意思" | 反直觉锚点：提出反常识观点并证明 |
| **决策** | "应不应该"、"怎么选"、"A还是B"、"值不值" | 遗憾预演：3年后你最后悔什么？ |
| **生成** | "帮我做"、"设计"、"写一个"、"搞一个" | 最小可行方案：只保留一个要素，选哪个？ |
| **分析** | "分析"、"评估"、"方案怎么样"、"看看" | 隐含假设暴露：前提不成立时结论怎么变？ |
| **探索** | "有什么方向"、"其他选择"、"头脑风暴" | 魔鬼代言人：说服对手走你反对的路线 |
| **诊断/调试** | "为什么报错"、"排查"、"跑不通"、"挂了" | 根因追问：你确定问题出在这里而不是X？ |
| **说服/沟通** | "怎么说服"、"怎么让X同意"、"咋让X同意" | 角色反转：如果你是对方，这个说法哪里让你抗拒？ |
| **验证/确认** | "对不对"、"可行吗"、"靠不靠谱" | 魔鬼审判：假设你的结论是错的，最强证据是什么？ |
| **规划** | "规划"、"路线图"、"怎么落地"、"时间表" | 逆向拆解：从终点往回推，第一步必须是什么？ |
| **学习/习得** | "教我"、"怎么学"、"入门"、"从哪开始学" | 学习路径压测：砍掉80%只留核心，你选哪20%？ |
| **优化/改进** | "怎么让X更好"、"如何提升"、"调优" | 削砍测试：必须砍掉一个优化方向，砍哪个？ |
| **比较/对比** | "有什么区别"、"哪个更好"、"区别在哪" | 差异压测：什么条件下这两个会变得一模一样？ |
| **总结/梳理** | "帮我整理"、"总结"、"梳理"、"理一下" | 极限压缩：用一句话概括全部，你选哪句？ |
| **求助/救援** | "卡住了"、"搞不定"、"怎么办" | 穿刺提问：卡在哪一步？方向不清、方案不行、还是执行不动？ |

> 每种意图识别后，自动弹出**专属上下文选项**帮助用户完善输入（如决策→问约束条件，生成→问受众格式），而非千篇一律问"背景/目标/场景"。

## Judge 独立审查（Level 3）

Level 3 引入独立 Judge 子代理，对每条优化路径执行三项审查：

| 审查项 | 说明 |
|--------|------|
| **反方辩护** | 假设其他路径更好，用 3 个具体论据攻击当前路径 |
| **真实反例** | 找真实失败案例（主体 + 时间 + 原因），找不到写"未验证" |
| **翻转条件** | 可量化的条件下结论会反转，无法确定写"边界模糊" |

> 调用 Judge 前告知用户等待约 10-30 秒。失败自动重试一次 → 仍失败降级为内联审查。

## 多路径交互选择（Level 3）

Level 3 生成 2-3 条不同角度的优化路径：

| 角度标签 | 含义 |
|---------|------|
| `risk-first` | 聚焦风险和下行分析 |
| `counter-intuitive` | 寻找反直觉答案 |
| `minimalist` | 精简到最核心要素 |
| `adversarial` | 站在对立面辩护 |
| `time-horizon` | 拉到 3-5 年后审视 |
| `role-reversal` | 从意想不到的视角切入 |

支持单选或多选组合。组合时按冲突决策优先级合并：**安全优先 > 信息量优先 > 用户偏好优先**。

## 自我学习系统

- **全级别记录** — Level 0/1/2/3 的选择都被学习
- **静默生效** — 偏好自动生效，不打断交互节奏
- **滑动窗口** — 基于最近 10 次交互，自然衰减
- **角度偏好** — 记住你偏好的路径角度，下次优先匹配
- **等级偏好** — 如果你 ≥70% 用 Level 3，低级别时主动建议升级
- **随时重置** — 说"重置偏好"即可清零

## Before vs After

### 示例 1：问题陈述 → 优化

**原输入：**
> 我们的转化率一直在下降。

**普通 AI 回答：**
> 1. 分析漏斗数据 2. 做 A/B 测试 3. 优化落地页 4. 提升用户体验 5. 加强用户运营
> （搜索引擎第一页的内容，任何 AI 都会给出类似答案）

**SharpInput 输出：**
> 我们是一个 toB SaaS 产品，注册到付费转化率从 8% 降到 3%，持续 3 个月。流量没变，产品没大改。
> **必须明确回答：问题出在产品、市场还是销售环节？** 不允许说"需要综合分析"。
> 给出一个**大多数人不会考虑的根因假设**，并为其辩护。
> 如果按你的诊断做了调整，**3 个月后最可能后悔的是什么？**

### 示例 2：想法验证 → 多路径优化

**原输入：**
> 我觉得应该用微服务重构我们的单体应用。

**SharpInput 输出（Level 3）：**

| 路径 | 角度 | 优化后的问题 | 风险判定 |
|------|------|------------|---------|
| A | risk-first | "假设微服务重构会在 6 个月内让团队产出降低 40%，你还坚持吗？..." | 可靠 |
| B | counter-intuitive | "说服我为什么不该用微服务——列出 3 个你的单体架构其实比微服务更适合的理由..." | 有条件 |
| C | time-horizon | "站在 3 年后回看，微服务重构可能带来的最大技术债务是什么？..." | 有条件 |

> 路径 A 风险最低，推荐首选。

### 示例 3：需求描述 → 优化

**原输入：**
> 帮我设计一个用户增长方案。

**SharpInput 输出：**
> 我是一个 B2C 教育产品的产品经理，DAU 5 万，月留存 20%，预算 10 万/月，目标 3 个月内 DAU 翻倍。
> **必须选择一个增长方向：拉新还是留存？** 不允许"两手都要抓"。
> 明确说出你**放弃的那个方向的最大机会**，以及你为什么认为它在当前阶段不重要。
> 给出一个**反常识的增长策略**，并用具体案例证明它有效。

## 适用场景

| 适合 | 不适合 |
|------|--------|
| 决策类 — 技术选型、职业选择、产品方向 | 事实查询 — "闭包是什么"（→ Level 0 快速通道） |
| 复杂分析 — 竞品分析、架构设计、方案评估 | 简单问答 — "北京今天天气"（→ Level 0） |
| 战略思考 — 商业模式、增长策略、优先级排序 | 代码 Debug — "这段代码报错了"（→ Level 0） |
| 问题陈述 — 转化率下降、用户流失、性能瓶颈 | 翻译/摘要 — 纯信息转换类（→ Level 0） |
| 需求描述 — 产品设计、方案制定、功能规划 | |
| 想法验证 — 架构重构、策略调整、模式创新 | |
| 方案评审 — 技术方案、产品方案、商业计划 | |

**一句话判断标准：** 如果这个输入扔给搜索引擎也能得到差不多的答案 → Level 0 快速通道帮你注入反共识角度。复杂决策 → Level 3 全面对抗分析。

## 安装

```bash
git clone https://github.com/gaoyechen/SharpInput.git
```

将 `SKILL.md` 和 `references/` 目录放入你的 AI Agent 的 skills 目录中。

## 使用方式

**触发词：**
- `帮我优化` / `优化输入` / `优化提问` / `优化一下`
- `帮我理清思路` / `帮我完善一下` / `帮我改一下`
- `这样表述好不好` / `这样说对不对` / `我这样说合适吗`

**等级控制：** `深度模式` → Level 3 / `简单优化` → Level 1

**偏好管理：** `重置偏好` → 清除历史偏好数据

## 文件结构

```
SharpInput/
├── SKILL.md                         # 主文件：完整流程 + Gate 决策树 + 边界规则
├── references/
│   ├── output-templates.md          # 输出模板（Level 0~3）
│   ├── judge-prompt.md              # Judge 子代理 prompt（反方辩护 + 反例 + 翻转条件 + 重试策略）
│   ├── prompt-patterns.md           # 共识识别与打破技巧、高质量问题信号
│   ├── self-learning.md             # 自学习系统规范
│   └── user-preferences.md          # 用户偏好数据（自动维护）
├── README.md
└── LICENSE                          # MIT License
```

## License

MIT

---

> **输入锐，回答深。** — SharpInput

<!-- LANG:ZH-END -->

---

<!-- LANG:EN-START -->

# SharpInput — AI Input Optimizer

Most people provide inputs in ways that guarantee mediocre answers. SharpInput applies **Opening → Gate → Memory Load → Intent Recognition → Context Completion → Stage 1~3 Optimization → Self-learning** to force AI into producing answers with genuine positions, real trade-offs, and actionable insight.

**Not just question optimization** — Problem statements, requirement descriptions, idea validation, plan reviews, and all non-trivial inputs can be optimized.

## Core Philosophy

> **If everyone would give the same answer, it's not worth producing.**

- **Forces AI to pick a side** — No neutrality allowed
- **Forces AI to challenge consensus** — Must challenge mainstream views and defend it
- **Forces AI to surface blind spots** — Dimensions you hadn't considered
- **Forces AI to sacrifice** — Must declare what it gives up
- **Forces AI to give actionable steps** — Not a direction, not a framework, a concrete action
- **Level 0 differentiator** — Injects a "one-second counter-question" in 3 seconds to break AI template answers
- **Independent review** — Level 3 invokes a Judge subagent for adversarial review + counter-examples
- **Self-learning** — Remembers your preferences, gets better over time

## Flow

```
Opening → Gate → Memory Load → Intent Recognition → Context Completion → Optimization (Stage 1~3) → Output
```

| Step | Description |
|------|-------------|
| **Opening** | Brief overview of what will happen |
| **Gate** | Decision tree auto-assigns Level 0~3 |
| **Memory Load** | Silently load user preferences |
| **Intent Recognition** | Classify core intent (14 types: Explain/Decision/Generate/Analyze/Explore/Debug/Persuade/Validate/Plan/Learn/Improve/Compare/Summarize/Stuck) |
| **Context Completion** | Intent-specific context options to refine input, skip if info sufficient |
| **Stage 1** | Problem reframing + four cognitive forcing constraints + consensus check |
| **Stage 2** | Divergent thinking: 2-3 paths from different angles (Level 2/3) |
| **Stage 3** | Independent Judge review + path selection + final output (Level 3) |

## Gate Decision Tree

Top-down matching, stop on first hit:

```
Input ≤ 15 chars and no clear question structure (no question mark, no options, no complete sentence)?
  → YES: Level 0 (rapid forcing)
  → NO: continue

User explicitly asking for "quick" or "simple"?
  → YES: Level 0
  → NO: continue

Clear direction, just needs phrasing polish?
  → YES: Level 1 (light optimization)
  → NO: continue

Involves choices / trade-offs, but ≤ 2 options and single constraint?
  → YES: Level 2 (medium forcing, simplified decision analysis)
  → NO: continue

Complex choices / multi-factor analysis / strategic trade-offs?
  → YES: Level 3 (deep adversarial, multi-path + Judge review)
  → NO: Level 2 (medium forcing)
```

Users can override anytime with "deep mode" / "downgrade".

## Four-Level System

| Level | When to Use | Output |
|-------|------------|--------|
| **Level 0** | Very short input / quick request | Forced question + consensus level + one-second counter-question |
| **Level 1** | Clear direction, needs polish | Diagnosis + optimized question + improvements |
| **Level 2** | Has context, needs stance & constraints | Intent + diagnosis + forced version + dimensions + warnings |
| **Level 3** | Complex decisions / trade-offs / strategy | Diagnosis → intent → paths A/B/C → Judge review → selection |

**Level 0's unique value:** It's not a "dumbed-down version". It injects a counter-intuitive twist ("Have you considered X might not be the problem and Y is?") that forces the AI out of template mode. That's a qualitative leap from raw copy-paste.

## Covered Input Types

| Input Type | Example |
|-----------|---------|
| Comparison | "React vs Vue" |
| Decision | "Should I change jobs" |
| Analysis | "How is this architecture" |
| Exploration | "What directions are there" |
| Strategy | "How to scale my team" |
| Problem statement | "Our conversion rate keeps declining" |
| Requirement | "I need a user growth strategy" |
| Idea validation | "I think we should refactor to microservices" |
| Plan review | "Here's my technical plan, review it" |
| Very short | "A or B?" (→ Level 0) |
| Rant/vent | "X is impossible to use" (→ implicitly converted) |

> All inputs go through Gate — nothing is "skipped". Simple inputs get the Level 0 fast lane.

## Edge Cases

| Input Type | Handling |
|-----------|----------|
| Very short (≤15 chars) | → Level 0, no context questions |
| Pure statement / venting | Convert to challenge question, then optimize |
| Multiple questions at once | Ask user to pick priority |
| User says "skip" | Output current progress immediately |
| Very long (>500 chars) | Compress first, then optimize |
| Duplicate trigger on same question | Auto-upgrade one level |

## Four Cognitive Forcing Constraints

All levels must inject these:

| Constraint | Requirement |
|-----------|-------------|
| **Stance** | Must pick a side, no neutrality |
| **Anti-consensus** | Must challenge mainstream views |
| **Trade-off** | Can't "have it all"; must declare what to sacrifice |
| **Actionability** | Give one specific action doable this week |

## Intent Recognition

| Intent | Signal | Forcing Strategy |
|--------|--------|------------------|
| **Explain** | "What is", "How to use", "Explain" | Counter-intuitive anchor: propose & defend an unconventional view |
| **Decision** | "Should I", "A or B", "Which to choose", "worth it?" | Regret pre-mortem: what will you regret most in 3 years? |
| **Generate** | "Help me build", "Design", "Write", "make one" | Minimal viable: keep only one element — which one? |
| **Analyze** | "Analyze", "Evaluate", "Review this plan", "take a look" | Hidden assumptions: how does the conclusion change if the premise is wrong? |
| **Explore** | "What directions", "Other options", "Brainstorm" | Devil's advocate: convince your opponent to take the path you oppose |
| **Debug** | "Why error", "Not working", "Crashed", "broken" | Root cause push: are you sure the problem is here and not X? |
| **Persuade** | "How to convince", "How to get X to agree" | Role reversal: if you were the other side, what would you resist? |
| **Validate** | "Is this right", "Feasible?", "Reliable?" | Devil's trial: assume your conclusion is wrong — strongest evidence? |
| **Plan** | "Plan", "Roadmap", "How to land", "timeline" | Reverse engineer: working back from the end, what must step 1 be? |
| **Learn** | "Teach me", "How to learn", "Start from where" | Learning path stress: cut 80%, keep core 20% — which 20%? |
| **Improve** | "How to make X better", "Improve", "optimize" | Cut test: must drop one optimization direction — which one? |
| **Compare** | "What's the difference", "Which is better" | Difference stress: under what condition would they become identical? |
| **Summarize** | "Help me organize", "Summarize", "sort out" | Extreme compression: one sentence for everything — which sentence? |
| **Stuck** | "I'm stuck", "Can't figure out", "What now" | Pinpoint: are you stuck on direction, plan, or execution? |

> After intent recognition, the system presents **intent-specific context options** to help users refine their input (e.g., Decision → ask constraints; Generate → ask audience & format), rather than generic "background/goals/context" questions.

## Judge-Driven Review (Level 3)

Level 3 invokes an independent Judge subagent for three reviews per path:

| Review | Description |
|--------|-------------|
| **Adversarial defense** | Attack each path with 3 specific arguments, assuming another path is better |
| **Real counter-example** | Find a real-world case where a similar strategy failed (entity + time + cause), or "unverified" |
| **Flip conditions** | Quantified boundary under which the conclusion reverses, or "boundary unclear" |

> User is told "starting independent review…" (~10-30 sec). On failure: one retry with simplified prompt → then degrade to inline review.

## Multi-Path Interactive Selection (Level 3)

Level 3 generates 2-3 optimized paths from different angles:

| Angle Tag | Meaning |
|-----------|---------|
| `risk-first` | Focus on downside analysis |
| `counter-intuitive` | Seek the non-obvious answer |
| `minimalist` | Strip to essentials |
| `adversarial` | Argue against the obvious |
| `time-horizon` | Shift to 3-5 years out |
| `role-reversal` | Unexpected stakeholder perspective |

Single or multi-select. When combining, conflict resolution priority: **Safety > Information coverage > User preference**.

## Self-Learning System

- **All-level tracking** — Level 0/1/2/3 choices are all learned
- **Silent operation** — Preferences manifest without interrupting flow
- **Sliding window** — Based on last 10 interactions, naturally decays
- **Angle preference** — Remembers your preferred path angles, prioritizes next time
- **Level bias** — If ≥70% of sessions use Level 3, proactively suggests upgrade at lower levels
- **Easy reset** — Say "reset preferences" to clear

## Before vs After

### Example 1: Problem Statement

**Original:**
> Our conversion rate keeps declining.

**Typical AI answer:**
> 1. Analyze funnel data 2. Run A/B tests 3. Optimize landing page 4. Improve UX 5. Strengthen user operations

**SharpInput output:**
> We're a B2B SaaS product. Registration-to-paid conversion dropped from 8% to 3% over 3 months. Traffic unchanged, no major product changes.
> **You must answer: is the problem in product, marketing, or sales?** "Needs comprehensive analysis" is not allowed.
> Give a root cause hypothesis that **most people wouldn't consider** and defend it.
> Tell me: if I follow your diagnosis, **what will I most likely regret 3 months from now?**

### Example 2: Idea Validation (Multi-Path)

**Original:**
> I think we should refactor our monolith to microservices.

**SharpInput output (Level 3):**

| Path | Angle | Optimized Question | Risk |
|------|-------|-------------------|------|
| A | risk-first | "Assume microservice refactoring will reduce team output by 40% for 6 months. Still want to do it?..." | Low |
| B | counter-intuitive | "Convince me why you should NOT use microservices — list 3 reasons your monolith is actually better..." | Conditional |
| C | time-horizon | "Looking back from 3 years in the future, what's the biggest tech debt microservices might create?..." | Conditional |

> Path A has the lowest risk — recommended.

### Example 3: Requirement

**Original:**
> I need a user growth strategy.

**SharpInput output:**
> I'm a PM for a B2C education product. DAU 50K, monthly retention 20%, budget 100K/month. Goal: double DAU in 3 months.
> **You must choose one growth direction: acquisition or retention?** "Both" is not allowed.
> State the **biggest opportunity you're giving up** in the other direction and why it doesn't matter now.
> Give a **counter-intuitive growth strategy** with a specific case proving it works.

## When to Use

| Great Fit | Poor Fit |
|-----------|----------|
| Decisions — Tech stack, career, product direction | Factual lookup — "What is a closure" (→ Level 0 fast lane) |
| Complex analysis — Competitor analysis, architecture | Simple Q&A — "What's the weather" (→ Level 0) |
| Strategy — Business models, growth, prioritization | Debug — "This code throws an error" (→ Level 0) |
| Problem statements — Declining metrics, user churn | Translation/summary — Pure info conversion (→ Level 0) |
| Requirements — Product design, feature planning | |
| Idea validation — Architecture refactoring, strategy shifts | |
| Plan reviews — Technical plans, business proposals | |

**One-line rule:** If a search engine would give roughly the same answer → Level 0 fast lane injects an anti-consensus angle. Complex decisions → Level 3 full adversarial analysis.

## Installation

```bash
git clone https://github.com/gaoyechen/SharpInput.git
```

Place `SKILL.md` and `references/` into your AI Agent's skills directory.

## Usage

**Triggers:**
- `Optimize this` / `Make this better` / `How to ask this better`
- `Help me organize` / `Is this good enough` / `How should I phrase this`

**Level control:** `deep mode` → Level 3 / `simple optimization` → Level 1

**Preferences:** `reset preferences` → Clear preference data

## File Structure

```
SharpInput/
├── SKILL.md                         # Core: full flow + Gate decision tree + boundary rules
├── references/
│   ├── output-templates.md          # Output templates (Level 0~3)
│   ├── judge-prompt.md              # Judge agent prompt (adversarial + counter-example + flip conditions + retry)
│   ├── prompt-patterns.md           # Consensus detection & breaking, high-quality question signals
│   ├── self-learning.md             # Self-learning system specification
│   └── user-preferences.md          # User preference data (auto-maintained)
├── README.md
└── LICENSE                          # MIT License
```

## License

MIT

---

> **Input sharp, answer deep.** — SharpInput

<!-- LANG:EN-END -->
