def apply_refund(remaining_cents: int, refund_cents: int) -> int:
    """Apply a positive refund that does not exceed the remaining amount.

    Raise ValueError when either amount is invalid.
    """
    if remaining_cents < 0 or refund_cents <= 0 or refund_cents > remaining_cents:
        raise ValueError
    return remaining_cents - refund_cents



if __name__ == "__main__":
    assert apply_refund(1000, 400) == 600
    assert apply_refund(1000, 1000) == 0

    # Each invalid case must raise ValueError.
    invalid_cases = [
        (500, 501),   # Refund exceeds what remains.
        (500, 0),     # A refund must be positive.
        (500, -1),    # A refund cannot be negative.
        (-1, 1),      # Remaining refundable amount cannot be negative.
    ]

    for remaining, refund in invalid_cases:
        try:
            apply_refund(remaining, refund)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"Expected ValueError for remaining={remaining}, refund={refund}"
            )

    print("All refund tests passed!")

