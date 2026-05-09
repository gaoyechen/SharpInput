# Level 1 Polish

User input:

```text
我想让 AI 帮我写一份需求文档，怎么问？
```

Expected route:

- Level 1
- primary_intent: 生成
- scenario: prd_srs_generation
- ask or placeholder for feature goal, user, constraints

Example upgraded prompt:

> 请帮我生成一份产品需求文档 PRD。产品/功能目标是 `[功能目标]`，目标用户是 `[目标用户]`，使用场景是 `[使用场景]`。请输出：背景与目标、用户故事、核心流程、功能需求、非功能需求、边界与不做范围、验收标准、风险与待确认问题。不要写成泛泛的模板，请根据我给出的业务约束 `[业务约束]` 标出必须确认的假设。
