# Mock 3 — Refund reconciliation

## Candidate packet

Use exact interview conditions for 60 minutes.

1. Parse charges and refunds; calculate remaining refundable cents per charge.
2. Reject invalid refunds and return a reason for each rejection.
3. Refunds include idempotency keys; a duplicate must not be applied twice.
4. Produce a merchant reconciliation summary sorted by discrepancy magnitude descending, then merchant ID.

Clarify what makes a refund invalid and how unknown charges, negative amounts, duplicate keys, and ties behave.

<details><summary>Evaluator</summary>
Readiness target: 26/32, with no category below 3 in correctness, testing/debugging, or communication. Record the exact failure mechanisms to repair on Day 12.
</details>

