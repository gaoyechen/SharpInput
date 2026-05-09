# Level 2 Pressure Prompt

User input:

```text
帮我优化：ChatGPT Plus 和 Claude Pro 选哪个？
```

Expected route:

- Level 2
- primary_intent: 决策
- scenario: ai_subscription_choice
- pressure: strong

Example upgraded prompt:

> 我想在 ChatGPT Plus 和 Claude Pro 之间选择一个订阅。我的主要工作流是 `[写作/代码/研究/学习/产品方案]`，预算是 `[预算]`，隐私或数据限制是 `[限制]`。请先给出明确推荐，再用表格比较：适合场景、短板、成本、输出稳定性、长文本能力、代码能力、中文表现。不要只说“看需求”，必须说明在我的场景下默认推荐会失效的条件，以及什么信号会让你改选另一个工具。最后给出一个 7 天试用验证清单。
