# Day 5 debugging lab

The files in this directory start with bugs. You are not supposed to infer the requirements from vague docstrings: the behavior below and the tests in `tests/test_debugging.py` are the specification.

## How to work each problem

1. Run only that problem's tests.
2. Read the first failure completely.
3. State the expected behavior and your hypothesis before editing.
4. Make the smallest reasonable fix.
5. Rerun that problem's tests.
6. After they pass, run the entire debugging test file to check regressions.

Do not edit the supplied tests merely to make a failure disappear. You may add more tests.

## Problem 1 — Successful totals

`successful_totals(records)` receives `(customer_id, amount_cents, status)` tuples.

- Include only records whose status is exactly `SUCCEEDED`.
- Add repeated successful records for the same customer.
- Omit customers that have no successful records.
- Empty input returns an empty dictionary.

Run:

```bash
python3 -m unittest tests.test_debugging.SuccessfulTotalsTests -v
```

## Problem 2 — Chronological timestamp ordering

`chronological(values)` receives non-negative integer timestamps represented as strings.

- Sort by their numeric values, not lexicographically.
- Return the original string values.
- Preserve duplicates.
- Empty input returns an empty list.

Example: `['10', '2', '1']` becomes `['1', '2', '10']`.

Run:

```bash
python3 -m unittest tests.test_debugging.ChronologicalTests -v
```

## Problem 3 — Applying a refund

`apply_refund(remaining_cents, refund_cents)` returns the new refundable balance.

- A refund must be positive.
- A refund cannot exceed the remaining refundable amount.
- The remaining amount cannot already be negative.
- Invalid input raises `ValueError` without returning a balance.
- Refunding the complete remaining amount returns zero.

Run:

```bash
python3 -m unittest tests.test_debugging.RefundTests -v
```

## Final regression command

```bash
python3 -m unittest tests.test_debugging -v
```

When everything passes, write one sentence per bug in `TRACKER.md`: the failure mechanism, not merely the corrected line.

