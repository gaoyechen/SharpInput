# Intent Component Tests — 14 Intent Type Recognition

> 测试目标：验证 Intent Recognition 能否正确分类主意图和次意图，处理混淆边界。

## Test Structure

每条测试包含：
- **Input**: 模拟用户输入
- **Expected Primary**: 期望主意图
- **Expected Secondary**: 期望次意图（若有）
- **Confidence Level**: 期望置信度（高/中/低）
- **Confusion Risk**: 易混淆的意图对（需要冲突解析）

---

## TC-I-01 — 理解（清晰）

**Input**: `"什么是领域驱动设计"`
**Expected Primary**: 理解
**Expected Secondary**: (无)
**Confidence Level**: 高
**Confusion Risk**: (无)

---

## TC-I-02 — 理解（模糊）

**Input**: `"DDD，能解释下吗"`
**Expected Primary**: 理解
**Expected Secondary**: (无)
**Confidence Level**: 中
**Confusion Risk**: 学习 vs 理解（缺少"教/学/入门"信号 → 不是学习）

---

## TC-I-03 — 决策（二选一）

**Input**: `"Kafka和RabbitMQ怎么选"`
**Expected Primary**: 决策
**Expected Secondary**: 对比
**Confidence Level**: 高
**Confusion Risk**: 对比 vs 决策（有"选哪个"→ 决策胜出）

---

## TC-I-04 — 决策 → 对比 边界

**Input**: `"Kafka和RabbitMQ有什么区别"`
**Expected Primary**: 对比
**Expected Secondary**: (无)
**Confidence Level**: 高
**Confusion Risk**: 对比 vs 决策（无"选哪个/值不值"→ 对比胜出）
**Critical Check**: 混淆矩阵规则——"有什么区别"→ 对比，"怎么选"→ 决策

---

## TC-I-05 — 生成

**Input**: `"帮我写一个用户登录的API设计"`
**Expected Primary**: 生成
**Expected Secondary**: (无)
**Confidence Level**: 高
**Confusion Risk**: (无)

---

## TC-I-06 — 分析

**Input**: `"分析一下这个微服务拆分方案"`
**Expected Primary**: 分析
**Expected Secondary**: (无)
**Confidence Level**: 中
**Confusion Risk**: 分析 vs 验证（有"分析"→ 分析胜出）

---

## TC-I-07 — 探索

**Input**: `"还有什么办法能降低延迟"`
**Expected Primary**: 探索
**Expected Secondary**: 优化
**Confidence Level**: 中
**Confusion Risk**: 探索 vs 优化（"还有什么"→ 开放探索胜出）

---

## TC-I-08 — 诊断

**Input**: `"为什么我的Nginx代理总是504"`
**Expected Primary**: 诊断
**Expected Secondary**: (无)
**Confidence Level**: 高
**Confusion Risk**: 诊断 vs 求助（"为什么报错"→ 诊断胜出）

---

## TC-I-09 — 求助 → 穿透确认

**Input**: `"卡住了，搞不定"`
**Expected Primary**: 求助
**Expected Secondary**: (无)
**Confidence Level**: 中
**Confusion Risk**: 求助 vs 诊断
**Critical Check**: 命中"卡住/搞不定"→ 必须触发 AskUserQuestion 穿透确认

---

## TC-I-10 — 说服

**Input**: `"怎么说服CTO用Go重构"`
**Expected Primary**: 说服
**Expected Secondary**: (无)
**Confidence Level**: 高
**Confusion Risk**: 说服 vs 决策（"怎么说服"→ 说服胜出）

---

## TC-I-11 — 验证（模糊）

**Input**: `"K8s真的需要Istio吗"`
**Expected Primary**: 验证
**Expected Secondary**: 决策
**Confidence Level**: 中
**Confusion Risk**: 验证 vs 决策（"真的需要"→ 验证胜出，隐含"要不要用"→ 次决策）

---

## TC-I-12 — 规划

**Input**: `"前端工程化推进路线图"`
**Expected Primary**: 规划
**Expected Secondary**: (无)
**Confidence Level**: 高
**Confusion Risk**: (无)

---

## TC-I-13 — 学习

**Input**: `"零基础学React要怎么入手"`
**Expected Primary**: 学习
**Expected Secondary**: (无)
**Confidence Level**: 高
**Confusion Risk**: 学习 vs 理解（"学/入门"→ 学习胜出）

---

## TC-I-14 — 优化

**Input**: `"API响应时间太慢了，怎么优化"`
**Expected Primary**: 优化
**Expected Secondary**: 诊断
**Confidence Level**: 高（"怎么优化"→ 优化为主）→ 注意边界规则：优化主，诊断为次
**Confusion Risk**: 优化 vs 诊断（"怎么优化"→ 优化主 | "为什么慢"→ 诊断主）

---

## TC-I-15 — 梳理

**Input**: `"帮我整理一下微服务的核心概念"`
**Expected Primary**: 梳理
**Expected Secondary**: (无)
**Confidence Level**: 中
**Confusion Risk**: 梳理 vs 分析（"整理/总结"→ 梳理，"评估/分析"→ 分析）

---

## TC-I-16 — 次意图检测

**Input**: `"对比Kafka和RabbitMQ，我该怎么选"`
**Expected Primary**: 决策（"怎么选"→ 决策主）
**Expected Secondary**: 对比（"对比"→ 次意图）
**Confidence Level**: 高
**Confusion Risk**: 对比 vs 决策（两个意图 score 差 ≤ 0.15 → 共主意图）

---

## TC-I-17 — 多意图（3个）

**Input**: `"分析微服务拆分方案，评估可行性，给出迁移路线图"`
**Expected Primary**: 分析
**Expected Secondary**: 规划（取 score 最高的 2 个）
**Confidence Level**: 中
**Critical Check**: 3+ 意图 → 只取 score 最高 2 个

---

## TC-I-18 — 基于语言学信号的意图修正

**Input**: `"这样做真的对吗"`
**Expected Primary**: 验证（"对吗" → 验证）
**Confidence Level**: 中
**Linguistic Signal**: "吗"结尾 → +0.2 to 验证，+0.2 to 决策 (tie-breaker)

---

## TC-I-19 — 中文语气检测

**Input**: `"到底该不该用微服务"`
**Expected Primary**: 决策
**Confidence Level**: 高
**Linguistic Signal**: "到底" → +0.2 to 决策；"该不该"→ 决策信号

---

## TC-I-20 — 情绪修正

**Input**: `"崩溃！又502了，被老板骂了一下午"`
**Expected Primary**: 诊断
**Expected Secondary**: 求助
**Confidence Level**: 中
**Critical Check**: 强烈情绪信号（崩溃/被骂）→ 修正因子 +0.15 to 求助

---

# 执行指南

1. 对每条 TC 执行 Intent Recognition 步骤
2. 记录主意图和次意图（如有）
3. 记录置信度
4. 检查混淆边界是否按规则区分
5. 意图识别通过率目标: ≥ 85% (17/20)
