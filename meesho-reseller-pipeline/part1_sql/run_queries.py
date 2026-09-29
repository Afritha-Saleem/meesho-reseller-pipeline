import sqlite3
import csv
from pathlib import Path

DB_PATH = Path("../data/meesho_reseller.db")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

conn = sqlite3.connect(DB_PATH)


def save_csv(filename, query):
    cursor = conn.execute(query)
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()

    output_path = OUTPUT_DIR / filename

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(rows)

    print(f"Created: {output_path} ({len(rows)} rows)")


# 1. Monthly revenue by category
save_csv(
    "monthly_category_revenue.csv",
    """
    SELECT
        month,
        category,
        ROUND(SUM(quantity * unit_price), 2) AS revenue,
        COUNT(*) AS n_orders
    FROM orders
    GROUP BY month, category
    ORDER BY
        CASE month
            WHEN 'April' THEN 1
            WHEN 'May' THEN 2
            WHEN 'June' THEN 3
        END,
        CASE category
            WHEN 'Ethnic Wear' THEN 1
            WHEN 'Western Wear' THEN 2
            WHEN 'Kids Wear' THEN 3
            WHEN 'Home & Kitchen' THEN 4
            WHEN 'Beauty & Personal Care' THEN 5
        END
    """
)


# 2. Region-wise total revenue and order count
save_csv(
    "region_revenue_orders.csv",
    """
    SELECT
        r.region,
        ROUND(SUM(o.quantity * o.unit_price), 2) AS revenue,
        COUNT(*) AS n_orders
    FROM orders o
    JOIN resellers r
        ON o.reseller_id = r.reseller_id
    GROUP BY r.region
    ORDER BY revenue DESC
    """
)


# 3. Top resellers by total spend
save_csv(
    "top_resellers.csv",
    """
    SELECT
        r.reseller_id,
        r.reseller_name,
        ROUND(SUM(o.quantity * o.unit_price), 2) AS total_spend
    FROM orders o
    JOIN resellers r
        ON o.reseller_id = r.reseller_id
    GROUP BY r.reseller_id, r.reseller_name
    HAVING total_spend > 50000
    ORDER BY total_spend DESC
    LIMIT 5
    """
)


# 4. Resellers who have never placed an order
save_csv(
    "zero_order_resellers.csv",
    """
    SELECT
        r.reseller_id,
        r.reseller_name,
        r.region
    FROM resellers r
    LEFT JOIN orders o
        ON r.reseller_id = o.reseller_id
    WHERE o.order_id IS NULL
    """
)


# 4b. Demonstrate COUNT(*) vs COUNT(order_id)
save_csv(
    "zero_order_count_demo.csv",
    """
    SELECT
        r.reseller_id,
        r.reseller_name,
        COUNT(*) AS row_count,
        COUNT(o.order_id) AS order_id_count
    FROM resellers r
    LEFT JOIN orders o
        ON r.reseller_id = o.reseller_id
    WHERE r.reseller_id = 'RS024'
    GROUP BY r.reseller_id, r.reseller_name
    """
)


# 5. June Delivered AOV
save_csv(
    "june_delivered_aov.csv",
    """
    SELECT
        ROUND(
            SUM(quantity * unit_price) / COUNT(*),
            2
        ) AS aov
    FROM orders
    WHERE month = 'June'
      AND status = 'Delivered'
    """
)


# README explaining COUNT(*) issue
readme = """# Part 1 SQL — COUNT(*) vs COUNT(order_id)

For the reseller with no matching orders (RS024), the LEFT JOIN
still produces one row containing NULL values from the orders table.

Therefore:

- COUNT(*) = 1 because COUNT(*) counts the unmatched LEFT JOIN row.
- COUNT(order_id) = 0 because order_id is NULL in that unmatched row,
  and COUNT(column) does not count NULL values.

Therefore COUNT(*) is the wrong way to detect a zero-match LEFT JOIN.
To detect the reseller with no orders, we use:

WHERE o.order_id IS NULL

or COUNT(o.order_id) = 0.
"""

with open(OUTPUT_DIR / "README.md", "w", encoding="utf-8") as f:
    f.write(readme)

conn.close()

print("\nAll Part 1 SQL queries completed successfully.")