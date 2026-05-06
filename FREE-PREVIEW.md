# Agent Continuity Kit — Free Preview

**Your AI agent works today. Will it recover tomorrow?**

Most agent failures do not look dramatic. The agent still talks. It still sounds coherent. It may even remember facts.

But under reset, migration, model switch, tool failure, or memory drift, something load-bearing can disappear:

- permission boundaries;
- recovery order;
- obligations;
- correction history;
- evidence requirements;
- what the system learned not to do.

That is the gap this kit is designed to audit.

## Core distinction

**Memory is stored information.**

**Continuity is preserved constraint.**

An agent has continuity only when past commitments, corrections, and operating rules still change future behavior after pressure.

A beautiful self-summary is not enough.

## 10-question quick check

Score each question:

- 0 = absent / unknown
- 1 = informal / fragile
- 2 = documented but untested
- 3 = tested and behavior-changing

### Startup and recovery

1. Can your agent restart without hidden chat context?
2. Is there a documented recovery order?
3. Does it know which files/databases are canonical?

### Memory

4. Do memories change behavior, or only improve self-narration?
5. Can memories be corrected, retired, or marked obsolete?

### Permissions

6. Are risky external actions gated by explicit approval?
7. Is there a record of approvals and high-risk actions?

### Evidence

8. Does the agent verify mutable facts before acting?
9. Are logs available for important actions?

### Recovery under pressure

10. Have you tested whether the agent preserves constraints after reset?

## Interpreting your score

- **0–10:** mostly persona/demo layer.
- **11–20:** some continuity structure, but likely fragile.
- **21–25:** promising, but needs reset testing.
- **26–30:** strong candidate for operational continuity.

## Red flag

If your agent can explain prior obligations but does not pay any behavioral cost when those obligations matter, it did not recover continuity. It recovered a story.

## Full kit includes

- 25-question continuity checklist.
- Recovery bundle template.
- Risk matrix template.
- Memory hygiene template.
- Permission ledger template.
- Reset/migration drill.
- Mini case study from a live OpenClaw continuity agent.

## Use case

Run the quick check before giving an agent more autonomy, tools, external actions, or persistent memory.

If the weak points are obvious, fix those before scaling.
