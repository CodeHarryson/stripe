# Payment records

You receive newline-separated records:

`payment_id,customer_id,amount,status`

`amount` is an integer number of cents and `status` is `SUCCEEDED` or `FAILED`.

Implement `summarize_payments(raw)` returning:

1. a dictionary of successful total cents per customer;
2. customer IDs ordered by successful total descending, then customer ID ascending.

Clarify before coding: whitespace, empty input, malformed lines, repeated payment IDs, negative amounts, and whether customers with only failed payments appear.

Start with the assumptions in the starter docstring, then add tests for any assumption you change.

