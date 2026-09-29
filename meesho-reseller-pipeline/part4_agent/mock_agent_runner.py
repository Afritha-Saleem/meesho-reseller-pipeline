import csv
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PART2_DIR = PROJECT_ROOT / "part2_engine"
PART1_OUTPUT = PROJECT_ROOT / "part1_sql" / "output"
FIXTURES = PART2_DIR / "fixtures"

sys.path.insert(0, str(PART2_DIR))
sys.path.insert(0, str(PROJECT_ROOT / "part3_narrative"))

from growth_engine import validate_feed, mom_growth, is_flagged
from narrative_engine import build_category_narrative


def load_month_data(csv_path: str, month: str) -> dict[str, float]:
    data = {}

    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["month"] == month:
                data[row["category"]] = float(row["revenue"])

    return data


def run_agent(
    current_csv: str,
    previous_month: str,
    current_month: str,
) -> dict:
    validation_ok, validation_errors = validate_feed(current_csv)

    if not validation_ok:
        return {
            "run_month": current_month,
            "validation_status": "invalid",
            "validation_errors": validation_errors,
            "flagged_categories": [],
            "suppressed_categories": [],
            "escalated_categories": [],
            "action_taken": "hard_stop",
        }

    previous_data = load_month_data(current_csv, previous_month)
    current_data = load_month_data(current_csv, current_month)

    flagged = []
    escalated = []

    for category in current_data:
        previous_revenue = previous_data[category]
        current_revenue = current_data[category]

        mom_pct = mom_growth(previous_revenue, current_revenue)
        status = is_flagged(mom_pct)

        if status == "flagged":
            flagged.append(
                {
                    "category": category,
                    "mom_pct": mom_pct,
                    "previous_revenue": previous_revenue,
                    "current_revenue": current_revenue,
                    "drafted": False,
                    "message": None,
                }
            )

        elif status == "escalate_exact_boundary":
            escalated.append(category)

    flagged.sort(key=lambda item: abs(item["mom_pct"]), reverse=True)

    top_three = flagged[:3]
    suppressed = flagged[3:]

    for item in top_three:
        item["drafted"] = True
        item["message"] = build_category_narrative(
            item["category"],
            item["previous_revenue"],
            item["current_revenue"],
            item["mom_pct"],
            current_month,
            previous_month,
        )

    return {
        "run_month": current_month,
        "validation_status": "valid",
        "validation_errors": [],
        "flagged_categories": top_three,
        "suppressed_categories": [
            item["category"] for item in suppressed
        ],
        "escalated_categories": escalated,
        "action_taken": "drafted_and_held_for_approval",
    }


def print_run(title: str, result: dict) -> None:
    print(f"\n{'=' * 60}")
    print(title)
    print("=" * 60)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    monthly_csv = str(
        PART2_DIR / "fixtures" / "monthly_category_revenue.csv"
    )
    corrupted_csv = str(
        FIXTURES / "corrupted_feed.csv"
    )

    may_result = run_agent(
        monthly_csv,
        "April",
        "May",
    )

    june_result = run_agent(
        monthly_csv,
        "May",
        "June",
    )

    corrupted_result = run_agent(
        corrupted_csv,
        "June",
        "July",
    )

    print_run("MAY SCENARIO", may_result)
    print_run("JUNE SCENARIO", june_result)
    print_run("CORRUPTED FEED SCENARIO", corrupted_result)