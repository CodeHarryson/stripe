# Mock 1 — Subscription ledger

## Candidate packet

You have 60 minutes: clarify/model for about 5, code for 45, then test and discuss.

Events use `timestamp,customer_id,event,plan`. Initially `event` is START or CANCEL.

1. Return each customer's active plan.
2. Return active-customer counts per plan.
3. Events may arrive out of order. Process chronologically and preserve input order for equal timestamps.
4. Add UPGRADE and DOWNGRADE and reject invalid transitions.

Do not open the evaluator section before time expires.

<details><summary>Evaluator and follow-ups</summary>

Ask: What happens on duplicate START, CANCEL without START, equal timestamps, and unknown events? Which prior tests must remain green? Score all eight rubric categories in TRACKER.md.
</details>

