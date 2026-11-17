# Day 6 transaction-fee baseline — November 17, 2026

## Conditions recorded

- Advanced to each part at the suggested reveal time.
- Attempted Parts 1–3.
- Did not attempt Part 4.
- No hints or solutions used during the attempt.
- Candidate knew syntax errors remained and stopped to preserve a genuine timed
  baseline rather than taking unlimited cleanup time.

## Verified outcome

The original timed implementation is archived unchanged in
`baselines/DAY_06_ATTEMPT_1.py`. The working exercise file was subsequently
restored to the clean starter for Attempt 2.

The submitted file does not compile. Python stops at line 107 with:

```text
IndentationError: expected an indented block
```

Because the file cannot run and all supplied assertions remain commented out,
there is no verified passing checkpoint for Part 1, Part 2, or Part 3. This does
not mean no useful progress occurred; it means correctness cannot currently be
credited in an interview-style evaluation.

## What the attempt demonstrates

- Correctly recognized that the CSV should be processed row by row.
- Extracted the important transaction fields.
- Recognized the need for a composite `(provider, country, status)` rule key.
- Attempted exact/wildcard rule handling.
- Recognized that refunds need original-transaction state and a non-negative cap.
- Followed the progressive reveal schedule instead of spending the whole session
  polishing Part 1.

## Primary failure mechanisms

1. **No protected working baseline.** Part 1 was changed to accommodate later
   parts before its tests were uncommented and executed.
2. **Parsing was not isolated.** The header is treated as a data row, and Part 1's
   seven-column rows are indexed as if they already contain an eighth column.
3. **Rule representation drifted.** Membership is checked against tuple-keyed
   dictionaries as though providers, countries, and statuses were separate keys;
   rule values are specified as dictionaries but accessed by numeric indexes.
4. **Money semantics are incorrect.** `/` produces floats, half-up rounding is
   absent, and the total is updated before the fixed fee is added.
5. **Fallback logic is inverted.** A transaction's actual country will not be
   `"*"`; the wildcard belongs in the fallback lookup key.
6. **Refund state is not modeled yet.** The code checks a result tuple as if it
   were an original-transaction index, subtracts the refund amount rather than
   the original fee, and does not track duplicate refund IDs.
7. **Testing/debugging loop was skipped.** Commented tests provided no fast signal,
   allowing syntax and semantic errors to accumulate.

## Baseline scores

Scores use the 1–4 mock scale. Communication was not observed and is therefore
not scored.

| Dimension | Score | Evidence |
|---|---:|---|
| Speed/progress | 2 | Reached Part 3 on schedule, but produced no runnable checkpoint. |
| Understanding | 2 | Identified major entities and intended rules, but several rule/refund semantics were misread. |
| Design | 1 | Parsing, rule selection, calculation, refund state, and output are coupled in one unstable loop. |
| Correctness | 1 | File does not compile; no part is verifiably correct. |
| Testing | 1 | No assertions were enabled or added. |
| Debugging | 1 | The first parser/compiler failure remained at the end of the attempt. |
| Python fluency | 2 | Useful standard operations appeared, but dictionary membership, value shapes, indentation, and numeric behavior caused errors. |
| Communication | Not observed | A future attempt must be narrated or recorded to score this fairly. |

Provisional total: **10/28 across the seven observable dimensions**. This is a
starting measurement, not a prediction of the interview result.

## Next-attempt requirements

1. Make Part 1 compile and pass its two supplied assertions before revealing
   Part 2.
2. Separate parsing, rule selection, fee calculation, and output assembly into
   small helpers or clearly isolated stages.
3. After every new part, rerun all earlier assertions before continuing.
4. Use integer arithmetic for half-up rounding and explain it with one boundary
   example.
5. Target a verified Part 1 within 12 minutes and a regression-free Part 2 by
   minute 30. Part 4 is secondary until those targets are met.
