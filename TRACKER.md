# Progress tracker

Status options: New · Attempted · Solved with help · Independently solved · Mastered

| Date | Exercise | Status | Time to first working output | Tests added | Regression? | Hint level | Main failure mechanism | Review dates |
|---|---|---|---:|---:|---|---:|---|---|
| 2026-11-17 | Day 6 — Transaction-fee baseline | Attempted | No verified runnable checkpoint | 0 | Yes | 0 | Advanced on schedule through Part 3, but changed the shared implementation before preserving a passing Part 1; syntax, input-shape, rule-lookup, rounding, and refund-state errors accumulated without executable tests | Nov 18, Nov 20, Nov 22 |
| 2026-11-16 | Day 1 — Payment records | Solved with help | Not recorded | 3 | No | 2 | Initially placed test data in the implementation instead of executable test methods; cleanup of unreachable starter code remains | Nov 19, Nov 23, Dec 7 |
| 2026-11-15 | Day 5 — Debugging lab | Solved with help | Not recorded | 0 supplied by learner | No | 2 | Aggregation required initializing unseen keys; timestamp strings required numeric sort keys; refunds needed explicit invalid-state checks | Nov 18, Nov 22, Dec 6 |

## Mock scores

Score each category 1–4.

| Mock | Speed | Understanding | Design | Correctness | Testing | Debugging | Python | Communication | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | | | | | | | | | /32 |
| 2 | | | | | | | | | /32 |
| 3 | | | | | | | | | /32 |

For every miss, schedule reviews approximately 3, 7, and 21 days later.

## Day 6 baseline — November 17

The original timed code is preserved in `baselines/DAY_06_ATTEMPT_1.py`; the
working exercise file was restored before Attempt 2.
Detailed assessment: `baselines/DAY_06_BASELINE.md`.

Immediate prevention rule: **do not reveal or implement the next part until the
current part executes and its smallest regression test passes.** At every reveal,
rerun all earlier tests before adding new logic.

