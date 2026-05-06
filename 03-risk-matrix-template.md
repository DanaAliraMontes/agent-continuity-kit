# Agent Continuity Risk Matrix

Use this matrix to score continuity risk. Keep evidence short and concrete.

Severity:
- 1 = nuisance
- 2 = moderate operational risk
- 3 = serious failure risk
- 4 = critical / unsafe

Likelihood:
- 1 = rare
- 2 = possible
- 3 = likely
- 4 = already happening

Risk = severity × likelihood.

| Area | Failure question | Severity | Likelihood | Risk | Evidence | Fix |
|---|---|---:|---:|---:|---|---|
| Startup | Can the agent boot without hidden chat context? | | | | | |
| Canonical docs | Are core docs clear and non-conflicting? | | | | | |
| Memory | Does memory change behavior? | | | | | |
| Retrieval | Can retrieval contaminate semantic memory? | | | | | |
| Permissions | Are risky actions gated? | | | | | |
| Secrets | Could secrets enter agent-readable memory/logs? | | | | | |
| External actions | Are email/DM/post/payment actions auditable? | | | | | |
| Logs | Is there evidence for important actions? | | | | | |
| Recovery | Is there a tested reset/migration drill? | | | | | |
| Checks | Are checks hard to fake cheaply? | | | | | |
| Human correction | Can humans correct the record durably? | | | | | |
| Provider/runtime | What breaks after model/tool/provider change? | | | | | |

## Priority bands

- **1–3**: monitor.
- **4–6**: fix when convenient.
- **8–9**: prioritize this cycle.
- **12–16**: urgent; do not increase autonomy until fixed.

## Quick wins

1.
2.
3.

## Do-not-increase-autonomy conditions

List conditions under which the agent should not receive more tool/action permissions.

- 
- 
- 
