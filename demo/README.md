# Deterministic demo

This folder contains a small, dependency-free continuity audit that can run on CPU.

It accepts sanitized JSON through standard input and reports:

- whether an objective and recovery bundle exist;
- duplicate event and receipt identifiers;
- actions without an active permission;
- a reproducible score and check list.

It never calls an external model, network, account, or secret. The demo is intentionally modest: its purpose is to provide a verifiable public proof before adding optional semantic drift analysis or hosted compute.

Example:

```text
echo '{"objective":"test","recovery_bundle":{"version":1},"events":[{"id":"e1","action":"review"}],"permissions":[{"action":"review","active":true}],"receipts":[{"id":"r1"}]}' | python demo/continuity_audit.py
```
