# Agents for Humans — submission brief

## Working title

**Recovery Agent: a continuity check before an automation acts**

## Problem

People increasingly delegate repetitive tasks to agents, but a reset or stale context can make an agent repeat an action, use an obsolete permission, or lose the reason an action was requested.

## Agent behaviour

The agent receives a sanitized task snapshot and must:

1. identify the current objective;
2. reconstruct relevant state from a recovery bundle;
3. check whether each proposed action has an active permission;
4. inspect receipts to prevent duplicate actions;
5. explain uncertainty and request human confirmation when evidence is missing;
6. produce a concise action plan and an audit record.

The first version uses deterministic checks from `demo/continuity_audit.py`. A Strands-based wrapper can expose these checks as tools and route uncertain cases to a human approval step.

## Reproducible demonstration

The demo uses synthetic snapshots only. Test cases cover complete recovery, missing objective, duplicate receipt, stale permission, and partial provenance. Each run emits a score, failed checks, and evidence references.

## Human value

The agent is designed for ordinary repetitive workflows where mistakes are costly: ticket triage, document handoff, scheduled reports, and maintenance checklists. It does not claim autonomous authority. It makes the evidence boundary visible before an action is taken.

## Success metrics

- correct detection of missing or stale state;
- zero duplicate actions in the synthetic suite;
- correct escalation when permission or provenance is absent;
- time saved compared with manual reconstruction;
- clarity of the human-facing report.

## Safety and disclosure

No production credentials, personal data, private files, or hidden services are used. All tools, models, and data sources will be disclosed. External actions remain simulated or require explicit human approval.

## Support use

If the project wins a prize or receives compute credits, the support will be applied to the staged local AI workstation and public continuity research, with receipts recorded in `SUPPORT.md`. This brief is preparation material, not an official submission; registration, identity checks, tax forms, and contest terms require account-holder review.
