# Meesho Reseller Growth & Alert Intelligence Pipeline

## Project Overview

This project builds a reliable analytics and agentic workflow for monitoring monthly reseller revenue by category.

The pipeline:
- Generates a reproducible Meesho-style reseller and order dataset.
- Uses SQL to calculate category, region, and reseller-level revenue metrics.
- Uses Python to calculate month-on-month (MoM) revenue growth.
- Applies an 8% growth threshold with an exact-boundary escalation rule.
- Validates incoming feeds before performing calculations.
- Generates deterministic stakeholder narratives for flagged categories.
- Masks reseller names using coded aliases.
- Uses a mock agent workflow to draft and hold messages for human approval.
- Prevents invalid feeds from progressing through the pipeline.

No external AI API, paid service, email service, or SMTP integration is required.

---

## Project Structure

```text
meesho-reseller-pipeline/
│
├── README.md
│
├── data/
│   ├── generate_dataset.py
│   ├── orders.csv
│   ├── resellers.csv
│   └── meesho_reseller.db
│
├── part1_sql/
│   ├── queries.sql
│   └── output/
│       ├── monthly_category_revenue.csv
│       ├── region_revenue_orders.csv
│       ├── top_resellers.csv
│       ├── zero_order_resellers.csv
│       ├── zero_order_count_demo.csv
│       ├── june_delivered_aov.csv
│       └── README.md
│
├── part2_engine/
│   ├── growth_engine.py
│   ├── test_growth_engine.py
│   └── fixtures/
│       ├── corrupted_feed.csv
│       └── monthly_category_revenue.csv
│
├── part3_narrative/
│   ├── prompt_pack.md
│   ├── narrative_report.md
│   └── masking.py
│
└── part4_agent/
    ├── agent_spec.md
    ├── mock_agent_runner.py
    └── test_agent_runner.py
