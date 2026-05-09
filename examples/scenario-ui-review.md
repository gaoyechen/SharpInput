# Scenario: UI Review

User input:

```text
帮我优化：这个网页有点丑，让 AI 帮我看看。
```

Expected scenario:

- ui_review
- description clarifier should convert "丑" into review dimensions

Example upgraded prompt:

> 请作为资深界面设计评审，评估这个网页的视觉和交互问题：`[截图/链接]`。页面目标是 `[目标]`，目标用户是 `[用户]`。请重点检查信息层级、视觉一致性、留白与密度、按钮与表单可发现性、移动端适配、品牌感。请按优先级输出问题清单，每条包括：问题位置、为什么影响体验、修改建议、改动成本、预期收益。不要只给审美评价，要给能执行的改法。
