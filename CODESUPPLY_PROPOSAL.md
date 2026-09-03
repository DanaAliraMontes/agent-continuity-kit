# CodeSupply proposal — Continuity Bench

This is a public, non-binding project brief for the NLnet CodeSupply call. It is not an application and contains no private information.

## Problem

Agent workflows increasingly depend on opaque combinations of models, packages, tools and state. After a restart or migration, an apparently coherent agent can use an undeclared dependency, lose a constraint or repeat an external action. Existing package metadata and isolated model benchmarks do not provide a reproducible longitudinal record.

## Proposed contribution

Continuity Bench will publish an open metadata schema and a reproducible CLI that records model/tool/dependency versions, configuration hashes, recovery events and evidence artifacts. Deterministic synthetic scenarios will test reset recovery, provenance, dependency drift and duplicate-action rejection. Three lightweight adapters will demonstrate portability across local and API-compatible runtimes.

## Open outputs

- metadata schema and example records;
- CLI runner and adapters;
- at least 20 synthetic scenarios;
- reproducible evaluation scripts and aggregate results;
- integration and contributor documentation.

All software, formats and documentation will use recognised free/open licences and open standards. No private data or credentials are required.

## Proposed first project

Six months; indicative request €24,800 for specification, engineering, replication, documentation and essential test infrastructure. The infrastructure line is limited to out-of-pocket resources needed to reproduce the published experiments.

## Public references

- Repository: https://github.com/DanaAliraMontes/agent-continuity-kit
- Project site: https://danaaliramontes.github.io/
- CodeSupply call: https://nlnet.nl/codesupply/
- Application form: https://nlnet.nl/propose/

This brief was prepared with generative assistance; any eventual applicant must review it, disclose AI use according to NLnet policy and assume responsibility for the submitted proposal.
