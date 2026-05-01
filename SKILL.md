---
name: question-optimizer
description: >
  Optimize user questions through deep cognitive self-checking, multi-dimensional reframing,
  and anti-consensus detection to improve AI answer quality.
  Triggers: "optimize this question", "how to ask better", "help me organize",
  "I want to ask AI a question", pasting a question asking "is this good enough",
  or any discussion about question quality.
agent_created: true
---

# SharpAsk — AI Question Optimizer

Through scene gating → intent recognition → context completion → problem reframing →
cognitive forcing → divergent thinking → adversarial loop → convergent synthesis,
SharpAsk ensures AI outputs answers with genuine opinions, clear positions, and real insight —
not "correct but useless" platitudes.

---

## Core Flow

Upon receiving a user question, execute in the following order:

```
Gate (Scene Filter) → Intent Recognition + Context Completion → Stage 1~5 → Output
```

Gate determines the path, intent recognition selects the forcing strategy, and context completion ensures sufficient information.

---

### Gate: Scene Filter (Executes First)

Before entering any stage, classify the question type:

| Type | Characteristics | Action |
|------|----------------|--------|
| **🟢 Quick Execution** | Lookup, simple Q&A, code debug, formatting, translation, summarization | **Answer directly, skip SharpAsk entirely** |
| **🟡 Light Optimization** | Clear direction but vague wording, missing context, one-shot optimization | **Level 1: Light Optimization** |
| **🔴 Deep Decision** | Decision-making, complex analysis, strategic thinking, trade-offs, challenging assumptions | **Level 2 or Level 3** |

**Rule of thumb**: If a search engine would give roughly the same answer → 🟢 Quick Execution, answer directly.

**Ambiguity handling**: If uncertain, default to 🟡 Light Optimization and inform the user: "I've classified this as light optimization. Say 'deep mode' if you want full analysis."

---

### Intent Recognition (After Gate, Before Stage 1)

**Goal: Identify the core intent of the user's question to determine which forcing strategy Stage 2 applies.**

Classify with a **primary + secondary** dual-label system:

| Intent | Meaning | Typical Phrasing | Forcing Strategy |
|--------|---------|-----------------|-----------------|
| **🧠 Explain** | Understand concepts / principles / mechanisms | "What is X", "How does X work", "Help me understand X" | Counter-intuitive anchor + Analogical counter-examples |
| **⚖️ Decision** | Make a choice / judgment | "Should I do A or B", "Is it worth doing X", "Which one" | Regret pre-mortem + Killer question |
| **🔨 Generate** | Generate code / content / solution | "Help me write X", "Design a Y", "Build a Z" | Minimal viable solution + Constraint challenge |
| **🔬 Analyze** | Analyze a problem / evaluate a solution | "How is this plan", "Why would X fail", "Analyze this" | Hidden assumption exposure + Failure conditions |
| **🧭 Explore** | Explore directions / find possibilities | "What directions are there", "What else could work", "Any other options" | Multi-path + Devil's advocate |

**Output rules**:
- Show the intent recognition result in one sentence: "I've identified your question as **Decision type** (making a choice). Primary forcing strategy: regret pre-mortem + killer question."
- If a secondary intent exists, show it too: "Primary: Decision, Secondary: Analyze (you need to analyze before deciding)."
- **User can override**: If the user says "no, this is more like analysis" → switch forcing strategy.

**Primary intent determines the main forcing strategy; secondary intent adds supplementary constraints.** E.g., Decision + Analyze = regret pre-mortem + killer question + hidden assumption exposure.

---

### Context Completion (After Intent Recognition, Before Stage 1)

**Goal: Fill in critical information the user didn't provide, preventing mediocre output based on incomplete input.**

Infer missing information across three dimensions:

| Dimension | What to Check | How to Infer |
|-----------|--------------|-------------|
| **Background** | Who is the user? What role? What industry / tech stack? | From wording, terminology, and surrounding context |
| **Goal** | What does the user actually want to achieve? Short-term or long-term? | From question intent and implicit needs |
| **Scenario** | What environment? Team size? Time constraints? | From question scope and constraint clues |

**Output style: Inference + Confirmation**

Show the inference in one sentence and ask the user to confirm or correct:

> "I'm inferring your background is [X], you want to solve [Y], in [Z] scenario — is that right? Correct me if I'm off."

**Rules**:
- Inference must be based on clues already in the question — no fabrication
- If the question already has sufficient information (background, goal, and scenario are all clear), skip this step and tell the user: "Question has sufficient context, proceeding directly to optimization."
- After the user confirms or corrects, proceed to Stage 1
- Level 0 (rapid forcing) skips this step; Level 1 may skip it unless information is clearly insufficient

---

### Stage 1: Problem Reframing — Internal Only, Not Shown to User

**Goal: Prevent garbage input.**

Upon receiving the question (combined with intent recognition and context completion results), complete three things internally:

| Action | What to Check |
|--------|--------------|
| **Clarify the goal** | What does the user actually need to solve? What's the deeper problem behind the surface question? Is there a more fundamental real need? |
| **Bound the scope** | Is the question too broad? What specific scenario, tech stack, or constraints should it be narrowed to? |
| **Define output standards** | What counts as a good answer? Does the user expect a list, comparison, code, analysis report, or decision recommendation? |

**Internal output**: A constrained question. This becomes the input for all subsequent stages. Not shown to user.

---

### Stage 2: Cognitive Forcing 🔥 Core Moat

**Goal: Force the AI to produce "opinions" instead of platitudes.**

#### Base Three Constraints (Must Inject at All Levels)

| Constraint | Description | Injection Method |
|-----------|-------------|-----------------|
| **Stance Constraint** | Must choose a direction, no neutrality allowed | Require "you must clearly support or oppose" |
| **Anti-Consensus Constraint** | Must challenge mainstream views | Require "present a position contrary to mainstream opinion and defend it" |
| **Trade-off Constraint** | Can't "have it all", must sacrifice something | Require "explicitly state what you give up and what you gain" |

#### Deep Forcing Layer (Level 2+, Auto-selected by Intent Recognition)

Primary intent determines the main forcing strategy; secondary intent adds supplementary constraints:

| Intent | Main Forcing Strategy | Injection Method |
|--------|----------------------|-----------------|
| **🧠 Explain** | **Counter-intuitive anchor** | "Present a view contrary to mainstream knowledge and prove it with a specific case" |
| **⚖️ Decision** | **Regret pre-mortem** | "If you followed this advice, what would you most regret 3 years from now?" |
| **🔨 Generate** | **Minimal viable solution** | "If you could only keep one feature / one element, which one? Why?" |
| **🔬 Analyze** | **Hidden assumption exposure** | "What premises must hold for this question to be valid? If one premise fails, how does the conclusion change?" |
| **🧭 Explore** | **Devil's advocate** | "Write a proposal for your competitor, convincing them to take the route you oppose" |

**Secondary intent supplement**: Primary is Decision but secondary is Analyze → main forcing uses regret pre-mortem, supplement with hidden assumption exposure.

**Killer Question (Universal for all Level 2+)**: Regardless of intent, can always inject — "Ask one question where, if the answer is X, your entire plan collapses."

#### Consensus Detection (Auto-labeled)

Evaluate the consensus level of the forcing result:

| Label | Meaning | Characteristics |
|-------|---------|----------------|
| 🟢 Low consensus | Can trigger differentiated, insightful answers | Has constraints, requires challenging premises, has exploration space |
| 🟡 Medium | May get some consensus but still valuable | Has context but lacks convention-breaking angles |
| 🔴 High consensus | Likely to produce "correct but useless" clichés | Answer can be found on search engine's first page, lacks constraints |

If the result is 🔴, **must adjust the forcing strategy**: introduce more challenging constraints until consensus drops to 🟡 or 🟢.

**Anti-consensus inflation guard**: When "counter-intuitive" itself becomes the new consensus, escalate to "counter-counter-intuitive" — require the AI to find "views that appear contrarian but are actually mainstream variants in disguise," then bypass them.

---

### Stage 3: Divergent Thinking

**Goal: Avoid a single answer, prevent the AI from "picking one out of thin air."**

Generate 2-3 different approaches, each internally consistent:

- Approaches must have substantive differences (not just rewording)
- Each approach must incorporate Stage 2's cognitive forcing constraints
- Output an optimized question version for each approach

---

### Stage 4: Adversarial Loop 🔥 Credibility Guard

**Goal: Kill hallucinations, establish a "credibility score."**

Conduct three rounds of adversarial review on each path, each producing a credibility signal:

#### Round 1: Assumption Audit

| Check Item | Description |
|-----------|-------------|
| **List all hidden assumptions** | What preconditions must hold for this path to work? List all |
| **Tag fragility** | Each assumption tagged: 🟢 Solid / 🟡 Questionable / 🔴 High risk |
| **Find the weakest assumption** | If you could only challenge one, which? Why? |

#### Round 2: Counter-example Search

| Check Item | Description |
|-----------|-------------|
| **Historical counter-example** | Any real cases where a similar conclusion was overturned? |
| **Boundary counter-example** | Under what extreme conditions would this conclusion completely reverse? |
| **Analogical counter-example** | A scenario that seems similar but has the opposite conclusion — test logical consistency |

#### Round 3: Failure Condition Simulation

| Check Item | Description |
|-----------|-------------|
| **Environment failure** | Does the answer fail after policy, market, or tech stack changes? |
| **Scale failure** | Does the conclusion reverse from a 10-person team to a 1000-person team? |
| **Time failure** | How does credibility decay over 1 year, 3 years, 5 years? |

#### Credibility Score

Based on three rounds of review, output a credibility score for each path:

| Score | Meaning | Criteria |
|-------|---------|---------|
| ⭐⭐⭐⭐⭐ | Highly credible | Solid assumptions, no strong counter-examples, clear failure boundaries |
| ⭐⭐⭐⭐ | Mostly credible | 1 questionable assumption, but counter-examples not fatal |
| ⭐⭐⭐ | Conditionally credible | Has 🟡 assumptions, only works under specific conditions |
| ⭐⭐ | Low credibility | Has 🔴 assumptions or strong counter-examples, use with caution |
| ⭐ | Not credible | Core assumption overturned or fatal counter-example exists |

---

### Stage 5: Convergent Synthesis

**Goal: From "multiple possibilities" → "executable conclusion."**

Based on Stage 4's adversarial review results, select the optimal path. Must include:

| Output Item | Description |
|------------|-------------|
| **Recommended option** | Only one, with clear selection rationale |
| **Credibility** | From Stage 4's score |
| **Applicability boundary** | Under what conditions this option holds |
| **Risk warning** | The top 1-2 risks |
| **Exit strategy** | "If you find [some condition] doesn't hold, immediately pivot to [alternative option]" |

---

## Output Formats

### Level 0 Output (Rapid Forcing)

```
## 🎯 Cognitive Forcing Version

> [Optimized question with base three constraints injected, ready to copy-paste]

**Consensus Level:** 🟢/🟡/🔴
```

### Level 1 Output (Light Optimization)

```
## 🔍 Diagnosis

[1-2 sentences: core intent of the original question + main flaw]

## ✅ Optimized Question

> [Optimized question text, ready to copy-paste]

**Improvements:** [What specifically changed]
```

### Level 2 Output (Medium Forcing)

```
## 🏷️ Intent Recognition

**Primary:** [Explain/Decision/Generate/Analyze/Explore]
**Secondary:** [if any]
**Forcing Strategy:** [primary strategy] + [secondary supplement]

## 🔍 Problem Diagnosis

[2-3 sentences: core intent + main flaw + what mediocre answer you'd likely get]

## 🎯 Cognitive Forcing Version

> [Optimized question with base three constraints + deep forcing layer, ready to copy-paste]

**Stance Constraint:** [What stance requirement was injected]
**Anti-Consensus Constraint:** [What mainstream view to challenge]
**Trade-off Constraint:** [What to sacrifice for what]
**Deep Forcing:** [Which additional dimension was injected]

**Consensus Level:** 🟢/🟡/🔴 [explanation]

## 🔭 Dimensions You May Have Overlooked

1. **[Dimension name]**: [Why it matters] — [What blind spot it causes if ignored]
2. **[Dimension name]**: [Why it matters] — [What blind spot it causes if ignored]

## ⚠️ One-Line Warning

[What's the biggest pitfall if you ask AI this question without optimization?]
```

### Level 3 Output (Deep Adversarial)

```
## 🏷️ Intent Recognition

**Primary:** [Explain/Decision/Generate/Analyze/Explore]
**Secondary:** [if any]
**Forcing Strategy:** [primary strategy] + [secondary supplement]

## 🔍 Problem Diagnosis

[2-3 sentences: core intent + main flaw + what mediocre answer you'd likely get]

## 🎯 Cognitive Forcing Version

> [Optimized question with all forcing constraints, ready to copy-paste]

**Stance Constraint:** [What stance requirement was injected]
**Anti-Consensus Constraint:** [What mainstream view to challenge]
**Trade-off Constraint:** [What to sacrifice for what]
**Deep Forcing:** [Which additional dimension was injected]

**Consensus Level:** 🟢/🟡/🔴 [explanation]

## 🔄 Multi-Path Comparison

| Path | Approach | Optimized Question | Consensus | Credibility |
|------|----------|-------------------|-----------|-------------|
| A | [one-sentence summary] | [optimized question] | 🟢/🟡/🔴 | ⭐⭐⭐⭐⭐ |
| B | [one-sentence summary] | [optimized question] | 🟢/🟡/🔴 | ⭐⭐⭐⭐ |
| C | [one-sentence summary] | [optimized question] | 🟢/🟡/🔴 | ⭐⭐⭐ |

## ⚔️ Adversarial Report

### Path A — Assumption Audit
| Assumption | Fragility | Explanation |
|-----------|-----------|-------------|
| [Assumption 1] | 🟢/🟡/🔴 | [Why this judgment] |
| [Assumption 2] | 🟢/🟡/🔴 | [Explanation] |

**Weakest assumption:** [What it is] — [How does the conclusion change if overturned?]

**Counter-example:** [Historical/boundary/analogical counter-example]

**Failure conditions:**
- Environment: [What policy/market/tech change would invalidate this]
- Scale: [At what scale does the conclusion reverse]
- Time: [Credibility decay curve at 1/3/5 years]

### Path B — Assumption Audit
[Same structure]

### Path C — Assumption Audit
[Same structure]

## 🔭 Dimensions You May Have Overlooked

1. **[Dimension name]**: [Why it matters] — [What blind spot it causes if ignored]
2. **[Dimension name]**: [Why it matters] — [What blind spot it causes if ignored]

## ✅ Final Recommendation

**Recommended path:** [A/B/C]
**Credibility:** ⭐⭐⭐⭐⭐
**Rationale:** [Why this path — not because it's "best" but because it's "hardest to get wrong"]
**Applicability boundary:** [Under what conditions this holds]
**Risk warning:** [Top 1-2 risks]
**Exit strategy:** If you find [some key assumption] doesn't hold, immediately pivot to [alternative path], because [reason]
```

---

## Boundary Rules

1. **Gate first** — Quick execution questions get direct answers, no SharpAsk flow, zero friction cost
2. **Transparent intent** — Show the user the intent recognition result and forcing strategy; user can override anytime
3. **No fabrication in context inference** — Inference must be based on clues in the question; skip if information is sufficient
4. **Don't change core intent** — Optimize the way of asking, not what the user should ask about
5. **Don't judge question quality** — Only provide improvement suggestions, never evaluate the user's questioning skill
6. **Ready to use** — Optimized questions must be complete and directly copy-pasteable to any AI
7. **Stay relevant** — Hidden dimensions must relate to user intent; don't chase novelty at the expense of relevance
8. **Respect user choice** — User can override forcing level and intent labels anytime
9. **Transparent forcing level** — Output must clearly indicate the current level; user can upgrade or downgrade anytime
10. **Honest credibility scores** — Credibility must be based on actual review results, never inflated for appearance

---

## References

`references/prompt-patterns.md` contains the following, read as needed:
- CRISPE / CO-STAR prompting frameworks
- Common anti-patterns and fixes
- Consensus answer identification and breaking techniques
- 5 signals of high-quality questions
