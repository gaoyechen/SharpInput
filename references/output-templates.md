# Output Templates

Output templates for all SharpInput forcing levels. Read this file when rendering output.

---

## Adaptive Output Rules

Templates below are the **default** format. Apply these adaptive rules:

**Summary mode (Level 3 default)**: Level 3 output is long. By default, render a **compact version**:
- Show: Intent Recognition → Multi-Path table → Selection Prompt
- Collapse Adversarial Report into one-line credibility+key-risk per path
- Collapse Dimensions into a single combined list
- User can say "expand" or "full report" to see full adversarial analysis before selecting

**Progressive disclosure (all levels)**: If the user says "stop" or "just give me the question" at any stage, skip remaining stages and output whatever is ready.

**Language adaptation**: Output template placeholders (e.g., `[Dimension name]`, `[Why it matters]`) should follow the user's language. If the user writes in Chinese, use Chinese placeholders; if in English, use English.

**Focus mode**: If the user specifies a focus (e.g., "only show me the adversarial part" or "skip the diagnosis"), output only the requested sections.

---

## Level 0 Output (Rapid Forcing)

```
## 🎯 Cognitive Forcing Version

> [Optimized question with base four constraints injected (stance + anti-consensus + trade-off + actionability), ready to copy-paste]

**Consensus Level:** 🟢/🟡/🔴
```

---

## Level 1 Output (Light Optimization)

```
## 🔍 Diagnosis

[1-2 sentences: core intent of the original question + main flaw]

## ✅ Optimized Question

> [Optimized question text, ready to copy-paste]

**Improvements:** [What specifically changed]
```

---

## Level 2 Output (Medium Forcing)

```
## 🏷️ Intent Recognition

**Primary:** [Explain/Decision/Generate/Analyze/Explore]
**Secondary:** [if any]
**Forcing Strategy:** [primary strategy] + [secondary supplement]

## 🔍 Problem Diagnosis

[2-3 sentences: core intent + main flaw + what mediocre answer you'd likely get]

## 🎯 Cognitive Forcing Version

> [Optimized question with base four constraints + deep forcing layer, ready to copy-paste]

**Stance Constraint:** [What stance requirement was injected]
**Anti-Consensus Constraint:** [What mainstream view to challenge]
**Trade-off Constraint:** [What to sacrifice for what]
**Actionability Constraint:** [What concrete first step is required]
**Deep Forcing:** [Which additional dimension was injected]

**Consensus Level:** 🟢/🟡/🔴 [explanation]

## 🔭 Dimensions You May Have Overlooked

1. **[Dimension name]**: [Why it matters] — [What blind spot it causes if ignored]
2. **[Dimension name]**: [Why it matters] — [What blind spot it causes if ignored]

## ⚠️ One-Line Warning

[What's the biggest pitfall if you ask AI this question without optimization?]
```

---

## Level 3 Output (Deep Adversarial)

Level 3 has three output phases: **Phase 1** (Analysis) is shown automatically, **Phase 2** (Selection Prompt) follows immediately, and **Phase 3** (Final Output) is shown after the user selects or combines a path.

### Phase 1: Analysis

```
## 🏷️ Intent Recognition

**Primary:** [Explain/Decision/Generate/Analyze/Explore]
**Secondary:** [if any]
**Forcing Strategy:** [primary strategy] + [secondary supplement]

## 🔍 Problem Diagnosis

[2-3 sentences: core intent + main flaw + what mediocre answer you'd likely get]

## 🔄 Multi-Path Comparison

| Path | Angle | Approach | Optimized Question | Consensus | Credibility |
|------|-------|----------|-------------------|-----------|-------------|
| A | [angle tag from vocabulary] | [one-sentence summary] | [full optimized question] | 🟢/🟡/🔴 | ⭐⭐⭐⭐⭐ |
| B | [angle tag from vocabulary] | [one-sentence summary] | [full optimized question] | 🟢/🟡/🔴 | ⭐⭐⭐⭐ |
| C | [angle tag from vocabulary] | [one-sentence summary] | [full optimized question] | 🟢/🟡/🔴 | ⭐⭐⭐ |

> Each path's optimized question already incorporates all forcing constraints (stance, anti-consensus, trade-off, actionability, deep forcing). The Angle column shows the path's distinctive perspective from the standard vocabulary.

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
```

### Phase 2: Selection Prompt

```
## 🎯 Choose Your Path

Pick a path, combine elements, or describe what you prefer:

- **A** — [one-line summary of path A's angle]
- **B** — [one-line summary of path B's angle]
- **C** — [one-line summary of path C's angle]
- **Combine** — e.g., "A's angle + B's constraint" (max 3 paths)

💡 If undecided: Path [X] has the highest credibility ([score]) and broadest applicability.
```

### Phase 3: Final Output (after user selection)

```
## ✅ Final Optimized Question

**Selected:** [Path X / Combination description]

> [Full polished question — clean, no meta-commentary, ready to copy-paste into any AI]

**Embedded constraints:**
- [Stance Constraint — what position was forced]
- [Anti-Consensus Constraint — what mainstream view was challenged]
- [Trade-off Constraint — what was sacrificed for what]
- [Actionability Constraint — what concrete first step was demanded]

**Best used when:** [Applicability boundary]
**Watch out for:** [Top risk]
**If the answer feels off, pivot by asking:** "[Follow-up question]"

---
拿到回答后，如果方向不对回复「方向偏了」；如果很好回复「很好」。
```
