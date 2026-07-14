# Certification Exam: Claude Certified Architect – Foundations (CCAR-F)

The four course folders in this repo are the coursework. This file tracks how that coursework maps to the actual exam and what practice still needs to be added to cover the gaps.

## Exam at a glance

- Exam code: CCAR-F
- Format: 60 items (multiple-choice and multiple-response); 4 scenarios drawn from a bank of 6
- Time: 120 minutes
- Passing: scaled score of 720 on a 100 to 1,000 scale (criterion-referenced; not a raw percentage)
- Delivery: Pearson VUE, online proctored or a test center
- Fee: 125 USD. Validity: 12 months.
- Style: scenario-based judgment questions ("most effective", "most likely root cause"), not recall.

## Domain weights

| Domain | Weight |
|--------|--------|
| Agentic Architecture & Orchestration | 27% |
| Claude Code Configuration & Workflows | 20% |
| Prompt Engineering & Structured Output | 20% |
| Tool Design & MCP Integration | 18% |
| Context Management & Reliability | 15% |

## How the courses map to the exam

- Well covered by the courses: Tool Design & MCP (18%), Claude Code Configuration & Workflows (20%), Prompt Engineering & Structured Output (20%). About 58% of the exam sits in the material these notebooks already cover.
- Under-covered, needs added practice: Agentic Architecture & Orchestration (27%, the largest domain) and parts of Context Management & Reliability (15%). These lean on the Claude Agent SDK and production judgment that go beyond the course notebooks.

## Planned practice to add

Focused on the gap domains above. To build:

- A multi-agent Agent SDK project: an agentic loop driven by `stop_reason`, a coordinator plus subagents spawned via the `Task` tool, explicit context passing, and parallel subagent spawning.
- Hooks practice: `PostToolUse` result normalization and tool-call interception for deterministic enforcement (for example, blocking an action above a threshold and redirecting to escalation).
- Error propagation and escalation: structured error context, local recovery before escalation, and explicit escalation criteria.
- Session management: `--resume` and `fork_session`, and choosing between resuming and starting fresh with an injected summary.

Reference: the exam guide's Preparation Exercises 1 and 4 target these areas directly.

## Status and next steps

1. Take one or two practice exams from the companion repo, Tom's "Python for AI Consultants" (https://github.com/tfurland-la/Consulting-python), which scores against the exam's skill areas.
2. Use the results to identify the weakest domains.
3. Build targeted practice here for those areas and fine-tune from there.
