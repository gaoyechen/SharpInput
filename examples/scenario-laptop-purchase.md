# Scenario: Laptop Purchase

User input:

```text
帮我把“我想买电脑，怎么选”改成一个好 prompt。
```

Expected scenario:

- computer_purchase

High-impact slots:

- budget_range
- primary_use
- must_have_constraints

Example upgraded prompt:

> 我想买一台电脑。预算是 `[预算范围]`，主要用途是 `[办公/编程/设计/剪辑/游戏/学习]`，我最不能妥协的是 `[性能/便携/屏幕/续航/系统生态/售后]`。请根据这些条件给出 3 个档位的购买建议，并说明每个档位适合谁、不适合谁、最容易踩的坑、推荐配置下限和可以牺牲的配置。不要只列品牌，请给出判断框架和最终推荐。
