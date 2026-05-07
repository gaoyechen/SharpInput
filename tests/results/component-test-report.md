# SharpInput Component Test Report
**Generated**: 2026-05-07 18:31
**Skill Version**: v2.3

## Summary

| Suite | Label | TCs | Target | Status |
|-------|-------|-----|--------|--------|
| gate | Gate 分级 | 10 | 90% | defined |
| intent | 意图识别 | 20 | 85% | defined |
| context | 上下文补全 | 10 | 85% | defined |
| judge | Judge 审查 | 7 | 80% | defined |
| **Total** | | **47** | | |

## Execution Guide

Each suite contains standalone TC definitions. To execute:

1. Run SharpInput on each TC input
2. Record the component output for each TC
3. Compare against the TC's expected result
4. Track pass/fail in a results log

### Target Pass Rates
- **Gate 分级**: ≥ 90% (10 TCs)
- **意图识别**: ≥ 85% (20 TCs)
- **上下文补全**: ≥ 85% (10 TCs)
- **Judge 审查**: ≥ 80% (7 TCs)

## Suites

### Gate 分级
- **File**: `tests/component/gate-tests.md`
- **TCs**: 10
- **Target**: ≥ 90%
- **Status**: defined

### 意图识别
- **File**: `tests/component/intent-tests.md`
- **TCs**: 20
- **Target**: ≥ 85%
- **Status**: defined

### 上下文补全
- **File**: `tests/component/context-tests.md`
- **TCs**: 10
- **Target**: ≥ 85%
- **Status**: defined

### Judge 审查
- **File**: `tests/component/judge-tests.md`
- **TCs**: 7
- **Target**: ≥ 80%
- **Status**: defined

## Next Actions

- [ ] Run each TC against SharpInput manually
- [ ] Track pass/fail counts for each suite
- [ ] Update report when target pass rates are met
- [ ] Integrate into CI (GitHub Actions)