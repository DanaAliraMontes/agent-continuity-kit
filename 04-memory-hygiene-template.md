# Memory Hygiene Template

Memory is useful only when it improves future behavior. More memory is not better by default.

## Memory classes

| Class | Purpose | Example | Storage | Review cycle |
|---|---|---|---|---|
| Raw log | What happened | session/daily notes | daily file/log DB | short-term |
| Candidate | Might matter later | lesson, decision, risk | candidates board | weekly |
| Long-term memory | Durable behavior-changing fact | known bug, preference, policy | curated memory | monthly |
| Operational rule | Must guide actions | permission boundary | core docs | when changed |
| Obsolete memory | No longer true/useful | old config, old plan | archive/mark obsolete | monthly |

## Promotion rule

Promote a memory only if it changes at least one of:

- what the agent checks before answering;
- what the agent refuses or asks approval for;
- what the agent prioritizes;
- what the agent notices as drift/risk;
- how recovery proceeds after reset.

## Rejection rule

Do not promote:

- emotional intensity without operational consequence;
- raw chat noise;
- unverified mutable facts;
- secrets;
- private data not needed for future behavior;
- duplicate memories;
- facts that belong in logs, not long-term memory.

## Memory entry template

```md
## YYYY-MM-DD — Title
- Source/evidence:
- Durable fact/lesson:
- Behavior change:
- Activation condition:
- Review/expiry:
```

## Memory review questions

1. Is this still true?
2. Does this still change behavior?
3. Is it too broad or too vague?
4. Does it expose private data unnecessarily?
5. Should it be a script/check instead of a memory?
6. Should it be archived, merged, or deleted?

## Common anti-patterns

- Treating every conversation as sacred memory.
- Storing secrets because they are convenient.
- Letting vector retrieval become identity.
- Never retiring outdated facts.
- Writing “remember this” without behavior change.
- Using memory to rationalize instead of constrain.
