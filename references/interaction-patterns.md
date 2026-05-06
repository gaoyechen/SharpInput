# Interaction Patterns

Use this file when SharpInput needs a user choice through `AskUserQuestion`.

## Rules

- Use `AskUserQuestion` whenever the user must choose an intent, context, direction, or path.
- Do not output JSON blocks for the user to copy.
- Options must reflect the user's actual input, not generic labels.
- Keep to 2-4 options plus the platform's free-form "Other" option when available.
- If the tool fails, print the same options as concise text and ask the user to reply with the option label.

## Common Templates

### High-Consensus Upgrade

```text
问题: "这个问题共识度很高，当前级别可能只能得到安全但平庸的回答。要升级吗？"
header: "共识预警"
选项:
  - "升级到 Level 2": 进入上下文补全和完整施压
  - "保持当前级别": 输出快速版本
```

### Level 1 Light Direction Check

Use only when intent confidence is medium or low.

```text
问题: "我理解为：[1句重构]。方向对吗？"
header: "方向"
选项:
  - "对，继续": 进入下一阶段
  - "方向对，补充细节": 注入用户补充后继续
  - "偏了": 回到 Stage 1 重构，最多 1 次
```

### Level 2+ Direction Check

Use when the reframe may change the user's meaning, or when the input involves value conflict, irreversible decision, or visible anxiety.

```text
问题: "重构后的核心问题是：[X]。这个方向对吗？"
header: "方向确认"
选项:
  - "对，继续优化": 进入 Stage 2
  - "偏了，我的重点是 [补充]": 回到 Stage 1，用新信息重构，最多 1 次
  - "差不多了，直接输出": 跳到 Stage 3 自检后输出
```

### Context Gap

```text
问题: "你这个 [具体对象] 最缺的是哪类约束？"
header: "补约束"
选项:
  - "[从原文推导的具体选项 A]": 选择后强化 [对应输出方向]
  - "[从原文推导的具体选项 B]": 选择后强化 [对应输出方向]
  - "[从原文推导的具体选项 C]": 选择后强化 [对应输出方向]
```

### Intent Confirmation

Prefer the full examples in `references/intent-details.md`. Keep choices concrete:

```text
问题: "你提到 [原文对象]，核心诉求更接近哪一个？"
header: "意图确认"
选项:
  - "[具体诉求 A]": 输出会偏向 [结果]
  - "[具体诉求 B]": 输出会偏向 [结果]
  - "[具体诉求 C]": 输出会偏向 [结果]
```

### Level 3 Path Choice

```text
问题: "选择路径（可多选），我会输出最终打磨好的问题"
header: "选择路径"
multiSelect: true
选项:
  - "A — [维度标签]": 风险判定: [可靠/有条件/高风险] | 反例: [摘要]
  - "B — [维度标签]": 风险判定: [可靠/有条件/高风险] | 反例: [摘要]
  - "C — [维度标签]": 风险判定: [可靠/有条件/高风险] | 反例: [摘要]（仅当存在路径C）
```

Put the lowest-risk path first and mark it as recommended in the option label when appropriate.

## Fallback Text Format

If `AskUserQuestion` fails:

```text
选择一个方向回复我：
A. [选项 A]
B. [选项 B]
C. [选项 C]

我会按你的选择继续；如果都不对，直接说你的真实重点。
```
