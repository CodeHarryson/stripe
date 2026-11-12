def apply_refund(remaining_cents: int, refund_cents: int) -> int:
    """Return remaining refundable amount. Intentionally under-validated."""
    return remaining_cents - refund_cents

