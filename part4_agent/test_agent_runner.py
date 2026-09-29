import json
import unittest

from mock_agent_runner import run_agent, PART2_DIR, FIXTURES


class TestAgentRunner(unittest.TestCase):

    REQUIRED_KEYS = {
        "run_month",
        "validation_status",
        "validation_errors",
        "flagged_categories",
        "suppressed_categories",
        "escalated_categories",
        "action_taken",
    }

    def setUp(self):
        self.monthly_csv = str(
            PART2_DIR / "fixtures" / "monthly_category_revenue.csv"
        )

        self.corrupted_csv = str(
            FIXTURES / "corrupted_feed.csv"
        )

    def test_may_scenario(self):
        result = run_agent(
            self.monthly_csv,
            "April",
            "May",
        )

        self.assertEqual(set(result.keys()), self.REQUIRED_KEYS)
        self.assertEqual(result["validation_status"], "valid")

        drafted = [
            item["category"]
            for item in result["flagged_categories"]
        ]

        self.assertEqual(
            drafted,
            ["Ethnic Wear", "Western Wear", "Kids Wear"]
        )

        self.assertEqual(
            set(result["suppressed_categories"]),
            {"Beauty & Personal Care", "Home & Kitchen"}
        )

        self.assertEqual(result["escalated_categories"], [])
        self.assertEqual(result["action_taken"],
                         "drafted_and_held_for_approval")

    def test_june_scenario(self):
        result = run_agent(
            self.monthly_csv,
            "May",
            "June",
        )

        self.assertEqual(set(result.keys()), self.REQUIRED_KEYS)
        self.assertEqual(result["validation_status"], "valid")

        drafted = [
            item["category"]
            for item in result["flagged_categories"]
        ]

        self.assertEqual(
            drafted,
            ["Ethnic Wear", "Home & Kitchen", "Kids Wear"]
        )

        self.assertEqual(
            result["suppressed_categories"],
            ["Western Wear"]
        )

        self.assertEqual(result["escalated_categories"], [])

        all_flagged_or_suppressed = (
            drafted + result["suppressed_categories"]
        )

        self.assertNotIn(
            "Beauty & Personal Care",
            all_flagged_or_suppressed
        )

    def test_corrupted_feed_hard_stop(self):
        result = run_agent(
            self.corrupted_csv,
            "June",
            "July",
        )

        self.assertEqual(set(result.keys()), self.REQUIRED_KEYS)
        self.assertEqual(result["validation_status"], "invalid")
        self.assertEqual(result["action_taken"], "hard_stop")

        self.assertEqual(result["flagged_categories"], [])
        self.assertEqual(result["suppressed_categories"], [])
        self.assertEqual(result["escalated_categories"], [])

        self.assertEqual(len(result["validation_errors"]), 3)

    def test_json_serializable(self):
        result = run_agent(
            self.monthly_csv,
            "April",
            "May",
        )

        json.dumps(result)


if __name__ == "__main__":
    unittest.main()