# Advanced Prompting Techniques for SharpInput

This reference provides advanced prompting techniques that can be integrated into SharpInput's optimization flow. When optimizing user inputs, consider applying these techniques to make the optimized version more effective.

## Chain-of-Thought (CoT) Prompting

Forcing the AI to show its reasoning process before giving a final answer.

**When to use:**
- Complex multi-step problems
- Questions requiring logical reasoning
- When the user needs to verify the AI's reasoning
- Math, coding, or analytical tasks

**Injection methods:**
- "Let's think step by step" — Forces sequential reasoning
- "First, identify the key factors. Then, analyze each one. Finally, conclude." — Structured CoT
- "Before answering, show me your reasoning chain" — Explicit reasoning demand
- "Walk me through your logic" — Natural language version

**Example injection in SharpInput:**
> Original: "应该跳槽吗？"
> Optimized: "...在给出建议前，请先列出影响这个决策的 5 个关键因素，逐一分析每个因素的权重，然后基于分析给出结论。不要直接跳到结论。"

## Few-Shot Prompting

Providing examples to establish the expected output pattern.

**When to use:**
- When output format is critical
- When the user has a specific style in mind
- When "show me what good looks like" is more effective than describing it
- Creative tasks, formatting tasks, tone calibration

**Injection methods:**
- Provide 1-3 examples of ideal output
- Show a "before vs after" comparison
- Include an example with annotations explaining why it's good

**Example injection in SharpInput:**
> "我想要的回答风格是这样的：[附一个示例]。请按照这个风格回答我的问题。"

## Role-Based Prompting

Assigning a specific persona or expertise to the AI.

**When to use:**
- When domain expertise matters
- When perspective-taking would improve the answer
- When the user needs advice from a specific vantage point
- When contrarian viewpoints are valuable

**Injection methods:**
- "You are a [specific role] with [years] of experience in [domain]"
- "Answer as if you were [specific person/role]"
- "From the perspective of a [role], what would you say?"
- "Switch between [Role A] and [Role B] perspectives"

**Example injection in SharpInput:**
> 原始："这个产品方案怎么样？"
> 优化后："假设你是一个有 10 年经验的产品VP，同时也是一个对新技术持怀疑态度的用户，你会怎么评价这个方案？请分别从这两个视角给出评价。"

## XML Tags for Structure

Using XML-like tags to organize complex prompts into clear sections.

**When to use:**
- Long, multi-part prompts
- When the AI needs to handle multiple constraints simultaneously
- When clarity of prompt structure is critical
- When the optimized question has 5+ distinct components

**Injection methods:**
- `<context>...</context>` — Background information
- `<task>...</task>` — What to do
- `<constraints>...</constraints>` — Rules and limitations
- `<output_format>...</output_format>` — How to format the answer
- `<examples>...</examples>` — Reference examples

**Example injection in SharpInput:**
```
<context>我在一家 50 人的 SaaS 创业公司做产品总监，DAU 5 万，月留存 60%。</context>
<task>评估我的增长策略：先做留存优化再做拉新。</task>
<constraints>必须给出明确的同意或反对立场，不允许"看情况"。必须说明风险。</constraints>
<output_format>先给结论（一句话），再给 3 个支撑论据，最后给 1 个最大的反驳理由。</output_format>
```

## Structured Output Forcing

Explicitly defining the output structure the AI should follow.

**When to use:**
- When the user needs a specific format (table, list, comparison matrix)
- When consistency across multiple queries matters
- When the answer needs to be parsed or processed programmatically
- When "answer in paragraphs" is too vague

**Injection methods:**
- "Output in this exact format: [template]"
- "Use a table with columns: [col1], [col2], [col3]"
- "Structure your answer as: 1) Summary (1 line) 2) Analysis (3 bullets) 3) Recommendation (1 action)"
- "Answer in JSON format with keys: ..."

**Example injection in SharpInput:**
> "请用以下结构回答：结论（一句话）→ 核心论据（3 条，每条一句话）→ 最大风险（1 条）→ 具体下一步（1 条可执行行动）。"

## Combining Techniques

The most effective prompts often combine multiple techniques:

**CoT + Role + Structured Output:**
> "你是一个有 10 年经验的增长专家。请一步步分析我们的增长瓶颈：先看数据，再看用户行为，最后看竞争环境。每一步给出一个结论。最终汇总为一个可执行的 30 天行动计划。"

**Few-Shot + Anti-Consensus:**
> "大多数人会说'先做拉新'——但看看这个反例：[案例]。请用类似的反直觉思路分析我的情况。"

**XML Tags + Role + CoT:**
```
<role>你是一个对增长策略持怀疑态度的CFO</role>
<task>评估这个增长方案的投入产出比</task>
<constraints>用数字说话，不接受"长期价值"这类模糊概念</constraints>
<process>先质疑假设 → 再估算成本 → 最后给出ROI预测</process>
```

## Integration with SharpInput

These techniques should be used **selectively** based on the input type and level:

| Level | Recommended Techniques |
|-------|----------------------|
| Level 0 | None (just forcing constraints) |
| Level 1 | Structured Output Forcing |
| Level 2 | + Role-Based, CoT |
| Level 3 | + Few-Shot, XML Tags, all combinations |

**Key principle**: Don't over-engineer. A Level 1 question about "React vs Vue" doesn't need XML tags and CoT. A Level 3 strategic decision might benefit from all of them.
