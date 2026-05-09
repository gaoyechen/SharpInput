# Level 3 Judge

User input:

```text
我有一个产品改版方案，帮我写一个让 AI 严格评审它的 prompt。
```

Expected route:

- Level 3
- primary_intent: 验证
- scenario: product_plan_review
- Judge required
- multi-path acceptable

Example upgraded prompt:

> 请作为资深产品评审和增长负责人，严格评审下面的产品改版方案：`[方案内容]`。请不要默认支持我的方案。请从用户价值、业务目标、信息架构、实现成本、上线风险、数据验证、替代方案七个维度打分，并给出证据。必须指出：最可能失败的 3 个原因、能推翻方案的关键指标、低成本验证实验、保守推进路径和激进推进路径。最后给出明确结论：继续、缩小范围、重做，或暂缓。
