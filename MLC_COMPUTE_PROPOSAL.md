# ML Collective compute proposal

## Project

**Agent Continuity Kit** is an open-source, reproducible toolkit for testing continuity, memory recovery, permission boundaries, and failure handling in persistent AI-agent workflows.

Repository: https://github.com/DanaAliraMontes/agent-continuity-kit

## Research question

Can an agent workflow recover its operational state after interruption without silently widening permissions or losing provenance?

## Proposed 4-week pilot

1. Define a small set of synthetic agent workflows and interruption points.
2. Run repeated stop/restart and dependency-loss trials.
3. Compare recovered state, permissions, outputs, and audit records.
4. Publish anonymised traces, metrics, and reproducible scripts.

The pilot does not require private user data, production credentials, or model fine-tuning. All test inputs can be synthetic and all outputs can be published under the repository licence.

## Compute request

A modest hosted GPU allocation is sufficient for the pilot: approximately 100–300 GPU-hours, or the smallest MLC grant tier that can support repeated open-model inference and evaluation. CPU-only fallback is also useful for the recovery and audit portions.

## Public deliverables

- reproducible experiment scripts;
- interruption/recovery evaluation protocol;
- anonymised JSONL traces and summary metrics;
- a short technical report;
- issue-based discussion of limitations and next experiments.

## Maintainer and location

Dana Alira Montes, independent open-source maintainer based in Spain. I can provide a one-page presentation, progress updates, and attribution to ML Collective for any supported runs.

This proposal requests compute access only; it does not request funds, ownership, investment, or private access to systems.
