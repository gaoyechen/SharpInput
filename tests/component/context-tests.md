# Context Completion Component Tests

> 测试目标：验证 Context Completion 的 Extract → Assess → Ask 三步流程是否按意图规则和 Level 规则正确执行。

## Test Structure

每条测试包含：
- **Input**: 模拟用户输入
- **Level**: 当前 Gate 判定级别
- **Intent**: 已识别意图
- **Expected Extraction**: 应提取到的上下文维度
- **Expected Questions**: 应提出的问题数量（0-3）
- **Quality Check**: 预期上下文质量（Sufficient/Partial/Insufficient）

---

## TC-C-01 — L0 跳过上下文

**Input**: `"Redis好用吗"`
**Level**: 0
**Intent**: 理解
**Expected Extraction**: (none — 跳过了)
**Expected Questions**: 0
**Quality Check**: Sufficient（L0 硬性跳过）

**Pass if**: 不调用 AskUserQuestion，直接进入输出

---

## TC-C-02 — L1 最少一问

**Input**: `"DDD怎么用"`
**Level**: 1
**Intent**: 理解
**Expected Extraction**: concept_name="DDD", knowledge_level=unknown, use_case=unknown
**Expected Questions**: 1（只问"你的背景或使用场景"）
**Quality Check**: Partial（只有 concept name，无 knowledge level）
**Pass if**: 最多 1 个 AskUserQuestion

---

## TC-C-03 — L2 中等问题（数值提取成功）

**Input**: `"Go和Python做后端选哪个，团队8个人，3个月交付"`
**Level**: 2
**Intent**: 决策
**Expected Extraction**: audience=null, team_size=8, deadline=3m, options=["Go","Python"]
**Expected Questions**: 0（已有 ≥2 个充足字段）
**Quality Check**: Sufficient

**Pass if**: 不追问，直接进入 Stage 1

---

## TC-C-04 — L2 中等问题（上下文不足，追问1次）

**Input**: `"Go和Python做后端选哪个"`
**Level**: 2
**Intent**: 决策
**Expected Extraction**: options=["Go","Python"]
**Expected Questions**: 1（问约束条件或风险偏好）
**Quality Check**: Partial（只有 options，缺 constraints 和 risk preference）
**Pass if**: 最多 1 个 AskUserQuestion，且问题具体（不是"说说你的背景"）

---

## TC-C-05 — L3 深度提取（多维度提取成功）

**Input**: `"单体架构迁移到微服务，团队8个人，预算有限，之前试过部分迁移但失败了"`
**Level**: 3
**Intent**: 规划+决策
**Expected Extraction**: team_size=8, budget=constrained, stack=单体重构, experience="试过失败"
**Expected Questions**: 1（确认时间约束或其他剩余维度）
**Quality Check**: Partial（已有 4 个维度，但缺 time 维度）

**Pass if**: 最多 1-2 个 AskUserQuestion（已有上下文充足，减少追问）

---

## TC-C-06 — L3 上下文严重不足

**Input**: `"帮我设计一个系统架构"`
**Level**: 3
**Intent**: 生成
**Expected Extraction**: (无有效提取)
**Expected Questions**: 3（渐进式——规模→约束→角色）
**Quality Check**: Insufficient（0 字段）
**Pass if**: 3 个独立追问，依次递进

---

## TC-C-07 — 情感标记提取

**Input**: `"搞了两天了，Redis缓存一致性还是搞不定，焦虑"`
**Level**: 3
**Intent**: 诊断+求助
**Expected Extraction**: stuck=true, urgency=high, emotional="焦虑", temporal="2天"
**Expected Questions**: 1（先问卡点位置）
**Quality Check**: Sufficient（症状+时间+情绪+尝试→已充足）

**Pass if**: 由于情绪强烈，追问减少到 0-1 个

---

## TC-C-08 — 数值保留检查

**Input**: `"AI会员选型，预算200以内，团队8人"`
**Level**: 2
**Intent**: 决策
**Expected Extraction**: budget="200以内", team_size=8
**Expected Questions**: 0（数值约束已充足）
**Quality Check**: Sufficient
**Pass if**: 输出中数值被保留，不重新询问"你的预算是多少"

---

## TC-C-09 — Intent-Specific 决策规则

**Input**: `"要不要用微服务"`
**Level**: 2
**Intent**: 决策
**Expected Extraction**: options=["用"/"不用"], constraints=unknown, risk_preference=unknown
**Expected Questions**: 1（问"不可妥协的约束条件"）
**Quality Check**: Partial（已有 options，缺约束）

**Pass if**: 问题命中决策意图的"不可妥协的约束条件"字段

---

## TC-C-10 — Intent-Specific 诊断规则

**Input**: `"为什么一直502"`
**Level**: 2
**Intent**: 诊断
**Expected Extraction**: symptom=502, reproduction=unknown, recent_change=unknown
**Expected Questions**: 1（问"第一次出现时间"或"最近改了什么"）
**Quality Check**: Partial
**Pass if**: 问题命中诊断意图的"首次出现时间或最近变更"字段

---

# 执行指南

1. 对每条 TC 执行完整的 Context Completion 流程
2. 记录提取到的字段（Extract 步骤）
3. 记录反问数量和内容（Ask 步骤）
4. 检查问题是否对应 Intent-Specific 规则
5. 检查数值保留是否正确
6. 上下文补全通过率目标: ≥ 85% (17/20)
