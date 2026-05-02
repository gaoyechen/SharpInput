# Output Templates

Output templates for all SharpInput forcing levels. Read this file before rendering output.

> [!] **GOLDEN RULE**: All selection prompts (path selection, intent clarification, parameter collection) **MUST use the `AskUserQuestion` tool**. **NEVER** output text-based "A / B / C" options — they are NOT clickable. Only a tool call produces an interactive dialog.

---

## Adaptive Output Rules

Templates below are the **default** format. Apply these adaptive rules:

**Level display (mandatory)**: Every output must start with the current Level on its own line: `[Level 0]` / `[Level 1]` / `[Level 2]` / `[Level 3]`. This lets the user know which level they're at and whether to upgrade.

**Level 3 output structure (Level 3 default)**: Level 3 output is structured as:
- Level →  →  → A + → B → C →  → 
- **No comparison table** — each path is presented independently with its own optimized question and credibility summary
- User can select one or multiple paths via multi-select dialog
- User can say "expand" to see full adversarial analysis before selecting

**Progressive disclosure (all levels)**: If the user says "stop" or "just give me the question" at any stage, skip remaining stages and output whatever is ready.

**Language adaptation**: Output template placeholders should follow the user's language. If the user writes in Chinese, use Chinese placeholders; if in English, use English.

**Focus mode**: If the user specifies a focus (e.g., "only show me the adversarial part" or "skip the diagnosis"), output only the requested sections.

---

## Level 0 Output (Rapid Forcing)

```
[Level 0]

> [Optimized question with base four constraints injected (stance + anti-consensus + trade-off + actionability), ready to copy-paste]

Consensus Level: [low/medium/high]
 Level 1~3
```

---

## Level 1 Output (Light Optimization)

```
[Level 1]

: [1-2 sentences: core intent + main flaw]

:
> [Optimized question text, ready to copy-paste]

: [What specifically changed]
 Level 2/3
```

---

## Level 2 Output (Medium Forcing)

```
[Level 2]

: [Explain/Decision/Generate/Analyze/Explore]
: [primary strategy] + [secondary supplement]

: [2-3 sentences: core intent + main flaw + what mediocre answer you'd likely get]

:
> [Optimized question with base four constraints + deep forcing layer, ready to copy-paste]

:
- : [what stance was forced]
- : [what mainstream view to challenge]
- : [what to sacrifice for what]
- : [what concrete first step is required]
- : [which additional dimension was injected]

: [low/medium/high]

:
1. [Dimension]: [why it matters]
2. [Dimension]: [why it matters]

: [biggest pitfall without optimization]
 Level 3
```

---

## Level 3 Output (Deep Adversarial)

Level 3 has two phases: **Phase 1** (Analysis + Paths + Selection) is shown in one go, and **Phase 2** (Final Output) is shown after the user selects paths.

### Phase 1: Analysis + Paths + Selection (Single Output)

The output follows this **strict order**: Level →  →  → A → B → C →  → 

**Do NOT show a comparison table.** Each path is presented independently with its own full optimized question and one-line credibility summary. The credibility tag and key risk are embedded inline under each path.

```
[Level 3]

: [2-3 sentences: core intent + main flaw + what mediocre answer you'd likely get]

: [Explain/Decision/Generate/Analyze/Explore]
: [primary strategy] + [secondary supplement]

 A — [angle tag]:
> [Full optimized question for path A, self-contained, ready to copy-paste]
: [***** ~ *] — [one-line key risk or weakest assumption]

 B — [angle tag]:
> [Full optimized question for path B, self-contained, ready to copy-paste]
: [***** ~ *] — [one-line key risk or weakest assumption]

 C — [angle tag]:
> [Full optimized question for path C, self-contained, ready to copy-paste]
: [***** ~ *] — [one-line key risk or weakest assumption]

:
1. [Dimension]: [why it matters]
2. [Dimension]: [why it matters]
```

**Immediately after** the text output, present the **AskUserQuestion multi-select dialog**:

**AskUserQuestion parameters:**
- `question`: ""
- `header`: ""
- `multiSelect`: **true** — user can select multiple paths to combine
- `options`: One per path (label = "Letter — angle tag", description = one-line credibility + key approach)
- **No "/Combine" option needed** — multi-select natively handles combination
- Place the **highest-credibility path first** (serves as recommendation hint)

**Example AskUserQuestion call (JSON, matches tool schema exactly):**
```json
{
  "questions": [
    {
      "question": "",
      "header": "",
      "multiSelect": true,
      "options": [
        {"label": "A — risk-first", "description": " *****"},
        {"label": "B — counter-intuitive", "description": " ****"},
        {"label": "C — time-horizon", "description": " 3-5  ***"}
      ]
    }
  ]
}
```

**Fallback (if tool unavailable):**
```
:

A — [one-line summary + credibility]
B — [one-line summary + credibility]
C — [one-line summary + credibility]

:  [X] 
 "A + B"
```

### Phase 2: Final Output (after user selection)

After the user selects one or multiple paths via the dialog:

**Single path selected:**
```
: [Path X — angle tag]

:
> [Full polished question — clean, ready to copy-paste into any AI]

:
- [Stance Constraint]
- [Anti-Consensus Constraint]
- [Trade-off Constraint]
- [Actionability Constraint]

: [under what conditions this works best]
: [top risk]
: "[follow-up question]"

:  [0-2]/2 |  [0-2]/2 |  [0-2]/2 |  [0-2]/2 |  [0-2]/2
```

**Multiple paths selected (combination):**
```
: [Path X + Path Y] — [brief description of what was merged]

:  [Path X]  [Path Y]  [specific elements]

:
> [Full polished question — merged from selected paths, clean, ready to copy-paste]

:
- [Stance Constraint]
- [Anti-Consensus Constraint]
- [Trade-off Constraint]
- [Actionability Constraint]

: [under what conditions this works best]
: [top risk]
: "[follow-up question]"

:  [0-2]/2 |  [0-2]/2 |  [0-2]/2 |  [0-2]/2 |  [0-2]/2
```

**Combination mechanics (multi-select):**
- **2 paths selected**: Use the higher-credibility path as base, inject the other's specified elements
- **3 paths selected (all)**: Use the highest-credibility path as base, inject the other two's strongest elements. Warn if over-constraining: ""
- **Conflict detection**: If combined elements contradict, flag it and suggest resolution
- After merging, run through the 5 Signals quality gate

**Quality gate** (before outputting):
- Check against 5 Signals (clear success criteria, constraints present, context provided, output format specified, room for exploration). Add any missing signal.
- Run the 5-Dimension Prompt Quality Score (see `references/advanced-techniques.md`):
  - **Clarity** (0-2): Is the optimized question unambiguous?
  - **Specificity** (0-2): Is it precisely scoped?
  - **Completeness** (0-2): Does it include all necessary context and constraints?
  - **Actionability** (0-2): Can the AI directly execute without asking clarifying questions?
  - **Robustness** (0-2): Would slightly different inputs still work with this question?
- If any dimension scores 0, fix it before outputting.

**Self-learning note**: After outputting the final question, silently record user preference data and append optional feedback line:

```

```

---

## Interactive Dialog Patterns

### When to Use AskUserQuestion

SharpInput uses interactive dialogs in three scenarios:

1. **Gate Step 3 (Low Confidence)** — When intent classification confidence is low, present options for the user to clarify
2. **Context Completion** — When critical parameters (budget, timeline, scope, tech stack) are missing or ambiguous
3. **Stage 5 (Path Selection)** — Already implemented for path selection

### Standard Dialog Templates

**[!] IMPORTANT**: All examples below show the content inside the `questions[0]` object. When calling the tool, wrap in `{"questions": [...]}`.

#### Budget Clarification
```json
{"questions": [{"question": "", "header": "", "options": [
  {"label": "1000-2000 ", "description": ""},
  {"label": "2000-5000 ", "description": ""},
  {"label": "5000-9000 ", "description": ""},
  {"label": "", "description": ""}
]}]}
```

#### Timeline Clarification
```json
{"questions": [{"question": "", "header": "", "options": [
  {"label": "1", "description": ""},
  {"label": "1", "description": ""},
  {"label": "3+", "description": ""},
  {"label": "", "description": ""}
]}]}
```

#### Scope/Scale Clarification
```json
{"questions": [{"question": "", "header": "", "options": [
  {"label": "", "description": ""},
  {"label": "", "description": ""},
  {"label": "", "description": ""}
]}]}
```

#### Technical vs Non-technical
```json
{"questions": [{"question": "", "header": "", "options": [
  {"label": "", "description": ""},
  {"label": "/", "description": ""},
  {"label": "", "description": ""}
]}]}
```

### Dialog Design Rules

1. **Max 4 options** — More than 4 overwhelms; use "Other" for overflow
2. **Always include "/Other"** — For custom values not covered by presets
3. **Description is mandatory** — Each option needs a one-line explanation
4. **Language match** — Dialog language must match user's input language
5. **No duplicate questions** — If Gate already asked, don't re-ask in Context Completion
6. **Record selection** — User's choice becomes context for all subsequent stages
