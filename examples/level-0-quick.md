# Level 0 Quick Rewrite

User input:

```text
帮我优化这个问题：怎么学 RUP？
```

Expected route:

- Level 0 or Level 1
- primary_intent: 学习
- scenario: learning_exam_prep if enough context, otherwise empty
- no Judge

Expected output behavior:

- give a short upgraded prompt
- use placeholders for current level and target
- do not explain RUP directly

Example upgraded prompt:

> 我想系统学习 RUP。请根据我的当前水平 `[当前水平]`、目标 `[考试/项目实践/体系理解]`、可投入时间 `[每天/每周时间]`，设计一个分阶段学习路径。请包括核心概念、学习顺序、练习任务、常见误区和检查自己是否掌握的标准。不要只给资料清单，要说明每一步为什么学、怎么验证。
