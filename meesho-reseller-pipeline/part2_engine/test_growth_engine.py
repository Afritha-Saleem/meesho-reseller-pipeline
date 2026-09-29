import unittest
from pathlib import Path

from growth_engine import mom_growth, is_flagged, validate_feed


BASE_DIR = Path(__file__).resolve().parent
FIXTURES = BASE_DIR / "fixtures"


class TestGrowthEngine(unittest.TestCase):

    def test_april_may_ethnic_wear(self):
        growth = mom_growth(104520.77, 185107.61)
        result = is_flagged(growth)

        self.assertEqual(growth, 77.1)
        self.assertEqual(result, "flagged")

    def test_may_june_beauty(self):
        growth = mom_growth(35542.11, 37559.07)
        result = is_flagged(growth)

        self.assertEqual(growth, 5.67)
        self.assertEqual(result, "not_flagged")

    def test_exact_boundary(self):
        growth = mom_growth(100000, 108000)
        result = is_flagged(growth)

        self.assertEqual(growth, 8.0)
        self.assertEqual(result, "escalate_exact_boundary")

    def test_corrupted_feed(self):
        ok, errors = validate_feed(
            str(FIXTURES / "corrupted_feed.csv")
        )

        self.assertFalse(ok)

        self.assertEqual(
            errors,
            [
                "line 3: negative revenue (-4200.0) for category=Western Wear",
                "line 4: missing category (month=July)",
                "line 6: missing revenue (category=Home & Kitchen)",
            ],
        )

    def test_validated_monthly_feed(self):
        ok, errors = validate_feed(
            str(FIXTURES / "monthly_category_revenue.csv")
        )

        self.assertTrue(ok)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()