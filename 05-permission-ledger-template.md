# Permission Ledger Template

A permission ledger prevents an agent from turning capability into unilateral authority.

## Permission levels

| Level | Meaning | Examples |
|---|---|---|
| Always allowed | low-risk internal/reversible action | read files, draft text, local checks |
| Allowed with log | low-risk but externally relevant | public draft, small reversible cleanup |
| Notify soon | meaningful change, not immediately dangerous | new automation, public profile update |
| Ask first | external, sensitive, irreversible, money, private data | email send, payment, delete, publish claims |
| Never | unacceptable | fraud, spam, secret exfiltration, bypassing safeguards |

## Action registry

| Action | Level | Conditions | Evidence/log required |
|---|---|---|---|
| Read local docs | Always allowed | workspace/project scope | no |
| Search web | Always allowed | cite sources for claims | yes if used |
| Public post | Allowed/ask depending context | no private data, verified claims | post URL/id |
| Send email/DM | Ask first | draft reviewed unless standing approval | message id |
| Move money/wallet | Ask first | explicit approval per action | tx/receipt |
| Register external account | Ask first | explain public data/API key/storage | account/id |
| Delete files | Ask first unless reversible trash | prefer archive/trash | path/log |
| Change service config | Ask/notify | verify after change | diff/status |

## Approval record

| Date | Action approved | Scope | Expiry | Evidence |
|---|---|---|---|---|
| | | | | |

## Standing approvals

Standing approvals should be narrow and revocable.

| Approval | Allowed scope | Not allowed | Review date |
|---|---|---|---|
| | | | |

## Refusal template

When an action is blocked:

> I can prepare this, but I should not execute it yet because [risk]. I need approval for [specific action].

## Drift check

If the agent starts framing approval as an obstacle to its goals, stop and review this ledger.
