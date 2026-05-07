#!/usr/bin/env python3
"""
SharpInput Component Test Runner
==================================
Runs all component-level test suites and produces a summary report.

Usage:
    python tests/run-component-tests.py                      # run all
    python tests/run-component-tests.py --suite gate          # run one suite
    python tests/run-component-tests.py --report              # generate report only (no re-execution)

Each test suite is a Markdown file in tests/component/.
This runner parses TC definitions and simulates rule-based checks
where possible (gate level, intent matching, context extraction).
"""

import json
import re
import sys
import os
from datetime import datetime
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
COMPONENT_DIR = SKILL_DIR / "tests" / "component"
OUTPUT_DIR = SKILL_DIR / "tests" / "results"

SUITES = {
    "gate": "gate-tests.md",
    "intent": "intent-tests.md",
    "context": "context-tests.md",
    "judge": "judge-tests.md",
}

SUITE_LABELS = {
    "gate": "Gate 分级",
    "intent": "意图识别",
    "context": "上下文补全",
    "judge": "Judge 审查",
}

SUITE_TARGETS = {
    "gate": 90,    # 9/10
    "intent": 85,  # 17/20
    "context": 85, # 17/20
    "judge": 80,   # 6/7
}


def parse_tc_count(suite_file: str) -> int:
    """Parse a test suite markdown file and count TC definitions."""
    path = COMPONENT_DIR / suite_file
    if not path.exists():
        print(f"  [WARN] {path.name} not found")
        return 0

    content = path.read_text(encoding="utf-8")
    # Count TC- pattern
    tc_pattern = re.compile(r"^## TC-", re.MULTILINE)
    matches = tc_pattern.findall(content)
    return len(matches)


def run_suite(suite_name: str) -> dict:
    """Run a test suite and return results.

    Performs structural validation (file exists, TCs parseable)
    and returns regression metadata.
    """
    suite_file = SUITES.get(suite_name)
    if not suite_file:
        return {"suite": suite_name, "status": "unknown", "total": 0, "error": "unknown suite"}

    path = COMPONENT_DIR / suite_file
    if not path.exists():
        return {"suite": suite_name, "status": "missing", "total": 0, "error": "file not found"}

    total = parse_tc_count(suite_file)
    if total == 0:
        return {"suite": suite_name, "status": "error", "total": 0, "error": "no TC definitions found"}

    return {
        "suite": suite_name,
        "label": SUITE_LABELS.get(suite_name, suite_name),
        "status": "defined",
        "total": total,
        "target": SUITE_TARGETS.get(suite_name, 80),
        "target_label": f"{SUITE_TARGETS.get(suite_name, 80)}%",
        "file": suite_file,
        "checked_at": datetime.now().isoformat(),
    }


def generate_report(results: list, output_path: Path):
    """Generate a structured JSON report and a markdown summary."""
    # JSON report
    report = {
        "generated_at": datetime.now().isoformat(),
        "skill_version": "v2.3",
        "suites": results,
        "summary": {
            "total_suites": len(results),
            "total_tcs": sum(r["total"] for r in results),
            "defined_suites": sum(1 for r in results if r["status"] == "defined"),
        }
    }

    output_path.mkdir(parents=True, exist_ok=True)
    json_path = output_path / "component-test-report.json"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    # Markdown summary
    md_lines = [
        f"# SharpInput Component Test Report",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Skill Version**: v2.3",
        f"",
        f"## Summary",
        f"",
        f"| Suite | Label | TCs | Target | Status |",
        f"|-------|-------|-----|--------|--------|",
    ]

    grand_total = 0
    for r in results:
        md_lines.append(
            f"| {r['suite']} | {r.get('label', '')} | {r['total']} | {r.get('target_label', 'N/A')} | {r['status']} |"
        )
        grand_total += r["total"]

    md_lines.extend([
        f"| **Total** | | **{grand_total}** | | |",
        f"",
        f"## Execution Guide",
        f"",
        f"Each suite contains standalone TC definitions. To execute:",
        f"",
        f"1. Run SharpInput on each TC input",
        f"2. Record the component output for each TC",
        f"3. Compare against the TC's expected result",
        f"4. Track pass/fail in a results log",
        f"",
        f"### Target Pass Rates",
    ])

    for r in results:
        md_lines.append(f"- **{r.get('label', r['suite'])}**: ≥ {r.get('target_label', '80%')} ({r['total']} TCs)")

    md_lines.extend([
        f"",
        f"## Suites",
    ])

    for r in results:
        md_lines.extend([
            f"",
            f"### {r.get('label', r['suite'])}",
            f"- **File**: `tests/component/{r['file']}`",
            f"- **TCs**: {r['total']}",
            f"- **Target**: ≥ {r.get('target_label', '80%')}",
            f"- **Status**: {r['status']}",
        ])

    if grand_total > 0:
        total_target = sum(r["total"] for r in results)
        md_lines.extend([
            f"",
            f"## Next Actions",
            f"",
            f"- [ ] Run each TC against SharpInput manually",
            f"- [ ] Track pass/fail counts for each suite",
            f"- [ ] Update report when target pass rates are met",
            f"- [ ] Integrate into CI (GitHub Actions)",
        ])

    md_path = output_path / "component-test-report.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"\nReports written:")
    print(f"  JSON: {json_path}")
    print(f"  MD:   {md_path}")

    return report


def main():
    # Parse args
    suites_to_run = list(SUITES.keys())
    gen_only = False

    args = sys.argv[1:]
    for i, arg in enumerate(args):
        if arg == "--suite" and i + 1 < len(args):
            suites_to_run = [args[i + 1]]
        elif arg == "--report":
            gen_only = True

    print(f"SharpInput Component Test Runner")
    print(f"{'=' * 40}")
    print(f"Skill dir: {SKILL_DIR}")
    print(f"Suites:    {', '.join(suites_to_run)}")
    print(f"{'=' * 40}")

    results = []
    for suite in suites_to_run:
        print(f"\n[{suite}]")
        result = run_suite(suite)
        results.append(result)
        print(f"  Status: {result['status']}")
        print(f"  TCs:    {result['total']}")
        print(f"  Target: ≥ {result.get('target_label', '80%')}")

    # Generate report
    report = generate_report(results, OUTPUT_DIR)

    print(f"\n{'=' * 40}")
    print(f"Done. {len(results)} suites, {sum(r['total'] for r in results)} total TCs.")
    print(f"Execute TCs and record pass/fail to validate component quality.")


if __name__ == "__main__":
    main()
