# CHIA × A³ submission brief

## Working title

**Continuity Loop: reproducible recovery tests for AI agents**

## One-sentence pitch

A small, open-source evaluation loop that tests whether an AI agent preserves its objective, evidence, permissions, and action receipts after a simulated cold restart.

## Problem

Agent demos often rely on warm context. They may appear coherent while losing the state needed to recover safely after restart, migration, tool failure, or human handoff. This makes agent behaviour difficult to reproduce and audit.

## Proposed loop

1. Load a sanitized JSON snapshot containing an objective, timestamped events, permissions, receipts, and a recovery bundle.
2. Remove ephemeral state to simulate a cold restart.
3. Reconstruct the agent's working state from the recovery bundle only.
4. Check objective presence, event/receipt uniqueness, active permissions, and duplicate-action prevention.
5. Emit a machine-readable report with pass/fail checks, score, and evidence references.
6. Repeat across several snapshots to measure recovery drift.

The first implementation is deterministic and dependency-free. Optional model-assisted semantic checks are a later experiment, not a hidden requirement.

## Why it is useful

- Reproducible: the same input produces the same checks.
- Safe: no network, accounts, production data, or secrets.
- Open: code, synthetic fixtures, and evaluation criteria are public.
- Practical: the result identifies a fix-first continuity failure rather than rewarding fluent text alone.

## Existing implementation

- demo/continuity_audit.py — deterministic evaluator.
- examples/audit-output-sample.md — synthetic failure example.
- 01-continuity-checklist.md — 25-question checklist.
- 02-recovery-bundle-template.md — recovery input structure.
- 03-risk-matrix-template.md — risk classification.
- 05-permission-ledger-template.md — action permissions and receipts.
- 06-reset-drill.md — manual cold-start test.

## Evaluation plan

We will publish at least five synthetic fixtures:

- complete recovery;
- missing objective;
- duplicate receipt;
- stale permission;
- partial recovery with missing provenance.

Metrics:

- check accuracy against fixture ground truth;
- duplicate-action rejection rate;
- recovery-field survival rate;
- runtime and memory on CPU;
- optional comparison of small open-weight models when compute is available.

## Hardware/compute request

The project can run its baseline on CPU. Additional compute would be used only for a measurable extension: comparing small open-weight models for semantic contradiction and drift detection across repeated resets. The request is for reproducible evaluation capacity, not a claim that a GPU is required for the baseline.

## Prize and support use

Any prize, compute credit, or hardware support would be used for the staged local workstation and public continuity research, with accepted support recorded transparently in SUPPORT.md. No investor return, exclusivity, or private access is promised.

## Disclosure

This document is a preparation brief, not an official submission. Registration, identity verification, tax forms, prize acceptance, and any legal terms require review by the account holder before submission.
