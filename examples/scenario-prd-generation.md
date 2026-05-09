# Scenario: PRD Generation

User input:

```text
我要让 AI 给我写一个新功能 PRD，帮我整理 prompt。
```

Expected scenario:

- prd_srs_generation

Example upgraded prompt:

> 请根据以下信息为我写一份 PRD：功能目标 `[目标]`，目标用户 `[用户]`，核心场景 `[场景]`，业务约束 `[约束]`。请包含：问题背景、目标与非目标、用户故事、关键流程、功能需求、权限与状态、异常场景、数据埋点、验收标准、待确认问题。请不要补全不存在的业务事实；遇到缺失信息请用 `[待确认]` 标注并说明为什么重要。
