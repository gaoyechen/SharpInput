# SharpInput — AI 输入优化器 / Input Optimizer

> 智能输入优化框架，让你的任何输入（提问、陈述、方案、想法、需求）都被打磨成能让 AI 输出有洞察力观点的高质量版本。
>
> A cognitive forcing framework that sharpens any user input into versions that force AI into producing genuine opinions, real trade-offs, and actionable insight.

**[中文](#sharpinput--ai-输入优化器)** | **[English](#sharpinput--ai-input-optimizer)**

---

<!-- LANG:ZH-START -->

# SharpInput — AI 输入优化器

大多数人的输入方式，注定了 AI 只能给出中庸答案。SharpInput 通过 **场景判断 → 记忆加载 → 意图识别 → 上下文补全 → 问题重构 → 认知施压 → 多路径生成 → 自我对抗 → 收敛输出 → 偏好学习**，强制 AI 产生立场、权衡和洞察，而非罗列教科书常识。

**不只是提问优化** — 问题陈述、需求描述、想法验证、方案评审，所有非简单查询类输入都能被优化。

## 核心理念

> **如果所有人都会给出同样的答案，那它不值得作为核心输出。**

- **逼 AI 选边站** — 不能中立，必须有立场
- **逼 AI 自我对抗** — 找反例、找失效条件、打掉幻觉
- **逼 AI 挖掘盲区** — 列出你自己都没想到的维度
- **逼 AI 放弃"全都要"** — 必须明确放弃什么来换取什么
- **逼 AI 给出可执行步骤** — 不是方向，不是框架，是一个具体行动
- **智能分流** — 简单问题直接答，不走过度流程
- **自我学习** — 记住你的偏好，越用越懂你

## 四级施压系统

| 等级 | 名称 | 执行阶段 | 适用场景 |
|------|------|---------|---------|
| **Level 0** | 极速施压 | 仅认知施压 → 输出施压版问题 | 只想要一个好问题，不需要分析 |
| **Level 1** | 轻度优化 | 问题重构 → 输出 | 输入质量不错，只需微调表述 |
| **Level 2** | 中度施压 | 问题重构 → 认知施压 + 深度施压层 | 需要有立场，但不需要完整对抗 |
| **Level 3** | 深度对抗 | 完整五阶段 + 多路径交互选择 | 复杂决策、需要全面分析 |

**自动分流**：查资料、Debug、翻译等简单问题直接回答，零摩擦。
**随时切换**：说"深度模式"升级到 Level 3，说"简单优化"降到 Level 1，说"施压一下"用 Level 0。

## 覆盖的输入类型

**进入优化流程：**

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

**直接回答，跳过优化：**

| 输入类型 | 示例 |
|---------|------|
| 事实查询 | "闭包是什么" |
| 调试报错 | "这段代码报错了" |
| 格式转换 | "翻译成英文" |

## 四大认知施压约束

| 约束 | 作用 |
|------|------|
| **立场约束** | 必须选边站，不允许中立 |
| **反共识约束** | 必须挑战主流观点并为其辩护 |
| **权衡约束** | 不能"全都要"，必须明确放弃什么 |
| **可执行约束** | 必须给出下周就能执行的一个具体步骤 |

## 意图识别

| 意图 | 含义 | 典型输入 | 施压策略 |
|------|------|---------|---------|
| Explain | 理解概念/原理 | 提问 / 需要根因分析的问题陈述 | 反直觉锚点 + 类比反例 |
| Decision | 做出选择/判断 | 提问 / 需要权衡评估的想法 | 后悔预判 + 杀手问题 |
| Generate | 生成代码/内容/方案 | 提问 / 需求描述 | 最简方案 + 约束挑战 |
| Analyze | 分析/评估/审查 | 提问 / 方案评审 / 想法验证 | 隐含假设暴露 + 失效条件 |
| Explore | 探索方向/寻找可能 | 提问 / 寻求解空间的问题陈述 | 多路径 + 反面辩护 |

支持主意图 + 次意图双标签，用户可覆盖识别结果。

## 多路径交互选择（Level 3）

Level 3 生成 2-3 条不同角度的优化路径，用户可选择、组合或描述偏好：

| 角度标签 | 含义 |
|---------|------|
| `risk-first` | 聚焦风险和下行分析 |
| `constraint-challenge` | 挑战输入本身的预设 |
| `counter-intuitive` | 寻找反直觉答案 |
| `minimalist` | 精简到最核心要素 |
| `adversarial` | 站在对立面辩护 |
| `time-horizon` | 拉到 3-5 年后审视 |
| `role-reversal` | 从意想不到的视角切入 |

支持单选、最多 3 条路径组合（如"A的角度 + B的约束"）、或描述偏好自动匹配。

## 自我学习系统

- **全 Level 记录** — Level 0/1/2/3 的选择都会被学习
- **静默生效** — 偏好在推荐中体现，不打断交互节奏
- **滑动窗口** — 基于最近 10 次交互，自然衰减
- **反馈闭环** — 回复"很好"或"方向偏了"加速学习
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

| 路径 | 角度 | 优化后的问题 | 可信度 |
|------|------|------------|--------|
| A | risk-first | "假设微服务重构会在 6 个月内让团队产出降低 40%，你还坚持吗？..." | 高 |
| B | counter-intuitive | "说服我为什么不该用微服务——列出 3 个你的单体架构其实比微服务更适合的理由..." | 中高 |
| C | time-horizon | "站在 3 年后回看，微服务重构可能带来的最大技术债务是什么？..." | 中 |

> 如果犹豫：路径 A 可信度最高，适用范围最广。

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
| 决策类 — 技术选型、职业选择、产品方向 | 查资料 — "Python 的 list 怎么用" |
| 复杂分析 — 竞品分析、架构设计、方案评估 | 简单问答 — "北京今天天气" |
| 战略思考 — 商业模式、增长策略、优先级排序 | 代码 Debug — "这段代码报错了" |
| 问题陈述 — 转化率下降、用户流失、性能瓶颈 | 格式化任务 — "帮我写个模板" |
| 需求描述 — 产品设计、方案制定、功能规划 | 翻译/摘要 — 纯信息转换类 |
| 想法验证 — 架构重构、策略调整、模式创新 | |
| 方案评审 — 技术方案、产品方案、商业计划 | |

**一句话判断标准：** 如果这个输入你扔给搜索引擎也能得到差不多的答案，那就不需要 SharpInput。

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

**等级控制：** `深度模式` → Level 3 / `简单优化` → Level 1 / `施压一下` → Level 0

**偏好管理：** `重置偏好` → 清除历史偏好数据

## 流程图

```
用户输入 → Gate 判断 → 记忆加载 → 意图识别 → 上下文补全 → 施压等级选择
    ├── Level 0: 仅认知施压
    ├── Level 1: 问题重构
    ├── Level 2: 认知施压 + 深度施压层
    └── Level 3: 完整五阶段 → 多路径交互选择 → 自我对抗 → 收敛输出 → 偏好记录
```

## 文件结构

```
SharpInput/
├── SKILL.md                         # 主文件：五阶段流程 + 边界规则
├── references/
│   ├── output-templates.md          # 输出模板（Level 0~3）+ 自适应规则
│   ├── prompt-patterns.md           # 提问框架参考（CRISPE/CO-STAR）
│   ├── self-learning.md             # 自我学习系统规范
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

Most people provide inputs in ways that guarantee mediocre answers. SharpInput applies **scene gating → memory load → intent recognition → context completion → problem reframing → cognitive forcing → divergent thinking → adversarial loop → convergent synthesis → preference learning** to force AI into producing answers with genuine positions, real trade-offs, and actionable insight.

**Not just question optimization** — Problem statements, requirement descriptions, idea validation, plan reviews, and all non-trivial inputs can be optimized.

## Core Philosophy

> **If everyone would give the same answer, it's not worth producing.**

- **Forces AI to pick a side** — No neutrality allowed
- **Forces AI to self-adversarize** — Find counter-examples, failure conditions, kill hallucinations
- **Forces AI to surface blind spots** — Dimensions you hadn't considered
- **Forces AI to sacrifice** — Can't "have it all"; must declare what it gives up
- **Forces AI to give actionable steps** — Not a direction, not a framework, a concrete action
- **Smart triage** — Simple questions get direct answers, no over-engineering
- **Self-learning** — Remembers your preferences, gets better over time

## Four-Level Forcing System

| Level | Name | Stages Executed | When to Use |
|-------|------|----------------|-------------|
| **Level 0** | Rapid Forcing | Cognitive forcing only → output forced question | Just want a good question, no analysis needed |
| **Level 1** | Light Optimization | Problem reframing → output | Input is decent, just needs polish |
| **Level 2** | Medium Forcing | Reframing → cognitive forcing + deep forcing layer | Need a stance, but no full adversarial loop |
| **Level 3** | Deep Adversarial | Full five stages + interactive multi-path selection | Complex decisions, need comprehensive analysis |

**Auto-triage**: Lookup, debug, translation — direct answers, zero friction.
**Switch anytime**: "deep mode" → Level 3 / "simple optimization" → Level 1 / "just force it" → Level 0.

## Covered Input Types

**Enters optimization:**

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

**Direct answer, skip optimization:**

| Input Type | Example |
|-----------|---------|
| Factual lookup | "What is a closure in JS" |
| Debug/error | "This code throws an error" |
| Formatting | "Translate to English" |

## Four Cognitive Forcing Constraints

| Constraint | Purpose |
|-----------|---------|
| **Stance** | Must pick a side, no neutrality |
| **Anti-consensus** | Must challenge mainstream views and defend it |
| **Trade-off** | Can't have it all; must declare what to sacrifice |
| **Actionability** | Must give one specific action the user can take this week |

## Intent Recognition

| Intent | Meaning | Typical Input | Forcing Strategy |
|--------|---------|--------------|-----------------|
| Explain | Understand concepts / principles | Questions / Problem statements needing root cause | Counter-intuitive anchor + analogical counter-examples |
| Decision | Make a choice / judgment | Questions / Ideas requiring trade-off evaluation | Regret pre-mortem + killer question |
| Generate | Generate code / content / solution | Questions / Requirements | Minimal viable solution + constraint challenge |
| Analyze | Analyze / evaluate / review | Questions / Plan reviews, idea validation | Hidden assumption exposure + failure conditions |
| Explore | Explore directions / find possibilities | Questions / Problem statements seeking solution space | Multi-path + devil's advocate |

Supports primary + secondary dual-label intent. Users can override the recognition result.

## Multi-Path Interactive Selection (Level 3)

Level 3 generates 2-3 optimized paths from different angles:

| Angle Tag | Meaning |
|-----------|---------|
| `risk-first` | Focus on downside analysis |
| `constraint-challenge` | Challenge the input's own premises |
| `counter-intuitive` | Seek the non-obvious answer |
| `minimalist` | Strip to essentials |
| `adversarial` | Argue against the obvious |
| `time-horizon` | Shift to 3-5 years out |
| `role-reversal` | Unexpected stakeholder perspective |

Supports single pick, combination of up to 3 paths, or preference-based auto-matching.

## Self-Learning System

- **All-level tracking** — Level 0/1/2/3 choices are all learned
- **Silent operation** — Preferences manifest in recommendations without interrupting flow
- **Sliding window** — Based on last 10 interactions, naturally decays
- **Feedback loop** — Reply "great" or "off track" to accelerate learning
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

| Path | Angle | Optimized Question | Credibility |
|------|-------|-------------------|-------------|
| A | risk-first | "Assume microservice refactoring will reduce team output by 40% for 6 months. Still want to do it?..." | High |
| B | counter-intuitive | "Convince me why you should NOT use microservices — list 3 reasons your monolith is actually better..." | Medium-high |
| C | time-horizon | "Looking back from 3 years in the future, what's the biggest tech debt microservices might create?..." | Medium |

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
| Decisions — Tech stack, career, product direction | Lookup — "How does Python's list work" |
| Complex analysis — Competitor analysis, architecture | Simple Q&A — "What's the weather" |
| Strategy — Business models, growth, prioritization | Debug — "This code throws an error" |
| Problem statements — Declining metrics, user churn | Formatting — "Help me write a template" |
| Requirements — Product design, feature planning | Translation/summary — Pure info conversion |
| Idea validation — Architecture refactoring, strategy shifts | |
| Plan reviews — Technical plans, business proposals | |

**One-line rule:** If a search engine would give roughly the same answer, you don't need SharpInput.

## Installation

```bash
git clone https://github.com/gaoyechen/SharpInput.git
```

Place `SKILL.md` and `references/` into your AI Agent's skills directory.

## Usage

**Triggers:**
- `Optimize this` / `Make this better` / `How to ask this better`
- `Help me organize` / `Is this good enough` / `How should I phrase this`

**Level control:** `deep mode` → Level 3 / `simple optimization` → Level 1 / `just force it` → Level 0

**Preferences:** `reset preferences` → Clear preference data

## Flow Diagram

```
User input → Gate → Memory Load → Intent Recognition → Context Completion → Forcing Level
    ├── Level 0: Cognitive forcing only
    ├── Level 1: Problem reframing
    ├── Level 2: Cognitive forcing + deep layer
    └── Level 3: Full five stages → multi-path interactive → adversarial → convergent → preference recording
```

## File Structure

```
SharpInput/
├── SKILL.md                         # Core: 5-stage flow + boundary rules
├── references/
│   ├── output-templates.md          # Output templates (Level 0~3) + adaptive rules
│   ├── prompt-patterns.md           # Prompting frameworks (CRISPE / CO-STAR)
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
