import unittest

from debugging.aggregation_bug import successful_totals
from debugging.ordering_bug import chronological
from debugging.refund_bug import apply_refund


class SuccessfulTotalsTests(unittest.TestCase):
    def test_empty_input(self) -> None:
        self.assertEqual({}, successful_totals([]))

    def test_first_successful_record_creates_customer_total(self) -> None:
        records = [("customer_1", 500, "SUCCEEDED")]
        self.assertEqual({"customer_1": 500}, successful_totals(records))

    def test_repeated_successes_accumulate(self) -> None:
        records = [
            ("customer_1", 500, "SUCCEEDED"),
            ("customer_1", 250, "SUCCEEDED"),
            ("customer_2", 900, "SUCCEEDED"),
        ]
        self.assertEqual(
            {"customer_1": 750, "customer_2": 900},
            successful_totals(records),
        )

    def test_failed_records_are_ignored(self) -> None:
        records = [
            ("customer_1", 500, "FAILED"),
            ("customer_1", 200, "SUCCEEDED"),
            ("customer_2", 300, "FAILED"),
        ]
        self.assertEqual({"customer_1": 200}, successful_totals(records))


class ChronologicalTests(unittest.TestCase):
    def test_empty_input(self) -> None:
        self.assertEqual([], chronological([]))

    def test_numeric_order_differs_from_string_order(self) -> None:
        self.assertEqual(["1", "2", "10"], chronological(["10", "2", "1"]))

    def test_preserves_duplicates(self) -> None:
        self.assertEqual(
            ["2", "2", "11", "100"],
            chronological(["100", "2", "11", "2"]),
        )

    def test_returns_strings(self) -> None:
        result = chronological(["20", "3"])
        self.assertTrue(all(isinstance(value, str) for value in result))


class RefundTests(unittest.TestCase):
    def test_partial_refund(self) -> None:
        self.assertEqual(600, apply_refund(1000, 400))

    def test_complete_refund(self) -> None:
        self.assertEqual(0, apply_refund(1000, 1000))

    def test_refund_larger_than_remaining_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            apply_refund(500, 501)

    def test_zero_refund_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            apply_refund(500, 0)

    def test_negative_refund_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            apply_refund(500, -1)

    def test_negative_remaining_amount_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            apply_refund(-1, 1)


if __name__ == "__main__":
    unittest.main()

