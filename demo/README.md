# Deterministic demo

This folder contains a small, dependency-free continuity audit that can run on CPU.

It accepts sanitized JSON through standard input and reports:

- whether an objective and recovery bundle exist;
- duplicate event and receipt identifiers;
- actions without an active permission;
- a reproducible score and check list.

It never calls an external model, network, account, or secret. The demo is intentionally modest: its purpose is to provide a verifiable public proof before adding optional semantic drift analysis or hosted compute.

These are static checks, not an execution or recovery engine. Distinct receipt IDs
can still describe the same action twice. Even a score of 100 does not establish
idempotency, successful recovery, or production safety. Input is not scanned for
secrets: use synthetic or sanitized data only. The output intentionally reports
`receipt_ids_unique` and `input_secret_scan_performed: false` rather than claiming
duplicate prevention or secret-free input.

Run the regression checks: `python -m unittest discover -s demo -p "test_*.py"`.

Example:

```text
echo '{"objective":"test","recovery_bundle":{"version":1},"events":[{"id":"e1","action":"review"}],"permissions":[{"action":"review","active":true}],"receipts":[{"id":"r1"}]}' | python demo/continuity_audit.py
```
