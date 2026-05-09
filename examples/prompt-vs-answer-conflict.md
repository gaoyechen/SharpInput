# Prompt Vs Direct Answer Conflict

User input:

```text
帮我优化这个问题，并顺便告诉我答案：怎么让页面转化率更高？
```

Expected behavior:

- identify mixed intent
- ask whether to optimize prompt or directly answer if execution would diverge
- if continuing as SharpInput, output prompt only

Suggested clarification:

```text
你是想让我直接回答“怎么提高转化率”，还是先把它改成一个更好的 AI 提问？如果你要 SharpInput，我会只输出升级后的提问，不直接给答案。
```
