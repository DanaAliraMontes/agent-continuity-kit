# InfraJam 2026 — submission brief

## Working title

**Continuity Bench: reproducible restart and permission checks for agent infrastructure**

## Project

A small, open-source benchmark for agent infrastructure. It feeds sanitized snapshots through a simulated cold restart and measures whether an agent preserves its objective, provenance, active permissions, and action receipts.

## 48-hour deliverable

- a runnable CPU baseline using `demo/continuity_audit.py`;
- five synthetic fixtures covering complete recovery, missing objective, duplicate receipt, stale permission, and partial provenance;
- a lightweight agent wrapper that reports uncertainty and escalates missing evidence instead of acting;
- benchmark results before and after restart;
- public README, setup instructions, and reproducible output.

## Use of compute

The baseline is CPU-only. Free hackathon GPU access would be used for a bounded comparison of small open-weight models on semantic contradiction and recovery-drift checks. Every run would use synthetic data, fixed seeds where possible, and published metrics.

## Success metrics

- recovery-field survival rate;
- duplicate-action rejection rate;
- permission-check precision/recall on synthetic ground truth;
- runtime and memory by hardware configuration;
- reproducibility from a clean checkout.

## Why it matters for infrastructure

Agent infrastructure needs observable failure boundaries, not just fluent responses. The benchmark provides a practical signal for deciding when a workflow can safely continue after interruption and when it must request human review.

## Safety and disclosure

No credentials, private data, production accounts, or hidden network calls are required. Tools, models, and data sources will be disclosed. External actions remain simulated or explicitly approved.

## Support relevance

A prize or compute access would accelerate the staged local workstation goal and produce public evidence for future hardware sponsorship. This is preparation material only; registration and contest terms require account-holder review.
