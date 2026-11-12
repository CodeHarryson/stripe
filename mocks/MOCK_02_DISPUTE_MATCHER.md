# Mock 2 — Dispute matcher

## Candidate packet

Match disputes to charges.

1. Match by `charge_id`.
2. When absent, fall back to exact `(customer_id, amount, currency)`.
3. At minute 20: when multiple charges qualify, choose the closest earlier timestamp, then smallest charge ID.
4. Each charge may match only once. Return unmatched disputes in original order.

Test after every part. Do not ask whether your approach is correct; walk through an example instead.

<details><summary>Evaluator</summary>
Probe missing IDs, equal timestamps, duplicate disputes, reuse of a charge, and deterministic output. Emphasize extensibility, response to the requirement change, and communication.
</details>

