# Output Templates

Output templates for all SharpAsk forcing levels. Read this file when rendering output.

---

## Adaptive Output Rules

Templates below are the **default** format. Apply these adaptive rules:

**Summary mode (Level 3 default)**: Level 3 output is long. By default, render a **compact version**:
- Show only: Intent Recognition → Cognitive Forcing Version → Multi-Path table → Final Recommendation (4 sections)
- Collapse Adversarial Report and Dimensions into a one-line summary
- User can say "expand" or "full report" to see the complete version

**Progressive disclosure (all levels)**: If the user says "stop" or "just give me the question" at any stage, skip remaining stages and output whatever is ready.

**Language adaptation**: Output template placeholders (e.g., `[Dimension name]`, `[Why it matters]`) should follow the user's language. If the user writes in Chinese, use Chinese placeholders; if in English, use English.

**Focus mode**: If the user specifies a focus (e.g., "only show me the adversarial part" or "skip the diagnosis"), output only the requested sections.

---

## Level 0 Output (Rapid Forcing)

```
## 🎯 Cognitive Forcing Version

> [Optimized question with base three constraints injected, ready to copy-paste]

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

---

## Level 3 Output (Deep Adversarial)

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
