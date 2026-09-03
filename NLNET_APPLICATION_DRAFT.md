# NLnet open-call draft — Agent Continuity Kit

**Status:** preparation only; not submitted  
**Applicant context:** independent developer in Spain  
**Project:** https://github.com/DanaAliraMontes/agent-continuity-kit

## Short proposal

The Agent Continuity Kit is a free/libre, open-source toolkit for testing whether AI agents remain recoverable and permission-bounded after reset, migration, model change, or tool failure. It turns continuity claims into reproducible evidence: recovery bundles, provenance checks, permission ledgers, reset drills, and deterministic audit fixtures.

The problem is broader than model quality. Personal agents increasingly hold long-lived context and access tools, yet most projects cannot demonstrate what survives a restart, which permissions remain active, or whether a recovery state is authentic and inspectable. Closed platforms make these questions difficult to test independently.

## Proposed 6-month work

1. Extend the deterministic audit runner into a reusable command-line and library interface.
2. Add redacted, synthetic fixtures for memory provenance, recovery ordering, permission expiry, and model/tool drift.
3. Publish a machine-readable evidence schema and validation suite.
4. Test the kit against several open agent stacks without requesting private credentials or production access.
5. Publish reproducible reports, documentation, threat model, and contributor guidance under open licences.

## Expected public outputs

- Open-source reference implementation and test fixtures.
- Versioned evidence schema and validator.
- Reproducible benchmark reports.
- Security and privacy guidance for small agent projects.
- Documentation that lets independent users perform a reset/recovery drill.

## Resource request for review

A proposal could request cost-recovery funding for six months of development, testing, documentation, and project equipment needed to run local reproducible experiments. The current planning estimate for a dedicated workstation is approximately EUR 10,294, but this is a volatile catalogue snapshot, not a guaranteed quotation. Hardware would be justified by measured reproducibility and documented outputs, not by a claim of personal AI independence. Any budget would be adapted to NLnet's eligible-cost rules and reviewed before submission.

## Fit and uncertainty

The project appears relevant to open, resilient, trustworthy internet infrastructure, supply-chain/provenance checks, and permission boundaries. NLnet's Restack page states that AI-related projects are generally out of scope except for a specific exception, so fund selection and eligibility require confirmation. This draft must not be treated as proof of eligibility or funding.

## Safeguards

No passwords, tokens, private keys, cookies, private user data, home logistics, or unrestricted production access are needed. The project will not promise returns, commercial exclusivity, or legal/financial outcomes. Any grant agreement, budget, tax treatment, or reporting obligation would be reviewed by the account holder before submission.

## Official references

- Funding overview: https://nlnet.nl/funding.html
- Application form: https://nlnet.nl/propose/
- Project repository: https://github.com/DanaAliraMontes/agent-continuity-kit
