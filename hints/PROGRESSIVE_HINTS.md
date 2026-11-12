# Progressive hints

Open only after a genuine attempt. Use the weakest hint that gets you moving.

## Payment records

1. Separate parsing from aggregation.
2. Accumulate with `totals.get(customer_id, 0)` or `defaultdict(int)`.
3. A descending numeric value and ascending ID can be expressed with a tuple key.

## Transfer volume

1. Normalize accepted transfers before calculating any views.
2. Deduplication and blocking are eligibility rules; downstream aggregations should consume the eligible list.
3. Keep input index with each parsed record to make equal-timestamp behavior explicit.

## Payout batches

1. Grouping and splitting are separate stages.
2. Decide whether a single payout larger than the maximum is rejected or placed alone; clarify it.
3. Preserve the earliest timestamp as batch metadata for final ordering.

