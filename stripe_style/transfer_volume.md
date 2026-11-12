# Transfer volume — progressive prompt

Input: `transfer_id,sender,recipient,amount,timestamp`.

## Part 1

Return total amount sent per account.

<details><summary>Part 2 — open only after Part 1 works</summary>
Return the top `k` accounts by sent + received volume. Break ties by account ID.
</details>

<details><summary>Part 3 — open only after Part 2 works</summary>
Transfer IDs may repeat. Only the record with the earliest timestamp counts. For equal timestamps, keep the earliest input occurrence.
</details>

<details><summary>Part 4 — open only after Part 3 works</summary>
Accept a blocked-account set. Ignore transfers involving any blocked account while preserving every earlier rule.
</details>

After each part, run all earlier tests and explain complexity.

