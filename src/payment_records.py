"""Day 1 starter.

Assumptions for the baseline:
- input lines are well formed;
- amounts are non-negative integer cents;
- repeated payment IDs are separate records;
- customers with no successful payments are omitted.
"""


def summarize_payments(raw: str) -> tuple[dict[str, int], list[str]]:
    """Return successful totals and deterministically ranked customer IDs."""

    if not raw:
        return {}, []
    
    #`payment_id,customer_id,amount,status`
    total = {}
    
    for n in raw.splitlines():
        n = n.split(',')
        #expeecting ['payment_id', 'customer_id', 'amount', 'status']
        cust_id = n[1]
        amount, status = int(n[2]), n[3]

        if status == 'SUCCEEDED':
            if cust_id in total:
                total[cust_id] += amount
            else:
                total[cust_id] = amount
            
        
            

    ranked = sorted(total, key=lambda customer_id: (-total[customer_id], customer_id))
    return total, ranked
    
    



    raise NotImplementedError("Implement during Day 1")

