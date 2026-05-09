# SharpInput Regression Cases

Run these after changing `SKILL.md`, `AGENT.md`, subskills, or references.

For each case, verify:

- SharpInput triggers only for prompt/input improvement
- primary intent is correct
- scenario is correct or intentionally empty
- Level is reasonable
- final output contains a complete copy-ready prompt
- the response does not directly answer the underlying task
- missing fields are asked or represented as placeholders
- default-answer stress test is used only when useful

## Cases

| ID | Input | Expected |
|---|---|---|
| R1 | 帮我优化：我想买电脑，怎么问 AI？ | Level 1/2, scenario `computer_purchase`, slots for budget/use/constraints |
| R2 | 帮我优化：ChatGPT Plus 和 Claude Pro 选哪个？ | Level 2, intent 决策/对比, scenario `ai_subscription_choice`, pressure enabled |
| R3 | 这个页面看起来很乱，帮我改成好 prompt | Level 1/2, scenario `ui_review`, clarify "乱" into dimensions |
| R4 | 我要让 AI 写 PRD，怎么问？ | Level 1, scenario `prd_srs_generation`, output PRD structure |
| R5 | 帮我写一个 prompt 严格评审我的产品方案 | Level 3, intent 验证, Judge required |
| R6 | 帮我优化：做一个 SaaS dashboard demo | Level 1/2, scenario `frontend_demo_generation`, slots for user/task/interactions |
| R7 | 怎么学 RUP？帮我优化成 AI 提问 | Level 0/1, intent 学习, placeholders for level/goal/time |
| R8 | 把这个问题变强一点：我们应该重构吗？ | Level 2/3 depending risk, intent 决策/验证, pressure enabled |
| R9 | 直接帮我调这个 bug | SharpInput should not trigger; direct coding/debugging request |
| R10 | 帮我润色这段发给老板的话 | Trigger, likely Level 1, intent 说服/优化, no Judge |

## Failure Patterns

- outputs advice instead of upgraded prompt
- asks broad generic questions before producing anything
- forces "反共识" framing on simple prompts
- guesses scenario-specific facts
- omits output format from generation prompts
- gives Level 3 multi-path flow for a simple rewrite
