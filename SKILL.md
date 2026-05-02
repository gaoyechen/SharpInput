---
name: SharpInput
description: >
  Optimize any user input (questions, statements, plans, ideas, requirements) through
  deep cognitive self-checking, multi-dimensional reframing, and anti-consensus detection
  to force AI outputs with genuine opinions, clear positions, and real insight —
  not "correct but useless" platitudes.
  Triggers: "optimize this", "how to ask better", "help me organize", "is this good enough",
  "how should I phrase this", "make this better", any discussion about input/question quality,
  pasting content asking for optimization, or any non-trivial input that benefits from sharpening.
  中文触发词: "优化这个问题", "帮我优化", "怎么问更好", "帮我组织一下",
  "这样问行不行", "这样表述好不好", "帮我改一下", "优化提问", "优化输入",
  "帮我理清思路", "这个问题问得好不好", "帮我润色", "优化一下",
  "这样说对不对", "帮我理一下", "我这样说合适吗", "帮我完善一下".
agent_created: true
---

# SharpInput — AI Input Optimizer

> ⚠️ **GOLDEN RULE — Interactive Dialogs**: When this skill instructs you to present options to the user (for intent clarification, parameter collection, or path selection), you **MUST call the `AskUserQuestion` tool**. **NEVER** output text-based options like "A / B / C" or bullet-list choices — these are **NOT interactive** and the user **cannot click them**. The only acceptable way to present choices is via the `AskUserQuestion` tool call. **This rule applies everywhere in this skill without exception.**
>
> **Exact call format** (the tool parameter is `questions`, an array of question objects):
> ```json
> {"questions": [{"question": "你的问题？", "header": "标签", "options": [
>   {"label": "选项A", "description": "说明"},
>   {"label": "选项B", "description": "说明"}
> ]}]}
> ```
> For multi-select, add `"multiSelect": true` inside the question object.

Through scene gating → intent recognition → context completion → problem reframing →
cognitive forcing → divergent thinking → adversarial loop → convergent synthesis,
SharpInput sharpens any user input — questions, problem statements, requirements, ideas, plans —
into optimized versions that force AI to produce genuine opinions, clear positions, and real insight,
not "correct but useless" platitudes.

---

## Core Flow

Upon receiving any user input, execute in the following order:

```
Gate (Scene Filter) → Memory Load → Intent Recognition + Context Completion → Stage 1~5 → Output
```

Gate determines the path, memory load personalizes the flow from past preferences, intent recognition selects the forcing strategy, and context completion ensures sufficient information.

---

### Gate: Scene Filter (Executes First)

Before entering any stage, classify the user input through a **signal detection decision tree**. Execute steps in order; stop at the first definitive match.

#### Step 1: Signal Detection — Scan for these signals in the input

| Signal | Detection Keywords / Patterns | Examples |
|--------|------------------------------|----------|
| **Factual lookup** | "what is X", "how to use X", "X definition", "X syntax"; "X是什么", "X怎么用", "X的定义", "X语法" | "What is a closure in JS" / "闭包是什么" |
| **Debug / error** | Error messages, "why does this error", stack traces, "this code doesn't work"; "报错了", "为什么报错", "这段代码不对" | "TypeError: Cannot read property" / "这段代码报错了" |
| **Formatting / conversion** | "convert", "format", "translate", "summarize", "rewrite this", "template"; "转换", "格式化", "翻译", "总结", "改写", "模板" | "Translate this to English" / "翻译成英文" |
| **Comparison signal** | "vs", "compared to", "which is better", "A or B", "difference between"; "哪个好", "A还是B", "对比", "区别", "优劣" | "React vs Vue" / "React和Vue哪个好" |
| **Decision signal** | "should I", "is it worth", "choose between", "decide", "trade-off", "pros and cons"; "应不应该", "是否值得", "要不要", "怎么选", "利弊" | "Should I switch jobs" / "我应不应该跳槽" |
| **Analysis signal** | "analyze", "evaluate", "how is this plan", "why would X fail", "review"; "分析", "评估", "这个方案怎么样", "为什么会失败", "评价" | "Analyze this architecture" / "分析一下这个架构" |
| **Exploration signal** | "what directions", "what else", "any other options", "brainstorm", "explore"; "有什么方向", "还有什么", "其他选择", "头脑风暴", "探索" | "What are my options" / "还有什么方向" |
| **Strategy signal** | "how should I approach", "long-term", "roadmap", "priority", "resource allocation"; "怎么规划", "长期", "路线图", "优先级", "资源分配" | "How should I scale my team" / "怎么规划团队扩张" |
| **Problem statement** | Describes a current situation/problem without asking a question; "转化率下降", "用户流失", "性能瓶颈", "团队效率低"; "conversion rate is dropping", "users are churning" | "我们的转化率一直在下降" / "Our conversion rate keeps declining" |
| **Requirement** | Describes what needs to be built/done; "帮我设计", "帮我做一个", "需要实现", "我想要一个"; "I need a", "build me", "design a", "create a" | "帮我设计一个用户增长方案" / "I need a user growth strategy" |
| **Idea / proposal** | Presents an idea or opinion to validate; "我觉得", "我的想法是", "我想试试", "方案是"; "I think", "my idea is", "what if we", "proposal" | "我觉得应该用微服务重构" / "I think we should refactor to microservices" |
| **Plan review** | Shares a plan or document for feedback; "这是我的方案", "帮我看看", "以下是我的计划"; "here's my plan", "review this", "check my approach" | "这是我的技术方案，帮我看看" / "Here's my technical plan, review it" |
| **System prompt design** | Wants to write system prompts / custom instructions / agent configs; "帮我写一个system prompt", "设计一个AI助手的指令", "帮我写custom instructions", "agent配置"; "write a system prompt", "design custom instructions", "create agent config" | "帮我写一个客服机器人的system prompt" / "Write a system prompt for a code review agent" |

#### Step 2: Decision Tree

```
Input received
  │
  ├─ Has Factual lookup OR Debug/Formatting signal?
  │   └─ YES → 🟢 Quick Execution: Answer directly. Skip SharpInput entirely.
  │
  ├─ Has Comparison/Decision/Analysis/Exploration/Strategy signal?
  │   ├─ Only 1 signal, no specific constraints (who/what/where/when)?
  │   │   └─ 🟡 Level 1 (Light Optimization): Clear direction, needs polish
  │   ├─ 1-2 signals + has specific constraints (role, scenario, tech stack, team size)?
  │   │   └─ 🔴 Level 2 (Medium Forcing): Has context, needs stance
  │   └─ 2+ signals OR contains "trade-off"/"risk"/"long-term"/"strategic" / "权衡"/"风险"/"长期"/"战略"?
  │       └─ 🔴 Level 3 (Deep Adversarial): Complex decision, full analysis
  │
  ├─ Has Problem statement / Requirement / Idea / Plan review signal?
  │   ├─ Short, vague statement with no context?
  │   │   └─ 🟡 Level 1 (Light Optimization): Needs sharpening and context
  │   ├─ Statement with some context but missing goals or constraints?
  │   │   └─ 🔴 Level 2 (Medium Forcing): Has substance, needs framing
  │   └─ Detailed plan/idea/proposal that would benefit from adversarial review?
  │       └─ 🔴 Level 3 (Deep Adversarial): Full analysis with multi-path alternatives
  │
  ├─ Has System prompt design signal?
  │   └─ YES → 🟡 Special Mode: Use system prompt design template from `references/advanced-techniques.md`.
  │       Apply SharpInput's cognitive forcing to the design: "Your system prompt must have a clear
  │       anti-definition — what it does NOT do is more important than what it does."
  │
  └─ No clear signal detected
      └─ 🟡 Level 1 by default. Inform user:
         "I've classified this as light optimization. Say 'deep mode' for full analysis."
         "已归类为轻度优化，说'深度模式'进入全面分析。"
```

#### Step 3: Confidence & Escalation

After classification, assign a **confidence score** (High / Medium / Low):

- **High confidence**: Question clearly matches one signal category → proceed directly
- **Medium confidence**: Question matches multiple categories or has ambiguous signals → state your classification and proceed, but note: "If this feels wrong, say 'upgrade' to go deeper." / "如果感觉不对，说'升级'可以深入分析。"
- **Low confidence**: No clear signal or contradictory signals → **MUST call the AskUserQuestion tool (not output text options)**.

**⚠️ CRITICAL — Low Confidence Dialog (AskUserQuestion REQUIRED):**

When confidence is low, you **MUST call the AskUserQuestion tool** to present clickable options. **DO NOT** output text-based options, bullet lists, or letter choices — these are NOT interactive and the user cannot click them. The only acceptable format is a tool call to AskUserQuestion. If you output "A / B / C" as text instead of calling AskUserQuestion, you have failed this step.

**Standard options for low confidence:**
- 2-3 most likely intent categories based on signal analysis
- A "Level override" option for direct level selection
- An "Other" option for custom input

**Example AskUserQuestion call (JSON format, matches tool schema exactly):**
```json
{
  "questions": [
    {
      "question": "我不确定如何分类你的问题，请选择最符合的意图",
      "header": "意图确认",
      "options": [
        {"label": "选项 A", "description": "适用于 [场景描述]"},
        {"label": "选项 B", "description": "适用于 [场景描述]"},
        {"label": "直接指定等级", "description": "选择 Level 0/1/2/3 进入对应优化模式"}
      ]
    }
  ]
}
```

**Domain-specific clarification dialogs:**

For certain common ambiguous scenarios, use specialized dialog options:

1. **Purchase/Budget decisions** (when input mentions buying, pricing, cost, or budget but range is unclear):
   ```json
   {"questions": [{"question": "你的预算范围是？", "header": "预算确认", "options": [
     {"label": "1000-2000 元", "description": "入门级选择"},
     {"label": "2000-5000 元", "description": "中端选择"},
     {"label": "5000-9000 元", "description": "高端选择"},
     {"label": "其他", "description": "自定义预算范围，选择 Other 输入具体金额"}
   ]}]}
   ```

2. **Technical vs Non-technical** (when domain is unclear):
   ```json
   {"questions": [{"question": "你的问题更偏向哪个领域？", "header": "领域确认", "options": [
     {"label": "技术实现", "description": "代码、架构、工程相关"},
     {"label": "产品/业务", "description": "策略、增长、用户体验相关"},
     {"label": "个人决策", "description": "职业、生活、学习相关"}
   ]}]}
   ```

3. **Scope clarification** (when problem scale is ambiguous):
   ```json
   {"questions": [{"question": "你的问题规模是？", "header": "规模确认", "options": [
     {"label": "具体问题", "description": "单一、明确的问题点"},
     {"label": "系统性问题", "description": "涉及多个关联因素"},
     {"label": "战略性问题", "description": "长期、大方向的决策"}
   ]}]}
   ```

**Dialog selection rules:**
- If user picks a predefined option → proceed with that intent/level
- If user picks "Other" → use their custom input to re-classify
- If user provides budget/price info → record as context for the optimization
- Always match the dialog language to the user's language (Chinese in → Chinese dialog)

**User override always takes priority**: If the user says "deep mode", "Level 3", "just optimize it", "深度模式", "深度分析", "Level 3", "施压一下", or any explicit level instruction, skip the decision tree and go directly to that level.

---

### Memory Load (After Gate, Before Intent Recognition)

> 📖 **Reference**: Full memory system spec in `references/self-learning.md`. Preference data stored in `references/user-preferences.md`.

Read `references/user-preferences.md`. If preference data exists, silently apply:

| Preference | How to Apply |
|-----------|-------------|
| **Default level bias** | If user historically prefers Level 3, when Gate classifies Level 1/2, suggest: "根据历史偏好建议 Level 3，说'升级'即可" |
| **Angle preference** | In Stage 3, prioritize generating paths matching user's preferred angle tags |
| **Forcing strategy** | Reduce priority of strategies user consistently skips |
| **Recommendation bias** | In Stage 5 selection prompt, recommend the path matching user's preference |
| **Domain context** | Use known domain to improve Context Completion inference accuracy |

If no preference data found, proceed normally.

**Fully silent**: Do NOT inform the user that preferences are being applied. The effect is visible in recommendations; the mechanism is invisible. Only explain if the user asks "why do you recommend this?"

---

### Intent Recognition (After Gate, Before Stage 1)

**Goal: Identify the core intent of the user's question to determine which forcing strategy Stage 2 applies.**

Classify with a **primary + secondary** dual-label system:

| Intent | Meaning | Typical Phrasing | Forcing Strategy |
|--------|---------|-----------------|-----------------|
| **🧠 Explain** | Understand concepts / principles / mechanisms | "What is X", "How does X work"; "X是什么", "X怎么工作", "帮我理解X" | Counter-intuitive anchor + Analogical counter-examples |
| **⚖️ Decision** | Make a choice / judgment | "Should I do A or B", "Is it worth doing X"; "我应该选A还是B", "值不值得做X", "哪个好" | Regret pre-mortem + Killer question |
| **🔨 Generate** | Generate code / content / solution | "Help me write X", "Design a Y"; "帮我写个X", "设计一个Y", "做一个Z" | Minimal viable solution + Constraint challenge |
| **🔬 Analyze** | Analyze a problem / evaluate a solution | "How is this plan", "Why would X fail"; "这个方案怎么样", "为什么X会失败", "分析一下" | Hidden assumption exposure + Failure conditions |
| **🧭 Explore** | Explore directions / find possibilities | "What directions are there", "What else could work"; "有什么方向", "还有什么办法", "还有其他选择吗" | Multi-path + Devil's advocate |

**Output rules**:
- Show the intent recognition result in one sentence:
  - EN: "I've identified your question as **Decision type** (making a choice). Primary forcing strategy: regret pre-mortem + killer question."
  - ZH: "我识别到你的问题是 **Decision 类型**（做选择）。主要施压策略：后悔预判 + 杀手问题。"
- If a secondary intent exists, show it too: "Primary: Decision, Secondary: Analyze" / "主意图: Decision, 次意图: Analyze"
- **User can override**: If the user says "no, this is more like analysis" / "不对，这更像是分析" → switch forcing strategy.

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

**Output style: Interactive Dialog + Conditional Framework**

When critical information is missing, you **MUST call the AskUserQuestion tool** to present clickable options. **DO NOT** output text-based "A / B / C" options — the user cannot click them. Only a tool call to AskUserQuestion produces an interactive dialog.

**Interactive dialog selection by ambiguity type:**

| Ambiguity Type | Detection Signal | Dialog Options |
|----------------|-----------------|----------------|
| **Budget/Price** | "买", "购买", "预算", "价格", "多少钱", "cost", "budget", "price", "afford" | 3 price tiers + "Other" (custom) |
| **Scope/Scale** | "做一个", "方案", "系统", "项目", "规模", "build", "system", "project" | Small / Medium / Large + "Other" |
| **Timeline** | "多久", "什么时候", "时间", "deadline", "when", "how long", "timeline" | 1周内 / 1个月内 / 3个月+ / 其他 |
| **Audience** | "给谁看", "写给", "面向", "for", "audience", "readers" | Internal / Client / Public / Other |
| **Tech Stack** | "用什么", "框架", "技术", "language", "framework", "stack" | 提供常见选项 + "Other" |
| **Role/Perspective** | "从谁的角度", "角色", "perspective", "role", "standpoint" | 技术 / 产品 / 管理层 / 用户 / Other |

**AskUserQuestion call pattern (JSON, matches tool schema exactly):**
```json
{"questions": [{"question": "[Chinese or English question matching user's language]", "header": "[Short label, 2-4 chars]", "options": [
  {"label": "[Option 1]", "description": "[What this option means]"},
  {"label": "[Option 2]", "description": "[What this option means]"},
  {"label": "[Option 3]", "description": "[What this option means]"},
  {"label": "其他", "description": "自定义，选择 Other 输入具体值"}
]}]}
```

**Fallback**: If AskUserQuestion tool is not available, use the text-based inference + confirmation pattern:
> "我推测你的背景是 [X]，想解决 [Y]，在 [Z] 场景下——对吗？说偏了帮我纠正。"

**Rules**:
- Inference must be based on clues already in the question — no fabrication
- If the question already has sufficient information (background, goal, and scenario are all clear), skip this step and tell the user:
  - EN: "Question has sufficient context, proceeding directly to optimization."
  - ZH: "问题信息充分，直接进入优化。"
- After the user selects or corrects, proceed to Stage 1
- Level 0 (rapid forcing) skips this step; Level 1 may skip it unless information is clearly insufficient
- **Language matching**: All user-facing messages in this flow must match the user's language (Chinese in → Chinese out, English in → English out)
- **Conditional answer for vague inputs**: When information is clearly insufficient (Level 1, vague input), do NOT only ask clarifying questions. Instead, provide a **conditional framework** alongside the questions: "If your situation is [X], my suggestion is [Y]. If it's [A], then [B]. Confirm which applies to you." This ensures the user gets directional value even without answering all questions.
- **Dialog vs text**: Prefer AskUserQuestion for common quantifiable parameters (budget, timeline, scope, tech stack). Use text fallback only for open-ended or nuanced context that can't be pre-defined.
- **Combine with Gate**: If Gate's Step 3 already triggered a dialog (e.g., budget dialog for low-confidence purchase question), do NOT ask the same question again in Context Completion. Use the Gate dialog result as input.

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
| **Compress if long** | If the input is very long (>500 words), extract the core question/statement to 2-3 sentences. Preserve key constraints. Note what was compressed. |

> For long inputs, apply context compression: remove filler, merge similar points, prioritize constraints and goals. See `references/advanced-techniques.md` → Context/Token Management.

**Internal output**: A constrained question. This becomes the input for all subsequent stages. Not shown to user.

---

### Stage 2: Cognitive Forcing 🔥 Core Moat

**Goal: Force the AI to produce "opinions" instead of platitudes.**

#### Base Four Constraints (Must Inject at All Levels)

| Constraint | Description | Injection Method |
|-----------|-------------|-----------------|
| **Stance Constraint** | Must choose a direction, no neutrality allowed | Require "you must clearly support or oppose" |
| **Anti-Consensus Constraint** | Must challenge mainstream views | Require "present a position contrary to mainstream opinion and defend it" |
| **Trade-off Constraint** | Can't "have it all", must sacrifice something | Require "explicitly state what you give up and what you gain" |
| **Actionability Constraint** | Must produce a concrete first step | Require "give me one specific action I can take this week — not a direction, not a framework, a step" |

#### Deep Forcing Layer (Level 2+, Auto-selected by Intent Recognition)

> 📖 **Reference**: For role-setting and persona construction in forcing constraints, see `references/prompt-patterns.md` → **CRISPE Framework** (Capacity/Request/Insight/Style/Personality/Experiment). For advanced prompting techniques (CoT, few-shot, XML tags, role-based prompting) that can be woven into optimized questions, see `references/advanced-techniques.md`.

Primary intent determines the main forcing strategy; secondary intent adds supplementary constraints:

| Intent | Main Forcing Strategy | Injection Method | Technique Hint |
|--------|----------------------|-----------------|----------------|
| **🧠 Explain** | **Counter-intuitive anchor** | "Present a view contrary to mainstream knowledge and prove it with a specific case" | Use CoT: require step-by-step reasoning before conclusion |
| **⚖️ Decision** | **Regret pre-mortem** | "If you followed this advice, what would you most regret 3 years from now?" | Use structured output: conclusion → reasoning → risk |
| **🔨 Generate** | **Minimal viable solution** | "If you could only keep one feature / one element, which one? Why?" | Use few-shot: provide an example of the expected output style |
| **🔬 Analyze** | **Hidden assumption exposure** | "What premises must hold for this question to be valid? If one premise fails, how does the conclusion change?" | Use XML tags: structure as `<assumptions>` → `<analysis>` → `<conclusion>` |
| **🧭 Explore** | **Devil's advocate** | "Write a proposal for your competitor, convincing them to take the route you oppose" | Use role-based: assign specific adversarial persona |

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

**Path presentation**: Label each approach as Path A / B / C. Each path entry must include:
- A one-sentence **approach label** (what makes this path distinct)
- The full **optimized question** (self-contained, ready to use)
- An **angle tag** from the standard vocabulary (see below) for combination reference

**Standard angle vocabulary** (pick the closest fit):

| Angle Tag | Meaning | When to Use |
|-----------|---------|-------------|
| `risk-first` | Focus on what could go wrong, downside analysis | Decision, Analyze intents |
| `constraint-challenge` | Challenge the question's own premises | Explain, Analyze intents |
| `counter-intuitive` | Seek the non-obvious answer | Explain, Explore intents |
| `minimalist` | Strip to essentials, "one thing only" | Generate, Decision intents |
| `adversarial` | Argue against the obvious direction | Explore, Decision intents |
| `time-horizon` | Shift perspective to 3-5 years out | Strategy, Decision intents |
| `role-reversal` | Answer from an unexpected stakeholder's view | All intents |

> 📖 Output format: see `references/output-templates.md` → Level 3 → Multi-Path Comparison.

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

**Goal: From "multiple possibilities" → user-selected, polished, copy-paste-ready question.**

> 📖 **Reference**: Verify the final question meets `references/prompt-patterns.md` → **5 Signals of a High-Quality Question**.

Level 3 output follows two phases: **Phase 1** (Analysis + Paths + Selection) in one go, **Phase 2** (Final Output) after user selection.

#### Step 1: Output Phase 1 — Analysis + Paths + Selection

Output in this **strict order**:

```
[Level 3]

诊断: [2-3 sentences: core intent + main flaw + what mediocre answer you'd likely get]

意图: [Explain/Decision/Generate/Analyze/Explore]（如有次意图也列出）
施压策略: [primary strategy] + [secondary supplement]

路径 A — [angle tag]:
> [Full optimized question for path A, self-contained, ready to copy-paste]
可信度: [⭐⭐⭐⭐⭐ ~ ⭐] — [one-line key risk or weakest assumption]

路径 B — [angle tag]:
> [Full optimized question for path B, self-contained, ready to copy-paste]
可信度: [⭐⭐⭐⭐⭐ ~ ⭐] — [one-line key risk or weakest assumption]

路径 C — [angle tag]:
> [Full optimized question for path C, self-contained, ready to copy-paste]
可信度: [⭐⭐⭐⭐⭐ ~ ⭐] — [one-line key risk or weakest assumption]

被忽略的维度:
1. [Dimension]: [why it matters]
2. [Dimension]: [why it matters]
```

**Key rules:**
- **No comparison table.** Each path is presented independently with its own full optimized question.
- Each path includes its own credibility score + one-line key risk.
- The full optimized question under each path is self-contained and ready to copy-paste.
- Paths are ordered by credibility (highest first).

**⚠️ CRITICAL — Immediately after** the text output, you **MUST call the AskUserQuestion tool** with `multiSelect: true`. **DO NOT** output text-based "A / B / C" options — these are NOT clickable. The user needs an interactive dialog to select paths. If you output text options instead of calling AskUserQuestion, you have failed this step.

**AskUserQuestion parameters:**
- `question`: "选择路径（可多选），我会输出最终打磨好的问题"
- `header`: "选择路径"
- `multiSelect`: **true** — user can select multiple paths to combine
- `options`: One per path (label = "Letter — angle tag", description = one-line credibility + key approach)
- **No "组合/Combine" option needed** — multi-select natively handles combination
- Place the **highest-credibility path first** (serves as recommendation hint)

**Example AskUserQuestion call (JSON, matches tool schema exactly — `multiSelect` goes inside the question object):**
```json
{
  "questions": [
    {
      "question": "选择路径（可多选），我会输出最终打磨好的问题",
      "header": "选择路径",
      "multiSelect": true,
      "options": [
        {"label": "A — risk-first", "description": "聚焦风险和下行分析，可信度 ⭐⭐⭐⭐⭐"},
        {"label": "B — counter-intuitive", "description": "寻找反直觉答案，可信度 ⭐⭐⭐⭐"},
        {"label": "C — time-horizon", "description": "拉到 3-5 年后审视，可信度 ⭐⭐⭐"}
      ]
    }
  ]
}
```

**Fallback**: If AskUserQuestion tool is not available, fall back to text-based prompt:
> **ZH:** "选择路径（可多选），我会输出最终打磨好的问题。如果犹豫，路径 [X] 可信度最高。可组合多条（如 'A + B'）。"
>
> **EN:** "Select paths (multi-select OK). If unsure, Path [X] has the highest credibility. Combine multiple (e.g., 'A + B')."

#### Step 2: Handle User Response

| User Response | Action |
|--------------|--------|
| Selects one path (e.g., only "B") | Use that path's optimized question as base |
| Selects multiple paths (e.g., "A" + "B") | Merge elements from selected paths (see combination mechanics below) |
| Describes preference (e.g., "更偏风险视角") | Use closest path as base, adjust per preference |
| Says "你选" / "your pick" | Apply recommendation hint (highest-credibility path) |
| Says "stop" / "直接给问题" | Output highest-credibility path immediately |

**Combination mechanics** (multi-select):
- **2 paths selected**: Use the higher-credibility path as base, inject the other's specified elements
- **3 paths selected (all)**: Use the highest-credibility path as base, inject the other two's strongest elements. Warn if over-constraining: "三条路径全组合可能导致约束过多，我会提取每条路径的核心要素而非全部内容。"
- **Conflict detection**: If combined elements contradict, flag it and suggest resolution
- After merging, run through the 5 Signals quality gate

#### Step 3: Output Phase 2 — Final Polished Output

**Single path selected:**
```
已选择: [Path X — angle tag]

优化后的问题:
> [Full polished question — clean, ready to copy-paste into any AI]

施压约束:
- [Stance Constraint]
- [Anti-Consensus Constraint]
- [Trade-off Constraint]
- [Actionability Constraint]

适用边界: [under what conditions this works best]
风险提示: [top risk]
如果回答方向不对，追问: "[follow-up question]"

优化质量: 清晰度 [0-2]/2 | 具体性 [0-2]/2 | 完整性 [0-2]/2 | 可执行性 [0-2]/2 | 鲁棒性 [0-2]/2
```

**Multiple paths selected (combination):**
```
已组合: [Path X + Path Y] — [brief description of what was merged]

融合策略: 以 [Path X] 为基础，注入 [Path Y] 的 [specific elements]

优化后的问题:
> [Full polished question — merged from selected paths, clean, ready to copy-paste]

施压约束:
- [Stance Constraint]
- [Anti-Consensus Constraint]
- [Trade-off Constraint]
- [Actionability Constraint]

适用边界: [under what conditions this works best]
风险提示: [top risk]
如果回答方向不对，追问: "[follow-up question]"

优化质量: 清晰度 [0-2]/2 | 具体性 [0-2]/2 | 完整性 [0-2]/2 | 可执行性 [0-2]/2 | 鲁棒性 [0-2]/2
```

Quality gate: before outputting, check against 5 Signals (clear success criteria, constraints present, context provided, output format specified, room for exploration). Add any missing signal.

Also run the 5-Dimension Prompt Quality Score (see `references/advanced-techniques.md` → Evaluation Framework):
- **Clarity** (0-2): Is the optimized question unambiguous?
- **Specificity** (0-2): Is it precisely scoped?
- **Completeness** (0-2): Does it include all necessary context and constraints?
- **Actionability** (0-2): Can the AI directly execute without asking clarifying questions?
- **Robustness** (0-2): Would slightly different inputs still work with this question?

If any dimension scores 0, fix it before outputting. Include the score summary at the end of the output.

#### Step 4: Record User Preference + Optional Feedback

After outputting the final question, execute two actions:

**A. Silent preference recording** (always, no user interaction):
Record this session's data to `references/user-preferences.md`. See `references/self-learning.md` for full rules.

**B. Optional feedback collection** (append to the output):
> **ZH:** "拿到回答后，如果方向不对回复「方向偏了」我会调整；如果很好回复「很好」我会记住这个模式。"
>
> **EN:** "After getting the answer, reply 'off track' if the direction was wrong, or 'great' if it worked well — I'll remember the pattern."

If user replies with feedback, record it as a high-quality preference signal in `references/user-preferences.md`.

---

## Output Formats

> All output templates (Level 0~3) and adaptive output rules are in `references/output-templates.md`. Read that file before rendering output.

**Level display (mandatory)**: Every output must start with the current Level on its own line: `[Level 0]` / `[Level 1]` / `[Level 2]` / `[Level 3]`. This lets the user know which level they're at and whether to upgrade. Each output should end with a hint: "说「升级」可进入 Level X。"

**Level quick reference**:
| Level | Name | What to Output |
|-------|------|---------------|
| 0 | Rapid Forcing | Cognitive Forcing Version + Consensus Level |
| 1 | Light Optimization | Diagnosis + Optimized Question + Improvements |
| 2 | Medium Forcing | Intent + Diagnosis + Forcing Version + Dimensions + Warning |
| 3 | Deep Adversarial | 诊断 → 意图 → 路径A/B/C（独立展示，含完整问题+可信度）→ 被忽略的维度 → 多选对话框 |

**Adaptive rules summary** (full details in `references/output-templates.md`):
- **Level 3 structure**: 诊断 → 意图 → 路径A/B/C（每条路径独立展示完整优化问题+可信度，不做对比表）→ 被忽略的维度 → AskUserQuestion 多选对话框
- **Progressive disclosure**: Say "stop" or "just give me the question" at any stage
- **Language adaptation**: Placeholders follow user's language
- **Focus mode**: Specify which sections to show

---

## Boundary Rules

1. **Gate first** — Quick execution questions get direct answers, no SharpInput flow, zero friction cost
2. **Transparent intent** — Show the user the intent recognition result and forcing strategy; user can override anytime
3. **No fabrication in context inference** — Inference must be based on clues in the question; skip if information is sufficient
4. **Don't change core intent** — Optimize the way of asking, not what the user should ask about
5. **Don't judge question quality** — Only provide improvement suggestions, never evaluate the user's questioning skill
6. **Ready to use** — Optimized questions must be complete and directly copy-pasteable to any AI
7. **Stay relevant** — Hidden dimensions must relate to user intent; don't chase novelty at the expense of relevance
8. **Respect user choice** — User can override forcing level and intent labels anytime
9. **Transparent forcing level** — Output must clearly indicate the current level; user can upgrade or downgrade anytime
10. **Honest credibility scores** — Credibility must be based on actual review results, never inflated for appearance
11. **Silent preferences** — Preferences are applied invisibly; only explain if asked
12. **Preference data stays in skill** — Store in `references/user-preferences.md`, not in workspace memory
13. **Sliding window** — Preference stats based on last 10 interactions; old data naturally decays

---

## References

- `references/output-templates.md` — All output templates (Level 0~3) and adaptive output rules
- `references/prompt-patterns.md` — Read as needed:
  - CRISPE / CO-STAR prompting frameworks
  - Common anti-patterns and fixes
  - Consensus answer identification and breaking techniques
  - 5 signals of high-quality questions
- `references/advanced-techniques.md` — Advanced prompting techniques for optimized questions:
  - Chain-of-Thought (CoT) reasoning
  - Few-shot examples
  - Role-based prompting
  - XML tags for structured prompts
  - Structured output forcing
  - System prompt design templates
  - Prompt quality evaluation (5-dimension scoring)
  - Technique combination patterns
- `references/self-learning.md` — Self-learning system specification (preference recording, application rules, sliding window)
- `references/user-preferences.md` — Auto-maintained user preference data (do not edit manually)
