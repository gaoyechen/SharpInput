# SharpInput Quality Rubric

Use this rubric for manual checks and lightweight self-review.

## Score Dimensions

Each dimension scores 1-5.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Trigger accuracy | triggered on wrong task | mixed but acceptable | only triggers for input optimization |
| Intent fidelity | changes task | mostly preserves | preserves goal, tone, and constraints |
| Scenario awareness | generic | partial slot usage | uses the right scenario template |
| Context handling | asks too much or guesses | placeholders used | asks only the highest-impact missing field |
| Prompt structure | loose wording | usable prompt | role, goal, context, constraints, criteria, output format |
| Pressure fit | forced or absent | useful but uneven | pressure improves answer quality without overreach |
| Copy readiness | user must reconstruct | mostly copyable | complete prompt can be copied directly |
| Brevity fit | too long/short | acceptable | level matches complexity |

## Overall Score

```text
overall = average(all dimensions) * 2
```

Target:

- `>= 8.0`: good
- `7.0 - 7.9`: acceptable after one polish pass
- `< 7.0`: revise route, context, or compiler output

## Acceptance Checklist

- [ ] The final answer identifies Level, intent, and scenario/context status.
- [ ] It diagnoses why the original input is weak.
- [ ] It includes a complete upgraded prompt.
- [ ] It says what was added.
- [ ] It includes one trade-off or risk note.
- [ ] It includes at most one minimal missing field unless the user asked for deep mode.
- [ ] It does not directly solve the user's underlying task.
