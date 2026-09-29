import csv
from pathlib import Path

from growth_engine import mom_growth, is_flagged


BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "fixtures" / "monthly_category_revenue.csv"


data = {}

with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        month = row["month"]
        category = row["category"]
        revenue = float(row["revenue"])

        data[(month, category)] = revenue


categories = [
    "Ethnic Wear",
    "Western Wear",
    "Kids Wear",
    "Home & Kitchen",
    "Beauty & Personal Care",
]


print("May vs April")
print("-" * 50)

for category in categories:
    previous = data[("April", category)]
    current = data[("May", category)]

    growth = mom_growth(previous, current)
    status = is_flagged(growth)

    print(f"{category}: {growth}% - {status}")


print()
print("June vs May")
print("-" * 50)

for category in categories:
    previous = data[("May", category)]
    current = data[("June", category)]

    growth = mom_growth(previous, current)
    status = is_flagged(growth)

    print(f"{category}: {growth}% - {status}")