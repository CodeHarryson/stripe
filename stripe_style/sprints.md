# Three 20-minute sprints

## Sprint 1 — Feature flags

Rules contain a flag, allowed countries, minimum app version, and percentage rollout. Determine enabled flags per user. Define a deterministic rollout function; do not use Python's randomized `hash()`.

## Sprint 2 — Webhook deduplication

Events have `event_id`, `object_id`, `type`, and `created_at`. Ignore duplicate event IDs and return the latest state per object. Clarify equal timestamps and invalid transitions.

## Sprint 3 — Coupon rules

Apply at most one coupon per order. Coupons have expiration, minimum spend, fixed or percentage discount, and a code. Choose the largest discount, then lexicographically smallest code.

For each: two minutes clarify/model, thirteen code, five test. Stop at twenty.

