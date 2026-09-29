\# Meesho Reseller Growth \& Alert Intelligence Pipeline



\## Project Overview



This project builds a reliable analytics and agentic workflow for monitoring monthly reseller revenue by category.



The pipeline:



\- Generates a reproducible Meesho-style reseller and order dataset.

\- Uses SQL to calculate category, region, and reseller-level revenue metrics.

\- Uses Python to calculate month-on-month (MoM) revenue growth.

\- Applies an 8% growth threshold with an exact-boundary escalation rule.

\- Validates incoming feeds before performing calculations.

\- Generates deterministic stakeholder narratives for flagged categories.

\- Masks reseller names using coded aliases.

\- Uses a mock agent workflow to draft and hold messages for human approval.

\- Prevents invalid feeds from progressing through the pipeline.



No external AI API, paid service, email service, or SMTP integration is required.



\---



\## Project Structure



```text

meesho-reseller-pipeline/

│

├── README.md

│

├── data/

│   ├── generate\_dataset.py

│   ├── orders.csv

│   ├── resellers.csv

│   └── meesho\_reseller.db

│

├── part1\_sql/

│   ├── queries.sql

│   └── output/

│       ├── monthly\_category\_revenue.csv

│       ├── region\_revenue\_orders.csv

│       ├── top\_resellers.csv

│       ├── zero\_order\_resellers.csv

│       ├── zero\_order\_count\_demo.csv

│       ├── june\_delivered\_aov.csv

│       └── README.md

│

├── part2\_engine/

│   ├── growth\_engine.py

│   ├── test\_growth\_engine.py

│   └── fixtures/

│       ├── corrupted\_feed.csv

│       └── monthly\_category\_revenue.csv

│

├── part3\_narrative/

│   ├── prompt\_pack.md

│   ├── narrative\_report.md

│   └── masking.py

│

└── part4\_agent/

&#x20;   ├── agent\_spec.md

&#x20;   ├── mock\_agent\_runner.py

&#x20;   └── test\_agent\_runner.py

