# Stripe SWE Intern Technical Screen Prep

This repository turns the November 11–22 plan into executable practice for the November 23, 2026 Stripe Summer 2027 SWE internship team screen.

## Rules

1. Work in Python without AI during timed attempts.
2. Read only the prompt and starter file. Do not open `hints/` or `solutions/` until the attempt ends.
3. Clarify assumptions aloud before coding.
4. Get a simple correct version running early.
5. Execute tests after every added requirement.
6. Record the result in `TRACKER.md`. Reading a solution is not mastery.

## Daily workflow

Open `schedule/DAY_XX.md` for the exact assignment. Run tests from the repository root:

```bash
python3 -m unittest discover -s tests -v
```

Run one file:

```bash
python3 -m unittest tests.test_payment_records -v
```

## Repository map

- `schedule/` — the 12-day sequence and success criteria
- `stripe_style/` — progressive business-logic implementation prompts
- `src/` — starter implementations with TODOs
- `tests/` — visible executable tests; add your own edge cases
- `leetcode/` — selected DSA maintenance plus a Stripe-relevant stateful design set with original progressive follow-ups
- `http_tracing/` — request/response, JSON, pagination, retries, and idempotency drills
- `design/` — function-level design and extensibility questions (not distributed system design)
- `debugging/` — intentionally broken programs
- `mocks/` — three 60-minute interview packets and scoring sheets
- `hints/` — progressive hints; open only after a timed attempt
- `solutions/` — solution-review checklists, intentionally not copy-paste implementations

## Interview routine

**Clarify → model the data → state the simplest working design → implement → run a normal example → test boundaries → debug methodically → extend.**

The reported-question material in this repo is pattern-based. It does not claim that any exact question will appear.

## Current highest-priority drill

Recent candidate feedback strengthens the case for a four-part, progressive
transaction-fee exercise involving CSV parsing, business rules, and debugging
under time pressure. Start with `schedule/DAY_06.md` and keep all work for that
session in `stripe_style/transaction_fee_engine.py`. This is representative
practice, not a guaranteed or leaked interview question.

