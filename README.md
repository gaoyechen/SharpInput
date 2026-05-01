# 🔥 SharpAsk — AI 提问优化器 / Question Optimizer

> 智能提问优化框架，让你的 AI 回答从"正确废话"变成"有洞察力的观点"。
>
> A cognitive forcing framework that transforms your AI answers from "correct platitudes" into "opinionated insights."

**[中文](#-sharpask--ai-提问优化器)** | **[English](#-sharpask--ai-question-optimizer)**

---

# 🔥 SharpAsk — AI 提问优化器

大多数人的提问方式，注定了 AI 只能给出中庸答案。SharpAsk 通过 **场景判断 → 意图识别 → 上下文补全 → 问题重构 → 认知施压 → 多路径生成 → 自我对抗 → 收敛输出**，强制 AI 产生立场、权衡和洞察，而非罗列教科书常识。

## ⚡ 核心理念

> **如果所有人都会给出同样的答案，那它不值得作为核心输出。**

SharpAsk 不是帮你"把问题写得更漂亮"，而是：

- 🎯 **逼 AI 选边站** — 不能中立，必须有立场
- ⚔️ **逼 AI 自我对抗** — 找反例、找失效条件、打掉幻觉
- 🔭 **逼 AI 挖掘盲区** — 列出你自己都没想到的维度
- 🚫 **逼 AI 放弃"全都要"** — 必须明确放弃什么来换取什么
- 🚦 **智能分流** — 简单问题直接答，不走过度流程

## 🚦 四级施压系统

| 等级 | 名称 | 执行阶段 | 适用场景 |
|------|------|---------|---------|
| **Level 0** | 极速施压 | 仅认知施压 → 输出施压版问题 | 只想要一个好问题，不需要分析 |
| **Level 1** | 轻度优化 | 问题重构 → 输出 | 问题质量不错，只需微调表述 |
| **Level 2** | 中度施压 | 问题重构 → 认知施压 + 深度施压层 | 需要有立场，但不需要完整对抗 |
| **Level 3** | 深度对抗 | 完整五阶段 | 复杂决策、需要全面分析 |

**自动分流**：查资料、Debug、翻译等简单问题直接回答，零摩擦。
**随时切换**：说"深度模式"升级到 Level 3，说"简单优化"降到 Level 1，说"施压一下"用 Level 0。

## 🏷️ 意图识别

| 意图 | 含义 | 施压策略 |
|------|------|---------|
| 🧠 **Explain** | 理解概念/原理 | 反直觉锚点 + 类比反例 |
| ⚖️ **Decision** | 做出选择/判断 | 后悔预判 + 杀手问题 |
| 🔨 **Generate** | 生成代码/内容/方案 | 最简方案 + 约束挑战 |
| 🔬 **Analyze** | 分析问题/评估方案 | 隐含假设暴露 + 失效条件 |
| 🧭 **Explore** | 探索方向/寻找可能 | 多路径 + 反面辩护 |

支持**主意图 + 次意图**双标签。用户可覆盖识别结果。

## 🔮 上下文补全

1. **自动推断** — 从问题中提取隐含的背景/目标/场景
2. **展示确认** — "我推测你是 [X]，想解决 [Y]，在 [Z] 场景下，对吗？"
3. **用户修正** — 只需说"对"或纠正一个点

## 📖 Before vs After

### 示例 1：学习效率（Level 2）

**原问题：**
> 如何提高学习效率？

**普通 AI 回答：**
> 1. 制定合理的学习计划 2. 保持充足的睡眠 3. 采用番茄工作法 4. 做好笔记和复习 5. 保持良好的学习环境
> （👆 搜索引擎第一页的内容，任何 AI 都会给出类似答案）

**SharpAsk 输出：**
> 🎯 **认知施压版问题：**
> 你是一位认知科学研究员，同时也是"效率至上主义"的批评者。我每天可用学习时间 3 小时，目标是在 6 个月内通过软考架构师考试。
> 请明确选择一个立场：**深度学习（慢但扎实）还是应试冲刺（快但浅薄）？** 不允许说"两者结合"。
> 必须放弃其中一个方向的核心优势来换取另一个方向的收益，明确说明你放弃了什么。
> 给出一个与"主流学习方法论"相反的观点，并为其辩护。

### 示例 2：技术选型（Level 3）

**原问题：**
> React 和 Vue 哪个好？

**SharpAsk 输出：**
> 🎯 **认知施压版问题：**
> 你是一个有 5 年经验的前端技术负责人，团队 4 人，其中 2 人只熟悉 jQuery。项目是一个需要维护 3 年以上的 toB 后台管理系统。
> 请**必须选择一个框架**，不允许说"各有优劣"或"取决于场景"。
> 为你的选择给出一个**反直觉的理由**。
> 明确说出你**放弃的那个框架的最大优势**，以及你为什么认为这个优势在当前场景下不重要。

### 示例 3：职业决策（Level 3）

**原问题：**
> 我应该跳槽吗？

**SharpAsk 输出：**
> 🎯 **认知施压版问题：**
> 我在一家中型 toG 公司做了 3 年产品经理，薪资低于市场 15%，但积累了行业经验。现在有一家大厂 offer，薪资涨 30%，但方向完全不同。
> **必须明确回答：跳还是不跳。** 不允许"需要综合考虑"。
> 为你的建议给出一个**大多数人不会考虑的风险**。
> 告诉我：如果我按你的建议做了，**3 年后最可能后悔的是什么？**

## ✅ 适用场景

| 适合 | 不适合 |
|------|--------|
| 🧠 决策类问题 — 技术选型、职业选择、产品方向 | 📚 查资料 — "Python 的 list 怎么用" |
| 🔬 复杂分析 — 竞品分析、架构设计、方案评估 | ❓ 简单问答 — "北京今天天气" |
| 🎯 战略思考 — 商业模式、增长策略、优先级排序 | 🔧 代码 Debug — "这段代码报错了" |
| 🤔 深度学习 — 理解概念本质、对比方法论 | 📝 格式化任务 — "帮我写个模板" |
| 💡 创意探索 — 找灵感、开拓思路、挑战假设 | 📖 翻译/摘要 — 纯信息转换类 |

**一句话判断标准：** 如果这个问题你扔给搜索引擎也能得到差不多的答案，那就不需要 SharpAsk。

## 🚀 安装

```bash
git clone https://github.com/gaoyechen/SharpAsk.git
```

将 `SKILL.md` 和 `references/` 目录放入你的 AI Agent 的 skills 目录中。

## 📋 使用方式

触发词：`帮我优化这个问题` / `怎么问才能得到更好的回答` / `我想问 AI 一个问题，帮我组织一下` / `这样问行不行`

等级控制：`深度模式` → Level 3 / `简单优化` → Level 1 / `施压一下` → Level 0

## 🧠 流程图

```
用户问题 → 🚦 Gate 判断 → 🏷️ 意图识别 → 🔮 上下文补全 → 施压等级选择
    ├── Level 0: 仅认知施压
    ├── Level 1: 问题重构
    ├── Level 2: 认知施压 + 深度施压层
    └── Level 3: 完整五阶段 → 多路径 → 自我对抗 → 收敛输出 → 最终推荐
```

## 📁 文件结构

```
SharpAsk/
├── SKILL.md                         # 主文件：五阶段流程 + 输出模板
├── references/
│   └── prompt-patterns.md           # 提问框架参考（CRISPE/CO-STAR）
├── README.md                        # 本文件
└── LICENSE                          # MIT License
```

## 📄 License

MIT — 随便用，随便改，随便分享。

---

> **问得锐，答得深。** — SharpAsk

---

# 🔥 SharpAsk — AI Question Optimizer

Most people ask questions in ways that guarantee mediocre answers. SharpAsk applies **scene gating → intent recognition → context completion → problem reframing → cognitive forcing → divergent thinking → adversarial loop → convergent synthesis** to force AI into producing answers with genuine positions, real trade-offs, and actionable insight — not textbook bullet points.

## ⚡ Core Philosophy

> **If everyone would give the same answer, it's not worth producing.**

SharpAsk doesn't help you "word your question better." It:

- 🎯 **Forces AI to pick a side** — No neutrality allowed
- ⚔️ **Forces AI to self-adversarize** — Find counter-examples, failure conditions, kill hallucinations
- 🔭 **Forces AI to surface blind spots** — Dimensions you yourself hadn't considered
- 🚫 **Forces AI to sacrifice** — Can't "have it all"; must declare what it gives up
- 🚦 **Smart triage** — Simple questions get direct answers, no over-engineering

## 🚦 Four-Level Forcing System

| Level | Name | Stages Executed | When to Use |
|-------|------|----------------|-------------|
| **Level 0** | Rapid Forcing | Cognitive forcing only → output forced question | Just want a good question, no analysis needed |
| **Level 1** | Light Optimization | Problem reframing → output | Question is decent, just needs polish |
| **Level 2** | Medium Forcing | Reframing → cognitive forcing + deep forcing layer | Need a stance, but no full adversarial loop |
| **Level 3** | Deep Adversarial | Full five stages | Complex decisions, need comprehensive analysis |

**Auto-triage**: Lookup, debug, translation — direct answers, zero friction.
**Switch anytime**: "deep mode" → Level 3 / "simple optimization" → Level 1 / "just force it" → Level 0.

## 🏷️ Intent Recognition

| Intent | Meaning | Forcing Strategy |
|--------|---------|-----------------|
| 🧠 **Explain** | Understand concepts / principles | Counter-intuitive anchor + analogical counter-examples |
| ⚖️ **Decision** | Make a choice / judgment | Regret pre-mortem + killer question |
| 🔨 **Generate** | Generate code / content / solution | Minimal viable solution + constraint challenge |
| 🔬 **Analyze** | Analyze a problem / evaluate a solution | Hidden assumption exposure + failure conditions |
| 🧭 **Explore** | Explore directions / find possibilities | Multi-path + devil's advocate |

Supports **primary + secondary** dual-label intent. Users can override the recognition result.

## 🔮 Context Completion

1. **Auto-infers** — Extracts implicit background / goals / scenario from the question
2. **Confirms** — "I'm inferring your background is [X], you want to solve [Y], in [Z] scenario — correct?"
3. **User corrects** — Just say "yes" or fix one point

## 📖 Before vs After

### Example 1: Learning Efficiency (Level 2)

**Original:**
> How to improve learning efficiency?

**Typical AI answer:**
> 1. Make a reasonable study plan 2. Get enough sleep 3. Use Pomodoro 4. Take notes and review 5. Good study environment
> (👆 First page of any search engine — any AI would give the same answer)

**SharpAsk output:**
> 🎯 **Cognitive Forcing Version:**
> You are a cognitive science researcher and a critic of "efficiency-ism." I have 3 hours of study time per day, goal: pass the System Architect exam in 6 months.
> Pick a position: **deep learning (slow but solid) or exam cramming (fast but shallow)?** "Both" is not allowed.
> You must sacrifice the core advantage of one approach to gain the benefit of the other. State explicitly what you're giving up.
> Present a view that contradicts mainstream learning methodology and defend it.

### Example 2: Tech Stack Decision (Level 3)

**Original:**
> React vs Vue — which is better?

**SharpAsk output:**
> 🎯 **Cognitive Forcing Version:**
> You are a frontend tech lead with 5 years of experience. Team of 4, 2 only know jQuery. Project: toB admin dashboard, 3+ year maintenance.
> You **must choose one framework**. "Both have pros and cons" is not allowed.
> Give a **counter-intuitive reason** for your choice (not "good ecosystem" or "easy to learn").
> State the **biggest strength of the framework you rejected** and explain why it doesn't matter here.

### Example 3: Career Decision (Level 3)

**Original:**
> Should I change jobs?

**SharpAsk output:**
> 🎯 **Cognitive Forcing Version:**
> I've been a PM at a mid-size toG company for 3 years, earning 15% below market. Now I have a big-tech offer with 30% salary bump, completely different domain.
> **You must answer: switch or stay.** "It depends" is not allowed.
> Give me a risk that **most people wouldn't think of**.
> Tell me: if I follow your advice, **what will I most likely regret 3 years from now?**

## ✅ When to Use

| Great Fit | Poor Fit |
|-----------|----------|
| 🧠 Decisions — Tech stack, career, product direction | 📚 Lookup — "How does Python's list work" |
| 🔬 Complex analysis — Competitor analysis, architecture | ❓ Simple Q&A — "What's the weather" |
| 🎯 Strategy — Business models, growth, prioritization | 🔧 Debug — "This code throws an error" |
| 🤔 Deep learning — Concepts, comparing methodologies | 📝 Formatting — "Help me write a template" |
| 💡 Creative exploration — Brainstorming, challenging assumptions | 📖 Translation/summary — Pure info conversion |

**One-line rule:** If a search engine would give roughly the same answer, you don't need SharpAsk.

## 🚀 Installation

```bash
git clone https://github.com/gaoyechen/SharpAsk.git
```

Place `SKILL.md` and `references/` into your AI Agent's skills directory.

## 📋 Usage

Triggers: `Optimize this question` / `How to ask this better` / `I want to ask AI a question, help me organize it` / `Is this question good enough`

Level control: `deep mode` → Level 3 / `simple optimization` → Level 1 / `just force it` → Level 0

## 🧠 Flow Diagram

```
User question → 🚦 Gate → 🏷️ Intent Recognition → 🔮 Context Completion → Forcing Level
    ├── Level 0: Cognitive forcing only
    ├── Level 1: Problem reframing
    ├── Level 2: Cognitive forcing + deep layer
    └── Level 3: Full five stages → multi-path → adversarial → convergent → final recommendation
```

## 📁 File Structure

```
SharpAsk/
├── SKILL.md                         # Core: 5-stage flow + output templates
├── references/
│   └── prompt-patterns.md           # Prompting frameworks (CRISPE / CO-STAR)
├── README.md                        # This file
└── LICENSE                          # MIT License
```

## 📄 License

MIT — use it, modify it, share it.

---

> **Ask sharp, answer deep.** — SharpAsk
