def successful_totals(records: list[tuple[str, int, str]]) -> dict[str, int]:
    """Add successful payment cents per customer; ignore failed records."""
    totals: dict[str, int] = {}
    for customer_id, amount, status in records:
        if status == "SUCCEEDED":
            if customer_id in totals:
                totals[customer_id] += amount
            else:
                totals[customer_id] = amount
    return totals


if __name__ == "__main__":
    # Run this file directly. Fix the function until every assertion passes.
    assert successful_totals([]) == {}

    assert successful_totals([
        ("customer_1", 500, "SUCCEEDED"),
    ]) == {"customer_1": 500}

    assert successful_totals([
        ("customer_1", 500, "SUCCEEDED"),
        ("customer_1", 250, "SUCCEEDED"),
        ("customer_2", 900, "SUCCEEDED"),
    ]) == {"customer_1": 750, "customer_2": 900}

    assert successful_totals([
        ("customer_1", 500, "FAILED"),
        ("customer_1", 200, "SUCCEEDED"),
        ("customer_2", 300, "FAILED"),
    ]) == {"customer_1": 200}

    print("All aggregation tests passed!")

