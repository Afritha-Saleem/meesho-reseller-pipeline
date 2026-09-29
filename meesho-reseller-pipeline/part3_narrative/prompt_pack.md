\# Reliable AI Narrative Prompt Pack



\## 1. Trigger



Start this prompt when a category's `is\_flagged` result is `"flagged"`.



The purpose is to turn verified Part 1 and Part 2 numbers into a stakeholder-ready update without inventing numbers, unsupported causes, or exposing internal reseller names.



\## 2. Input List



The prompt requires these verified placeholder variables:



\- `{category}` — category name

\- `{previous\_revenue}` — revenue for the previous month

\- `{current\_revenue}` — revenue for the current month

\- `{mom\_pct}` — verified month-on-month percentage

\- `{month}` — current month

\- `{prev\_month}` — previous month



Only the supplied placeholder values may be used as numerical facts in the narrative.



\## 3. Prompt



Using only the supplied verified values, write a concise stakeholder update using the following structure:



\### Context



State what is being measured and the comparison period.



Example:

`{category} revenue for {month} compared with {prev\_month}.`



\### Insight



State exactly what happened using `{mom\_pct}` and explicitly label the statement as \*\*FACT\*\*.



Example:

`{category} revenue changed by {mom\_pct}% MoM — FACT.`



\### Implication



Suggest a specific next step for the stakeholder. Any possible explanation or cause must be explicitly labeled \*\*HYPOTHESIS\*\* and must not be presented as proven by the supplied data.



Do not invent or introduce any number, percentage, benchmark, comparison, date, reseller name, or causal explanation that is not contained in the supplied inputs.



If a reseller must be referenced, use its coded alias rather than its raw reseller name.



\## 4. Checklist



Before using the narrative, verify all of the following:



\- \[ ] Every number in the draft matches a supplied verified value exactly.

\- \[ ] The exact MoM percentage is stated and labeled as \*\*FACT\*\*.

\- \[ ] Any proposed cause or explanation is labeled \*\*HYPOTHESIS\*\*, not presented as proven.

\- \[ ] The narrative contains no invented benchmarks, percentages, or comparisons.

\- \[ ] Any reseller is referenced only by coded alias, never by raw reseller name.

\- \[ ] The suggested next step is specific and actionable.

