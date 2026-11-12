# Stripe-relevant stateful design set

These exercises supplement—not replace—the CSV parsing and progressive business-rule work. Use the official LeetCode prompt for the baseline, then apply the original follow-up below. Do not memorize an editorial implementation.

## Day 6 — State and lookup foundations

### LeetCode 2043: Simple Bank System — 25 minutes

Focus: validation, atomic state changes, array/index semantics, and readable method boundaries.

Stripe-style follow-up: add idempotency keys to transfers. Repeating the same key must return the original result without applying the transfer again. Explain where deduplication state lives.

Required tests: invalid account, insufficient funds, transfer to self, zero/negative amount policy, and repeated idempotency key.

### LeetCode 981: Time Based Key-Value Store — 25 minutes

Focus: representation, timestamp ordering, binary-search boundaries, and missing values.

Stripe-style follow-up: writes can arrive out of timestamp order. Decide whether to reject them or support them, state the trade-off, and modify the design without breaking existing reads.

## Day 8 — Boundaries and time-window state

### LeetCode 362: Design Hit Counter — 25 minutes

Focus: precise window semantics and state eviction.

Stripe-style follow-up: maintain independent counters per API key and allow endpoint-specific windows. State the exact inclusive/exclusive boundary before coding.

Required tests: timestamp 1, exact boundary, just outside boundary, repeated timestamps, and two keys.

### LeetCode 635: Design Log Storage System — 30 minutes

Focus: timestamp parsing, granularity, range boundaries, and deterministic result order.

Stripe-style follow-up: logs include merchant ID and severity. Filter by optional merchant and minimum severity while preserving the original range behavior.

## Day 9 — Timed progressive design

### LeetCode 1396: Design Underground System — 30 minutes

Focus: pairing events, aggregate state, invalid sequences, and average computation.

Stripe-style follow-ups, reveal one at a time:

1. A rider can have an incomplete journey; it must not affect averages.
2. Duplicate check-in events can arrive. Define and enforce a policy.
3. Return the busiest route by completed-trip count, then lexicographic route order.

Run regression tests after every follow-up.

## Day 10 or optional stretch — Hierarchical records

### LeetCode 588: Design In-Memory File System — 35-minute cap

Focus: hierarchical parsing, tree representation, lookup, and evolving operations. If the prompt is unavailable, use this substitute:

- `mkdir(path)` creates missing directories.
- `write(path, content)` creates or replaces a file.
- `read(path)` returns file content or a missing marker.
- `list(path)` returns child names sorted lexicographically.

Stripe-style follow-up: support `move(source, destination)` atomically and reject moves that create a directory cycle.

## Completion standard

For each problem, record:

1. time to first working baseline;
2. invariant and representation;
3. tests executed before the follow-up;
4. whether the follow-up required a rewrite;
5. one communication sentence you would say to an interviewer.

Mark Mastered only after an independent later re-solve with the follow-up.
