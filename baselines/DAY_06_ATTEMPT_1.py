"""Archived Day 6 timed submission from November 17, 2026.

This file intentionally preserves the candidate's code, including syntax and
logic errors. Do not use it as a solution or edit it during the next attempt.
"""

from collections import defaultdict
def calculate_fees(csv_text, rules):
    """Implement incrementally. Do not read a solution before attempting it."""
    #transaction_id,merchant_id,amount_cents,currency,provider,country,status,original_transaction_id
    result = defaultdict(list)
    sum = 0
    for n in csv_text.splitlines():
        n = n.split(',')
        transaction_id = n[0]
        merchant_id = n[1]
        amount_cents = int(n[2])
        provider = n[4]
        country = n[5]
        status = n[6]
        original = n[7]

        if status == 'refunded':
            if original in result['Fees'][0] and (result['Fees'][1] - amount_cents) >= 0:
                result['Fees'][1] -= amount_cents
                result['Fees']

                 
                 
            

        elif provider in rules and country != '*' and country in rules and status in rules:
            #amount_cents * basis_points / 10_000``
            compute = amount_cents * rules[(provider, country, status)][0] / 10_000
            sum += compute
            compute += rules[(provider, country, status)][1]
            result['Fees'].append((transaction_id, compute))
        elif provider in rules and country == '*' and country in rules and status in rules:
                    #amount_cents * basis_points / 10_000``
                compute = amount_cents * rules[(provider, country, status)][0] / 10_000
                sum += compute
                compute += rules[(provider, country, status)][1]
                result['Fees'].append((transaction_id, compute))
        else:
              
              
    result['total_fee_cents'] = sum
    return result

            




    raise NotImplementedError
