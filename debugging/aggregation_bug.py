def successful_totals(records: list[tuple[str, int, str]]) -> dict[str, int]:
    """Return successful cents per customer. This implementation is intentionally wrong."""
    totals: dict[str, int] = {}
    for customer_id, amount, status in records:
        if status == "SUCCEEDED":
            totals[customer_id] += amount
    return totals

