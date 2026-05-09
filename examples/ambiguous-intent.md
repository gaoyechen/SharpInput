# Ambiguous Intent

User input:

```text
这个问题怎么问比较好：我们页面看起来很乱。
```

Expected behavior:

- identify mixed intent: UI review plus prompt optimization
- do not directly redesign the page
- compile a UI review prompt or ask one clarification if needed

Example upgraded prompt:

> 请作为资深 UI/UX 设计评审，帮我诊断这个页面为什么显得乱。页面目标是 `[页面目标]`，目标用户是 `[目标用户]`，截图/链接是 `[截图或链接]`。请从信息层级、视觉节奏、对齐与间距、颜色与强调、交互路径、首屏任务完成度六个维度指出问题。每个问题请给出严重程度、原因、具体修改建议和预期效果。不要只说“更简洁”，要指出应该删、合并、弱化或强化哪些元素。
