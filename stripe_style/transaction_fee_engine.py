"""Day 6 — progressive transaction-fee engine.

This is an ORIGINAL practice exercise based on the recurring interview format,
not a claim about the exact Stripe question.

Interview rules
---------------
* Total time: 60 minutes. Aim for about 45 minutes of coding.
* Read only Part 1 at first. Reveal Parts 2–4 at the indicated times.
* You may use Python documentation, but not AI or copied solutions.
* Run the tests after every part and keep all earlier tests passing.
* Use integer cents. Do not use binary floating point for money.

Input
-----
Transactions arrive as one CSV string with this header:

transaction_id,merchant_id,amount_cents,currency,provider,country,status

All amounts are non-negative integers. Input order must be preserved in the
per-transaction output.

Part 1 — reveal at minute 0
---------------------------
Implement ``calculate_fees(csv_text, rules)``.

``rules`` maps a transaction status to a fee in basis points. One basis point
is 0.01%, so the fee is ``amount_cents * basis_points / 10_000``. Round to the
nearest cent, with exact half cents rounded up. If a status has no rule, its
fee is zero.

Return a dictionary with:

* ``fees``: a list of ``(transaction_id, fee_cents)`` tuples
* ``total_fee_cents``: the sum of all fees

Part 2 — reveal at minute 18
----------------------------
Rules are now keyed by ``(provider, country, status)``. A rule may use ``"*"``
for country. Prefer an exact-country rule; otherwise use the wildcard-country
rule; otherwise charge zero. Each rule contains ``basis_points`` and
``fixed_cents``. The fixed fee is added after the percentage fee.

Part 3 — reveal at minute 30
----------------------------
Add refunds. A ``refunded`` transaction refers to a prior transaction using a
new ``original_transaction_id`` CSV column. Its fee is the negative of the
original transaction's calculated fee, capped so total fees for that original
can never fall below zero. Duplicate refund transaction IDs must not be applied
twice. Explain what you will do if the original ID is missing or unknown.

Part 4 — reveal at minute 39
----------------------------
Add ``merchant_totals`` to the result: a dictionary from merchant ID to its net
fee cents. Output its keys in sorted order. Your earlier outputs and tests must
continue to work.

Before coding, say aloud
------------------------
1. What assumptions need clarification?
2. What representation will you use for parsed rows and rules?
3. How will you avoid rewriting the function as later parts arrive?
4. What is the smallest useful test for Part 1?
"""

from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
def calculate_fees(csv_text, rules):
    """Implement incrementally. Do not read a solution before attempting it."""
    #transaction_id,merchant_id,amount_cents,currency,provider,country,status
    result = defaultdict(list)
    total = 0

    for line in csv_text.splitlines()[1:]:
        if not line.strip():
            continue
        fields = line.strip().split(",")
        print(fields)
        transaction_id = fields[0]
        tamount = fields[2]
        status = fields[6]

        if status in rules:
            fee_amount = (int(tamount) * rules[status] + 5_000) // 10_000
            
            #fees: [(transactionid, feeamount)]
            total += fee_amount
            result['fees'].append((transaction_id, fee_amount))
        else:
            result['fees'].append((transaction_id, 0))
    result['total_fee_cents'] = total
    print(result)
    return result


            



if __name__ == "__main__":
    # Uncomment only the tests for the part you have revealed.

    # PART 1 TESTS
    csv_part_1 = """transaction_id,merchant_id,amount_cents,currency,provider,country,status
    tx_1,m_1,10000,usd,card,US,succeeded
    tx_2,m_2,5050,usd,card,US,succeeded
    tx_3,m_1,900,usd,card,US,failed
    tx_half,m_1,100,usd,card,US,succeeded

    """
    result = calculate_fees(csv_part_1, {"succeeded": 250})
    assert result["fees"] == [("tx_1", 250), ("tx_2", 126), ("tx_3", 0), ("tx_half", 3)]
    assert result["total_fee_cents"] == 379

    # PART 2 TESTS
    # rules_part_2 = {
    #     ("card", "US", "succeeded"): {"basis_points": 250, "fixed_cents": 30},
    #     ("card", "*", "succeeded"): {"basis_points": 300, "fixed_cents": 20},
    # }
    # result = calculate_fees(csv_part_1, rules_part_2)
    # assert result["fees"] == [("tx_1", 280), ("tx_2", 156), ("tx_3", 0)]
    # assert result["total_fee_cents"] == 436
    # Add one non-US row and prove the wildcard fallback works.

    # PART 3 TESTS
    # Replace the header with the following and add refund rows:
    # transaction_id,merchant_id,amount_cents,currency,provider,country,status,original_transaction_id
    # Required cases: valid refund, duplicate refund ID, unknown original,
    # and refunds whose combined reversal would exceed the original fee.

    # PART 4 TESTS
    # Assert merchant totals for at least two merchants, including one refund,
    # and verify list(result["merchant_totals"]) is sorted.

    print("Uncomment the tests for the part you are currently solving.")
