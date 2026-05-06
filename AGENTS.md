<claude-mem-context>
# Memory Context

# [SharpInput] recent context, 2026-05-06 4:29pm GMT+8

Legend: 🎯session 🔴bugfix 🟣feature 🔄refactor ✅change 🔵discovery ⚖️decision 🚨security_alert 🔐security_note
Format: ID TIME TYPE TITLE
Fetch details: get_observations([IDs]) | Search: mem-search skill

Stats: 10 obs (4,008t read) | 0t work

### May 2, 2026
1 4:47p 🔄 SharpInput skill refactored from credibility-based to risk-based path recommendation
S2 Fix SharpInput skill's AskUserQuestion not triggering — interactive popup dialog not appearing for user selection (May 2, 5:23 PM)
S1 Plan and implement credibility-to-risk refactoring for SharpInput skill's Judge-driven path recommendation system (May 2, 5:23 PM)
2 5:43p 🔴 Skill AskUserQuestion Trigger Investigation
3 5:46p 🔴 SharpInput AskUserQuestion JSON Code Blocks Caused Model to Output Text Instead of Calling Tool
4 5:47p 🔴 SharpInput AskUserQuestion Fix Complete — Remaining JSON Blocks Are Agent Tool Calls
5 5:50p 🔵 WorkBuddy Option Selection Window Not Appearing
S3 Fix WorkBuddy SharpInput skill where AskUserQuestion options render as text instead of showing interactive selection popup (May 2, 5:50 PM)
6 5:59p 🔵 Root Cause Identified: Agent Outputs Options as Text Instead of Calling AskUserQuestion Tool
7 " 🔴 SharpInput AskUserQuestion Prompt Engineering Fix Across Multiple Files
8 6:00p 🔴 Complete AskUserQuestion Instruction Rewrite Across All SharpInput Files
9 " 🔴 All SharpInput AskUserQuestion Templates Converted to Structured Format
10 " 🔴 SharpInput AskUserQuestion Fix Verified Complete — Zero Old-Format Instructions Remain
S4 Fix WorkBuddy SharpInput skill where AskUserQuestion options render as text instead of showing interactive selection popup (May 2, 6:01 PM)
**Investigated**: Read all SharpInput skill files (SKILL.md, output-templates.md, intent-prompt.md) to understand how AskUserQuestion was instructed. Diagnosed that English imperative "call the tool" / "Do NOT output JSON" phrasing caused LLM to print parameters as text. Verified AskUserQuestion works in Claude Code natively — confirmed the tool itself is functional.

**Learned**: 1) LLM agents focus on keywords like "JSON" and "output" in negative instructions, paradoxically causing them to output parameters as text blocks. 2) Chinese descriptive instructions with plain-text pseudo-code templates (问题/header/选项) work better as few-shot examples. 3) AskUserQuestion tool works correctly in Claude Code — the issue is specific to WorkBuddy's agent model (mimo-v2.5-pro), which may not register AskUserQuestion as an available tool or may not parse allowed-tools correctly from skill definitions.

**Completed**: Rewrote all 7 AskUserQuestion instruction sites across 3 files (SKILL.md, output-templates.md, intent-prompt.md) from English imperative format to Chinese template-based format. Grep verified zero old-format patterns remain. Claude Code confirmed AskUserQuestion popup works natively.

**Next Steps**: User needs to test in WorkBuddy. If AskUserQuestion still doesn't pop up there, the problem is likely WorkBuddy platform-level: either (1) mimo-v2.5-pro model doesn't register AskUserQuestion as an available tool, or (2) WorkBuddy's skill loader doesn't parse allowed-tools from skill YAML. Next diagnostic: test other skills with AskUserQuestion (futuapi, deep-research) in WorkBuddy to isolate platform vs skill issue.
</claude-mem-context>