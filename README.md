# 🔥 SharpAsk — AI Question Optimizer

> A cognitive forcing framework that transforms your AI answers from "correct platitudes" into "opinionated insights."

**English** | [中文](./README_CN.md)

Most people ask questions in ways that guarantee mediocre answers. SharpAsk applies **scene gating → intent recognition → context completion → problem reframing → cognitive forcing → divergent thinking → adversarial loop → convergent synthesis** to force AI into producing answers with genuine positions, real trade-offs, and actionable insight — not textbook bullet points.

---

## ⚡ Core Philosophy

> **If everyone would give the same answer, it's not worth producing.**

SharpAsk doesn't help you "word your question better." It:

- 🎯 **Forces AI to pick a side** — No neutrality allowed
- ⚔️ **Forces AI to self-adversarize** — Find counter-examples, failure conditions, kill its own hallucinations
- 🔭 **Forces AI to surface blind spots** — Dimensions you yourself hadn't considered
- 🚫 **Forces AI to sacrifice** — Can't "have it all"; must declare what it gives up
- 🚦 **Smart triage** — Simple questions get direct answers, no over-engineering

---

## 🚦 Four-Level Forcing System

SharpAsk doesn't treat all questions equally. It classifies the question first, then selects the appropriate forcing depth:

| Level | Name | Stages Executed | When to Use |
|-------|------|----------------|-------------|
| **Level 0** | Rapid Forcing | Cognitive forcing only → output forced question | Just want a good question, no analysis needed |
| **Level 1** | Light Optimization | Problem reframing → output | Question is decent, just needs polish |
| **Level 2** | Medium Forcing | Reframing → cognitive forcing + deep forcing layer | Need a stance, but no full adversarial loop |
| **Level 3** | Deep Adversarial | Full five stages | Complex decisions, need comprehensive analysis |

**Auto-triage**: Lookup, debug, translation, and other simple questions get direct answers — zero friction.

**Switch anytime**: Say "deep mode" to jump to Level 3, "simple optimization" for Level 1, or "just force it" for Level 0.

---

## 🏷️ Intent Recognition

SharpAsk automatically identifies the core intent of your question to select the right forcing strategy:

| Intent | Meaning | Forcing Strategy |
|--------|---------|-----------------|
| 🧠 **Explain** | Understand concepts / principles | Counter-intuitive anchor + analogical counter-examples |
| ⚖️ **Decision** | Make a choice / judgment | Regret pre-mortem + killer question |
| 🔨 **Generate** | Generate code / content / solution | Minimal viable solution + constraint challenge |
| 🔬 **Analyze** | Analyze a problem / evaluate a solution | Hidden assumption exposure + failure conditions |
| 🧭 **Explore** | Explore directions / find possibilities | Multi-path + devil's advocate |

Supports **primary + secondary** dual-label intent. Users can override the recognition result.

---

## 🔮 Context Completion

User questions often lack critical information (background, goals, scenario). SharpAsk:

1. **Auto-infers** — Extracts implicit background / goals / scenario from the question
2. **Confirms** — "I'm inferring your background is [X], you want to solve [Y], in [Z] scenario — correct?"
3. **User corrects** — Just say "yes" or fix one point, much faster than answering three separate questions

Automatically skipped when information is sufficient — zero friction.

---

## 📖 Before vs After

### Example 1: Learning Efficiency (Level 2 — Medium Forcing)

**Original question:**
> How to improve learning efficiency?

**Typical AI answer:**
> 1. Make a reasonable study plan
> 2. Get enough sleep
> 3. Use the Pomodoro technique
> 4. Take good notes and review regularly
> 5. Maintain a good study environment
>
> (👆 Content from the first page of any search engine — any AI would give a similar answer)

---

**SharpAsk output:**

> 🎯 **Cognitive Forcing Version:**
>
> You are a cognitive science researcher and a critic of "efficiency-ism." I have 3 hours of study time per day, and my goal is to pass the System Architect certification exam in 6 months.
>
> Pick a position: **deep learning (slow but solid) or exam cramming (fast but shallow)?** "Both" is not allowed.
>
> You must sacrifice the core advantage of one approach to gain the benefit of the other. State explicitly what you're giving up.
>
> Present a view that contradicts mainstream learning methodology and defend it.

> 🔭 **Dimensions you may have overlooked:**
> 1. **"Learning efficiency" itself may be a false premise** — If the exam tests breadth over depth, "efficiency" means something completely different
> 2. **The upside of forgetting** — Moderate forgetting actually strengthens memory; "review everything" might be the worst strategy

---

### Example 2: Tech Stack Decision (Level 3 — Deep Adversarial)

**Original question:**
> React vs Vue — which is better?

**Typical AI answer:**
> React's strengths are a rich ecosystem, large community, flexible JSX… Vue's strengths are a gentle learning curve, intuitive template syntax… The choice depends on your project requirements.
>
> (👆 The classic "both are good, it depends" non-answer)

---

**SharpAsk output:**

> 🎯 **Cognitive Forcing Version:**
>
> You are a frontend tech lead with 5 years of experience. Your team of 4 includes 2 who only know jQuery. The project is a toB admin dashboard that needs to be maintained for 3+ years.
>
> You **must choose one framework**. "Both have pros and cons" or "it depends" are not allowed.
>
> Give a **counter-intuitive reason** for your choice (not "good ecosystem" or "easy to learn" — those are consensus opinions).
>
> State the **biggest strength of the framework you rejected** and explain why you think that strength doesn't matter in this scenario.

> ⚔️ **Adversarial check:**
> - Weakest assumption: Assuming "low learning cost" equals "low long-term maintenance cost"
> - Counter-example: jQuery teams migrating to Vue see short-term gains, but Vue 3's Composition API rewrite steepened the learning curve dramatically
> - Failure condition: If the project later requires extensive custom rendering logic, React's JSX flexibility advantage reverses

---

### Example 3: Career Decision (Level 3 — Deep Adversarial)

**Original question:**
> Should I change jobs?

**Typical AI answer:**
> Before changing jobs, consider: salary increase, career growth, team culture, company prospects… We recommend a comprehensive evaluation before deciding.
>
> (👆 That's saying absolutely nothing)

---

**SharpAsk output:**

> 🎯 **Cognitive Forcing Version:**
>
> I've been a product manager at a mid-size toG company for 3 years, earning 15% below market, but I've accumulated industry expertise. Now I have a big-tech offer with a 30% salary bump, but in a completely different domain.
>
> **You must answer clearly: switch or stay.** "It depends on your circumstances" is not allowed.
>
> Give me a risk that **most people wouldn't think of**.
>
> Tell me: if I follow your advice, **what will I most likely regret 3 years from now?**

> 🔭 **Dimensions you may have overlooked:**
> 1. **Depreciation rate of industry expertise** — toG product experience may have far less market value at big tech than you think
> 2. **Future you ≠ current you** — Your "industry expertise" today could become "path dependency" tomorrow, limiting your future choices

---

## ✅ When to Use

| Great Fit | Poor Fit |
|-----------|----------|
| 🧠 **Decisions** — Tech stack, career, product direction | 📚 **Lookup** — "How does Python's list work" |
| 🔬 **Complex analysis** — Competitor analysis, architecture design, plan evaluation | ❓ **Simple Q&A** — "What's the weather in Beijing" |
| 🎯 **Strategy** — Business models, growth strategy, prioritization | 🔧 **Debug** — "This code throws an error" |
| 🤔 **Deep learning** — Understanding concepts, comparing methodologies | 📝 **Formatting** — "Help me write a template" |
| 💡 **Creative exploration** — Brainstorming, challenging assumptions | 📖 **Translation/summary** — Pure information conversion |

**One-line rule:** If a search engine would give roughly the same answer, you don't need SharpAsk.

---

## 🚀 Installation

### Option 1: Git Clone

```bash
git clone https://github.com/gaoyechen/SharpAsk.git
```

Place `SKILL.md` and `references/` into your AI Agent's skills directory.

### Option 2: Manual Install

Copy `SKILL.md` and `references/prompt-patterns.md` to your agent's skill directory:

```
your-agent-skills/SharpAsk/
├── SKILL.md
└── references/
    └── prompt-patterns.md
```

---

## 📋 Usage

After installation, use these trigger phrases in conversation:

- `Optimize this question: [your question]`
- `How to ask this better`
- `I want to ask AI a question, help me organize it`
- `Is this question good enough: [your question]`

### Forcing Level Control

- **Default**: AI auto-classifies the question and selects the appropriate level
- `Deep mode` — Force Level 3, full five stages
- `Simple optimization` — Level 1, problem reframing only

### Output Content

| Level | Output |
|-------|--------|
| **Level 1** | Diagnosis + optimized question + improvements |
| **Level 2** | Diagnosis + cognitive forcing version + hidden dimensions |
| **Level 3** | Diagnosis + cognitive forcing version + multi-path comparison + adversarial report + hidden dimensions + final recommendation |

---

## 🧠 Flow Diagram

```
User question
    ↓
🚦 Gate: Quick execution? ──→ Yes ──→ Answer directly, done
    │ No
    ↓
🏷️ Intent Recognition (Explain / Decision / Generate / Analyze / Explore)
    ↓
🔮 Context Completion: Infer missing background / goals / scenario → Confirm
    ↓
Forcing Level Selection
    ├── Level 0: Cognitive forcing only → output forced question
    ├── Level 1: Problem reframing → output optimized question
    ├── Level 2: Reframing → cognitive forcing (with intent-adapted deep layer)
    └── Level 3: Full five stages → multi-path → adversarial → convergent output
                                                              ↓
                                                        Final recommendation + credibility score
```

---

## 📁 File Structure

```
SharpAsk/
├── SKILL.md                         # Core: Gate + intent + context + 5 stages + output templates
├── references/
│   └── prompt-patterns.md           # Prompting frameworks (CRISPE / CO-STAR)
├── README.md                        # English README (this file)
├── README_CN.md                     # 中文 README
└── LICENSE                          # MIT License
```

---

## 📄 License

MIT — use it, modify it, share it.

---

> **Ask sharp, answer deep.** — SharpAsk
