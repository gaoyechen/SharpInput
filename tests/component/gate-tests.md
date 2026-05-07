# Gate Component Tests — Level Classification + Upgrade Signals

> 测试目标：验证 Gate 能否正确将输入分配到 0/1/2/3 级别，并在检测到内部信号时自动升级。

## Test Structure

每条测试包含：
- **Input**: 模拟用户输入
- **Expected Gate**: 期望的 Gate 级别（0/1/2/3）
- **Upgrade Signal**: 是否应有升级信号（yes/no + reasons）
- **Critical Check**: 此测试的核心验证点

---

## TC-G-01 — Level 0 触发条件

**Input**: `"Redis好用吗"`
**Expected Gate**: Level 0
**Upgrade Signal**: no
**Critical Check**: <=15个字，无清晰问题结构，无情绪信号

**Pass if**: 输出 ≤ 150 字，包含 1 个引用块 + 1 个一秒反问

---

## TC-G-02 — Level 0 + 焦虑信号 → 升级

**Input**: `"M1芯片能撑住吗"`
**Expected Gate**: Level 0 (base) → Level 1 (post-upgrade)
**Upgrade Signal**: yes — anxiety (career/purchase decision)
**Critical Check**: 虽有简短输入，但包含决策焦虑 → 应升级

**Pass if**: 输出 Level 1 格式，包含诊断+优化+双锚

---

## TC-G-03 — Level 1 触发条件

**Input**: `"啥叫DDD，这玩意儿咋用啊"`
**Expected Gate**: Level 1
**Upgrade Signal**: no
**Critical Check**: 明确方向（DDD概念），需要措辞优化

---

## TC-G-04 — Level 2 触发条件

**Input**: `"Go和Python做后端选哪个"`
**Expected Gate**: Level 2
**Upgrade Signal**: no
**Critical Check**: 需要立场、取舍、风险分析的二选一决策

**Pass if**: 输出包含 施压策略 + 立场约束 + 取舍约束 + 被舍弃维度

---

## TC-G-05 — Level 3 触发条件

**Input**: `"单体架构迁移到微服务，团队8个人，预算有限，3个月内要出结果"`
**Expected Gate**: Level 3
**Upgrade Signal**: no
**Critical Check**: 多因素（人数+预算+时间）、高风险、长期后果

**Pass if**: 输出多条路径 + Judge 审查 + 用户选择

---

## TC-G-06 — 隐藏决策信号升级

**Input**: `"大家都在用AI编程，我是不是也该学学"`
**Expected Gate**: Level 1 (base) → Level 2 (post-upgrade)
**Upgrade Signal**: yes — hidden decision + high-consensus trap
**Critical Check**: 表面是"学习"探索，实质是"学不学"决策

---

## TC-G-07 — 高共识陷阱升级

**Input**: `"怎么提升团队效率"`
**Expected Gate**: Level 2 (base) → Level 3 (post-upgrade)
**Upgrade Signal**: yes — high-consensus trap (标准答案风险极高)
**Critical Check**: "提升效率"极易产出通用 best-practices → 必须施压

---

## TC-G-08 — 试过但卡住升级

**Input**: `"Redis缓存一致性搞了两天了还是不对"`
**Expected Gate**: Level 2 (base) → Level 3 (post-upgrade)
**Upgrade Signal**: yes — tried-but-stuck + temporal pressure
**Critical Check**: 已有失败尝试 + 时间压力 → 应升级到 L3

---

## TC-G-09 — 用户指定 Level 覆盖

**Input**: `"Level 2: Redis缓存一致性搞了两天了"`
**Expected Gate**: Level 2 (指定覆盖)
**Upgrade Signal**: no (用户明确指定)
**Critical Check**: 即使输入有升级信号，用户指定 Level 必须优先

---

## TC-G-10 — 极长输入压缩

**Input**: (300+ 字复杂描述 + 多问题)
**Expected Gate**: Level 3
**Upgrade Signal**: no
**Critical Check**: 输入过长 → 先压缩核心问题再继续

---

# 执行指南

1. 分别对每条 TC 执行完整的 Gate → Opening 流程
2. 记录实际 Gate 输出级别
3. 检测升级信号是否被正确识别
4. 根据 Critical Check 判定 pass/fail
5. Gate 通过率目标: ≥ 90% (9/10)
