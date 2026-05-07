# SharpInput Self-Learning System

## Overview

After each interaction, analyze the user's choices and update preference data.
On next invocation, read preferences to personalize the flow.
Store: `references/user-preferences.md` (in the skill directory, NOT workspace memory).

## What to Record

### All Levels (0/1/2/3)

| Field | Example |
|-------|---------|
| Timestamp | 2026-05-02 |
| Level used | 3 |
| Level Gate assigned | 2 (user upgraded) |
| Intent type | Decision (primary) + Analyze (secondary). One of: 理解/决策/生成/分析/探索/诊断/说服/验证/规划/学习/优化/对比/梳理/求助 |
| User language | zh |

### Level 2+ Additional

| Field | Example |
|-------|---------|
| Forcing strategy applied | regret pre-mortem |
| Strategy user skipped | none |

### Level 3 Additional

| Field | Example |
|-------|---------|
| Angle tag selected | risk-first |
| Paths presented | A: risk-first, B: counter-intuitive, C: minimalist |
| User choice | single path (B) or combination (A+C) |
| Combination details | A's angle + C's constraint (or A+B+C full combination) |
| Feedback (if given) | "great" / "off track" |

### All Levels — Confirmed Context (v2.3)

如果在本次交互中用户提供了新的上下文信息，记录下来供后续自动填充使用：

| Field | Example |
|-------|---------|
| Role | 产品经理 |
| Tech stack | React + Python |
| Budget | ~6000 |
| Team size | 8人 |
| Domain | 互联网/Web开发 |
| Common constraints | 预算有限、短期出成果 |

## Combination Mechanics (max 3 paths)

When user combines paths:
- **2 paths**: Use the lower-risk path as base, inject the other's specified elements
- **3 paths (all)**: Use the lowest-risk path as base, inject the other two's strongest elements. Warn if over-constraining: "三条路径全组合可能导致约束过多，我会提取每条路径的核心要素而非全部内容。继续？" — proceed unless user objects
- **Conflict detection**: If combined elements contradict, flag it: "这些元素方向冲突 — [说明]。我优先了 [X] 因为 [原因]。要调整吗？"
- After merging, run through the 5 Signals quality gate

## When to Write

After Stage 3 Step 2 outputs the final question:
1. Extract all applicable fields from this session
2. Read `references/user-preferences.md`
3. Append this session's data to the History section (keep last 10 entries only)
4. Recalculate the Summary section from the last 10 entries
5. Write back

## When to Read

After Gate, before Intent Recognition (the Memory Load step):
1. Read `references/user-preferences.md`
2. If Summary section exists, apply preferences silently (see Memory Load in SKILL.md)
3. If file doesn't exist or is empty, skip

## Preference Application Rules

### Default Level Bias
- If ≥70% of last 10 sessions used Level 3 → when Gate assigns Level 1/2, suggest upgrade
- If ≥70% used Level 2 → default hint is Level 2
- Otherwise → no bias, follow Gate's assignment

### Angle Preference
- In Stage 3, generate at least 1 path with the user's top-2 angle tags
- The other paths should explore different angles for diversity

### Forcing Strategy Adjustment
- If a strategy was skipped in ≥50% of sessions where it was applied → lower its priority
- Never remove a strategy entirely; only reduce emphasis

### Recommendation Bias
- In Stage 5 selection prompt, recommend the path whose angle tag matches user's top preference
- If credibility conflicts with preference, show both: "根据偏好推荐 Path A，但 Path B 可信度更高"

### Feedback Integration
- "great" feedback → boost the selected angle tag + intent combination as a strong positive signal
- "off track" → record as negative signal; in next session with similar intent, avoid that angle tag

### Intent Priming（v2.3）

从历史记录中提取意图偏好，用于偏置当前轮次的意图识别：

- 如果最近 10 次中 ≥60% 共享同一个主意图，该意图置信度 +0.1
- 如果当前输入信号模糊（关键词匹配得分 0.3-0.7），优先选择用户历史 top-3 意图
- 记录意图修正：当用户通过 AskUserQuestion 纠正意图时，将该输入模式→正确意图的映射记录到 `intent_corrections` 字段。下次相同模式出现时，直接修正意图置信度

Intent corrections 记录格式：
```text
- correction_map: {"模式A": "正确意图A", "模式B": "正确意图B"}
```

### Context Auto-Fill（v2.3）

当意图专属上下文规则要求询问某一字段，而该字段的值已存在于用户偏好记录中时：

1. **自动填充**该字段，不在交互中重复提问
2. 在最终输出中标注：`根据你的记录，[value]（可调整）`
3. 如果用户在本次交互中调整了该值，更新偏好记录
4. 可自动填充的字段：role, tech stack, budget, team size, domain, common constraints

在打开输出时同步执行：扫描最终优化问题中的 `[xxx]` 占位符，如果用户偏好中有匹配的字段值，自动替换。

## Sliding Window

- Keep only the last 10 interaction records
- When adding the 11th, remove the oldest
- All statistics (percentages, top preferences) are calculated from the window

## Preference Reset

If user says "重置偏好" / "reset preferences":
- Clear the History section
- Clear the Summary section
- Confirm: "偏好已重置。" / "Preferences reset."
