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

    # Add at least three more tests before considering this exercise complete.


if __name__ == "__main__":
    unittest.main()

