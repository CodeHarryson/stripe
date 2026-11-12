# Payout batches

Each payout has `payout_id`, `merchant_id`, `currency`, `amount_cents`, and `created_at`.

Group eligible payouts into merchant/currency batches. Exclude non-positive amounts. A batch may not exceed `max_batch_cents`; when the next payout would exceed the limit, start another batch. Process payouts by creation time, then input order. Return batches ordered by earliest included record, then merchant ID.

Extension: each `(merchant, currency)` may have a reserve amount that cannot be paid out. Clarify whether the reserve applies once or per batch.

Design goal: isolate parsing, eligibility, batching, and output formatting so the extension does not require a rewrite.

