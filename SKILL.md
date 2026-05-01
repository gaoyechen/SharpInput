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

Before entering any stage, classify the question through a **signal detection decision tree**. Execute steps in order; stop at the first definitive match.

#### Step 1: Signal Detection — Scan for these signals in the question

| Signal | Detection Keywords / Patterns | Examples |
|--------|------------------------------|----------|
| **Factual lookup** | "what is X", "how to use X", "X definition", "X syntax", single-concept questions | "What is a closure in JS" |
| **Debug / error** | Error messages, "why does this error", stack traces, "this code doesn't work" | "TypeError: Cannot read property" |
| **Formatting / conversion** | "convert", "format", "translate", "summarize", "rewrite this", "template" | "Translate this to English" |
| **Comparison signal** | "vs", "compared to", "which is better", "A or B", "difference between" | "React vs Vue" |
| **Decision signal** | "should I", "is it worth", "choose between", "decide", "trade-off", "pros and cons" | "Should I switch jobs" |
| **Analysis signal** | "analyze", "evaluate", "how is this plan", "why would X fail", "review" | "Analyze this architecture" |
| **Exploration signal** | "what directions", "what else", "any other options", "brainstorm", "explore" | "What are my options" |
| **Strategy signal** | "how should I approach", "long-term", "roadmap", "priority", "resource allocation" | "How should I scale my team" |

#### Step 2: Decision Tree

```
Question received
  │
  ├─ Has Factual lookup OR Debug/Formatting signal?
  │   └─ YES → 🟢 Quick Execution: Answer directly. Skip SharpAsk entirely.
  │
  ├─ Has Comparison/Decision/Analysis/Exploration/Strategy signal?
  │   ├─ Only 1 signal, no specific constraints (who/what/where/when)?
  │   │   └─ 🟡 Level 1 (Light Optimization): Clear direction, needs polish
  │   ├─ 1-2 signals + has specific constraints (role, scenario, tech stack, team size)?
  │   │   └─ 🔴 Level 2 (Medium Forcing): Has context, needs stance
  │   └─ 2+ signals OR contains "trade-off" / "risk" / "long-term" / "strategic"?
  │       └─ 🔴 Level 3 (Deep Adversarial): Complex decision, full analysis
  │
  └─ No clear signal detected
      └─ 🟡 Level 1 by default. Inform user:
         "I've classified this as light optimization. Say 'deep mode' for full analysis."
```

#### Step 3: Confidence & Escalation

After classification, assign a **confidence score** (High / Medium / Low):

- **High confidence**: Question clearly matches one signal category → proceed directly
- **Medium confidence**: Question matches multiple categories or has ambiguous signals → state your classification and proceed, but note: "If this feels wrong, say 'upgrade' to go deeper."
- **Low confidence**: No clear signal or contradictory signals → **ask the user before proceeding**:
  > "I'm not sure how to classify this. Is this more of a [option A] or [option B]? Or just say the level you want: Level 0/1/2/3."

**User override always takes priority**: If the user says "deep mode", "Level 3", "just optimize it", or any explicit level instruction, skip the decision tree and go directly to that level.

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

**Primary intent determines the main forcing strategy; secondary intent adds supplementary constraints.**

#### Mixed Intent Matrix (Primary × Secondary)

When two intents coexist, use this matrix to determine the combined forcing strategy:

| Primary → Secondary ↓ | 🧠 Explain | ⚖️ Decision | 🔨 Generate | 🔬 Analyze | 🧭 Explore |
|----------------------|-----------|-------------|-------------|-----------|-----------|
| **🧠 Explain** | — | Regret pre-mortem + Counter-intuitive anchor | Minimal viable solution + "Why this conceptual foundation?" | Hidden assumption exposure + Counter-intuitive anchor | Multi-path + "Explain each path's underlying mechanism" |
| **⚖️ Decision** | Counter-intuitive anchor + "Which choice does this imply?" | — | Minimal viable solution + Regret pre-mortem | Hidden assumption exposure + Regret pre-mortem | Multi-path + Regret pre-mortem (evaluate each path's regret) |
| **🔨 Generate** | Counter-intuitive anchor + Constraint challenge | Regret pre-mortem + Constraint challenge | — | Hidden assumption exposure + Constraint challenge | Multi-path + Minimal viable solution (simplify each path) |
| **🔬 Analyze** | Counter-intuitive anchor + Hidden assumption exposure | Regret pre-mortem + Hidden assumption exposure | Minimal viable solution + Hidden assumption exposure | — | Multi-path + Hidden assumption exposure |
| **🧭 Explore** | Counter-intuitive anchor + Devil's advocate | Regret pre-mortem + Devil's advocate | Minimal viable solution + Devil's advocate | Hidden assumption exposure + Devil's advocate | — |

**Tertiary intent handling**: If a third intent is clearly present, add only its **most distinctive constraint** (don't stack all three). Inform the user: "I'm also detecting [tertiary intent] — adding [specific constraint] as a supplementary layer."

**Intent conflict detection**: When primary and secondary strategies directly contradict (e.g., Explain wants to expand understanding while Generate wants to narrow to one solution), notify the user:
> "Your question has both 'understand' and 'build' dimensions. I recommend processing them in sequence: first explore the concept (Explain), then converge on a solution (Generate). Proceed this way?"

If the user declines, prioritize the primary intent and note the trade-off.

---

### Context Completion (After Intent Recognition, Before Stage 1)

**Goal: Fill in critical information the user didn't provide, preventing mediocre output based on incomplete input.**

> 📖 **Reference**: For structuring the output format and audience targeting of context-inferred questions, see `references/prompt-patterns.md` → **CO-STAR Framework** (Context/Objective/Style/Tone/Audience/Response). Use the Audience and Response elements to sharpen the context completion output.

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

> 📖 **Reference**: When diagnosing question flaws, cross-check against `references/prompt-patterns.md` → **Common Anti-Patterns** (vague request, too broad, hidden assumption, contradictory constraints, missing role, no format specified, over-constraining, assumed consensus). These 8 anti-patterns are the standard checklist for what's wrong with the original question.

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

> 📖 **Reference**: For role-setting and persona construction in forcing constraints, see `references/prompt-patterns.md` → **CRISPE Framework** (Capacity/Request/Insight/Style/Personality/Experiment). Use the Capacity element to craft more precise stance constraints.

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

> 📖 **Reference**: For consensus detection criteria and consensus-breaking techniques, see `references/prompt-patterns.md` → **Identifying Consensus Answers** and **Techniques to Break Consensus**. Use the 5 consensus traits as the diagnostic checklist; use the breaking techniques as the adjustment toolkit when consensus is 🔴.

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

> 📖 **Reference**: Before finalizing the output, verify it meets the quality bar in `references/prompt-patterns.md` → **5 Signals of a High-Quality Question** (clear success criteria, constraints present, context provided, output format specified, room for exploration). Each signal the optimized question satisfies = one quality point.

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

> 📖 All output templates (Level 0~3) and adaptive output rules are in `references/output-templates.md`. Read that file before rendering output.

**Level quick reference**:
| Level | Name | What to Output |
|-------|------|---------------|
| **0** | Rapid Forcing | Cognitive Forcing Version + Consensus Level |
| **1** | Light Optimization | Diagnosis + Optimized Question + Improvements |
| **2** | Medium Forcing | Intent + Diagnosis + Forcing Version + Dimensions + Warning |
| **3** | Deep Adversarial | Full template (default: summary mode, say "expand" for full) |

**Adaptive rules summary** (full details in `references/output-templates.md`):
- **Summary mode**: Level 3 defaults to compact (4 core sections); say "expand" for full
- **Progressive disclosure**: Say "stop" or "just give me the question" at any stage
- **Language adaptation**: Placeholders follow user's language
- **Focus mode**: Specify which sections to show

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

- `references/output-templates.md` — All output templates (Level 0~3) and adaptive output rules
- `references/prompt-patterns.md` — Read as needed:
  - CRISPE / CO-STAR prompting frameworks
  - Common anti-patterns and fixes
  - Consensus answer identification and breaking techniques
  - 5 signals of high-quality questions
