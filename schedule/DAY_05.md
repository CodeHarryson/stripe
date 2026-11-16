# Day 5 — Debugging and executable tests

Fix the three programs in `debugging/`.

For each: reproduce the failure, state a hypothesis, isolate the cause, fix it, and add a regression test. Then write five tests for a merchant-grouping function in under three minutes.

Each debugging file now contains its own test cases at the bottom. Open and run only the file you are currently fixing:

```bash
python3 debugging/aggregation_bug.py
python3 debugging/ordering_bug.py
python3 debugging/refund_bug.py
```

Do not modify the supplied expected results merely to make a test pass.

