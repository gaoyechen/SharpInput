# Prompt Optimization Frameworks

## CRISPE Framework

| Element | Meaning | Example |
|---------|---------|---------|
| **C**apacity (Role) | What role does the AI play | "You are a senior frontend architect" |
| **R**equest (Task) | What specifically to do | "Help me design a component architecture" |
| **I**nsight (Context) | Relevant background info | "The project uses React + TypeScript, team of 3" |
| **S**tyle (Format) | Expected answer style | "Think like an engineer, give actionable plans" |
| **P**ersonality (Tone) | Answer personality | "Direct, no fluff, opinionated" |
| **E**xperiment (Variation) | Request multiple versions | "Give 2-3 options and compare pros/cons" |

---

## CO-STAR Framework

| Element | Meaning | When to Use |
|---------|---------|------------|
| **C**ontext | Provide background information | All questions benefit from this |
| **O**bjective | Clarify what the AI should do | Vague requests need anchoring |
| **S**tyle | Desired writing style | Content creation tasks |
| **T**one | Formal / casual / serious, etc. | When targeting different audiences |
| **A**udience | Who the answer is for | When depth needs customization |
| **R**esponse | List / table / code / essay, etc. | When structured output is needed |

---

## Common Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| **Vague request** | "Help me write a program" | Anchor language, functionality, input/output |
| **Too broad** | "Teach me programming" | Break into specific sub-topics, tackle one at a time |
| **Hidden assumption** | "How to increase conversion rate" | Expose the premise first: what's the current rate? Where's the bottleneck? |
| **Contradictory constraints** | "Be concise but comprehensive" | Clarify priority, choose one direction |
| **Missing role** | "What do you think of this plan" | From whose perspective? Tech? Product? CEO? |
| **No format specified** | "Tell me about X" | Table? Bullet list? Deep analysis? Quick summary? |
| **Over-constraining** | "Implement feature Y using framework X" | May block better solutions from being considered |
| **Assumed consensus** | "Follow best practices" | Whose best practices? Which community? Which version? |

---

## Identifying Consensus Answers

When a question is likely to produce consensus answers, it typically has these traits:

1. **Searchable** — If Google's first result answers it, the AI will give a similar answer
2. **Unconstrained** — Fewer constraints = answers converge on the "safe but mediocre" middle ground
3. **Premises unchallenged** — When premises aren't questioned, answers stay within the default framework
4. **Single perspective** — One angle of questioning = one angle of "standard answer"
5. **Single time horizon** — Only asks "what to do now", never "how does this look in 5 years" or "under what conditions does this fail"

### Techniques to Break Consensus

- Ask the AI to find the **weakest assumption** in its own answer
- Ask the AI to **make the strongest case for the opposite position**
- Add **specific scenario constraints** (time, budget, team size, tech stack)
- Require the answer to include **one counter-intuitive insight**
- Specify a **time horizon** ("Looking back from 3 years in the future")

---

## 5 Signals of a High-Quality Question

1. **Clear success criteria** — The user knows what counts as a "good" answer
2. **Constraints present** — Scope, style, depth, and audience are bounded
3. **Context provided** — The AI doesn't need to guess the background
4. **Output format specified** — It's clear what form the answer should take
5. **Room for exploration** — The AI is allowed to challenge assumptions and offer different perspectives
