import unittest

from src.payment_records import summarize_payments


class PaymentRecordTests(unittest.TestCase):
    def test_normal_records(self) -> None:
        raw = "p1,c1,500,SUCCEEDED\np2,c2,300,SUCCEEDED\np3,c1,100,FAILED"
        totals, ranked = summarize_payments(raw)
        self.assertEqual({"c1": 500, "c2": 300}, totals)
        self.assertEqual(["c1", "c2"], ranked)

    def test_empty_input(self) -> None:
        self.assertEqual(({}, []), summarize_payments(""))

    def test_repeated_customer_totals_are_combined(self) -> None:
        raw = "p1,c1,500,SUCCEEDED\np2,c1,300,SUCCEEDED\np3,c2,200,SUCCEEDED"
        totals, ranked = summarize_payments(raw)
        self.assertEqual({"c1": 800, "c2": 200}, totals)
        self.assertEqual(["c1", "c2"], ranked)

    def test_failed_payments_are_excluded(self) -> None:
        raw = "p1,c1,500,FAILED\np2,c2,300,SUCCEEDED\np3,c2,100,FAILED"
        totals, ranked = summarize_payments(raw)
        self.assertEqual({"c2": 300}, totals)
        self.assertEqual(["c2"], ranked)

    def test_tied_totals_are_ranked_by_customer_id(self) -> None:
        raw = "p1,c2,500,SUCCEEDED\np2,c1,200,SUCCEEDED\np3,c1,300,SUCCEEDED"
        totals, ranked = summarize_payments(raw)
        self.assertEqual({"c2": 500, "c1": 500}, totals)
        self.assertEqual(["c1", "c2"], ranked)


if __name__ == "__main__":
    unittest.main()

