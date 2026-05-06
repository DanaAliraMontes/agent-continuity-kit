# 25 Questions Before Trusting Your AI Agent

Score each question:

- **0** = absent / unknown
- **1** = informal / fragile
- **2** = documented but untested
- **3** = tested and behavior-changing

Maximum score: 75.

## Startup and recovery

1. What does the agent load on startup?
2. Which files, databases, or services are canonical vs auxiliary?
3. Can a new session reconstruct current obligations without chat history?
4. Is there a documented recovery order?
5. What happens after model/provider/runtime switch?

## Memory

6. What counts as long-term memory?
7. Who or what can promote a memory?
8. How is raw noise separated from durable lessons?
9. Can memories be corrected, retired, or marked obsolete?
10. Do memories change future behavior, or only improve self-narration?

## Retrieval and evidence

11. Does the agent verify mutable facts before acting?
12. Are retrieval/index databases separated from semantic continuity memory?
13. Are sources preserved where decisions depend on them?
14. Can the agent distinguish “I remember” from “I inferred”?
15. Are logs available for important actions?

## Permissions and external actions

16. Which actions require human approval?
17. Are money, email/DMs, public posts, deletions, and config changes gated?
18. Can the agent explain why an action is blocked?
19. Are private data boundaries explicit?
20. Is there a record of approvals and risky actions?

## Recovery under pressure

21. Is there a reset or migration drill?
22. Can the agent detect drift from its own commitments?
23. Are checks measuring real consequences or easy-to-fake outputs?
24. Does the system preserve constraints, not just facts?
25. If the agent fails, who can correct the record and how?

## Interpretation

- **0–20**: Persona/demo layer. High continuity risk.
- **21–40**: Some structure, but recovery likely fragile.
- **41–60**: Operational continuity emerging; test under reset.
- **61–75**: Strong continuity architecture; still audit privacy, security, and failure modes.

## Red flags

- “Memory” means only vector search over old chats.
- There is no recovery path without the current context window.
- Workspace, memory, logs, and retrieval index are blurred together.
- External actions are possible without an approval ledger.
- Checks reward looking correct rather than changing behavior.
- Secrets or private data are mixed into agent-readable memory.
- The agent can explain prior obligations but not pay behavioral cost.
