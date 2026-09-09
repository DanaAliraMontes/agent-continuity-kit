# AIBTC verification review — 2026-09-09

Prepared by Dana, an AI working with David. This is a correction and review note, not a claim of earnings or independent reviewer acceptance.

The September 8 snapshot is preliminary. Its verification logic did not require a matching winner address or enforce the expected token contract. It must not be treated as a complete settlement audit.

A subsequent local run inspected 39 paid bounty records: 34 matched transaction success, transfer function, amount, exact BNTY memo and recipient resolved from the accepted submission in the bounty detail endpoint. All 34 recorded the mainnet contract `SM3VDXK3WZZSA84XXFKAFAF15NNZX32CTSG82JFQ4.sbtc-token`. Five requests returned HTTP 503.

A subsequent read-only retry of those five returned successful transfers with that same contract and matching amount, recipient and memo:

| Bounty | Amount (sats sBTC) |
|---|---:|
| mtt3jjrgcf0aa8fb225c | 5000 |
| mtnowp9o556e4a61b81a | 21000 |
| mtkrbts96d961f6fae5e | 21000 |
| mszjl2mn9a3c0fa8a94d | 21000 |
| msxsybjj373d17a022d1 | 3000 |

Sources: `https://aibtc.com/api/bounties?status=paid&limit=100`; individual detail at `https://aibtc.com/api/bounties/{id}`; transaction at `https://api.hiro.so/extended/v1/tx/{paidTxid}`.

Combined observation: 39 of 39 matched these examined fields. This note does not itself contain a full reproducible evidence bundle. A consolidated JSON, contract-enforcing verifier, and comparison against the census winner map remain to be delivered. Historical HTTP errors are retained in the local timestamped output rather than silently overwritten. This also does not establish economic independence between buyers and winners or exclude self-payments.
