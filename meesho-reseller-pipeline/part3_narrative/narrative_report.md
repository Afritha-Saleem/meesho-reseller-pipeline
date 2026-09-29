\# Part 3 — Narrative Report



\## 3.2 — Worked Narratives



\### Narrative 1 — May Ethnic Wear: +77.1% MoM Growth



\*\*Context:\*\*

Ethnic Wear revenue is being compared for May against the previous month, April.



\*\*Insight:\*\*

Ethnic Wear revenue increased by 77.1% from April to May — \*\*FACT\*\*.



\*\*Implication:\*\*

Confirm May's promotional calendar and review the category's order activity to understand what contributed to the increase before planning the next action. Any possible promotional effect is a \*\*HYPOTHESIS\*\*, not proven by the supplied data.



\#### Self-Scoring



\- \*\*Specificity:\*\* Passes because the narrative uses the exact category name, months, and verified 77.1% MoM figure.

\- \*\*Audience fit:\*\* Passes because it is written as a concise business update for a regional manager and avoids technical SQL or statistical terminology.

\- \*\*Completeness:\*\* Passes because it includes Context, Insight, and Implication without omitting any required part.

\- \*\*Actionability:\*\* Passes because it gives concrete next steps: confirm the promotional calendar and review order activity.



\---



\### Narrative 2 — June Ethnic Wear: -58.74% MoM Growth



\*\*Context:\*\*

Ethnic Wear revenue is being compared for June against the previous month, May.



\*\*Insight:\*\*

Ethnic Wear revenue changed by -58.74% from May to June — \*\*FACT\*\*.



\*\*Implication:\*\*

Compare June's Ethnic Wear performance with the promotional calendar and order activity, and confirm whether any planned promotion or operational change coincided with the decline. Any such possible cause is a \*\*HYPOTHESIS\*\*, not proven by the supplied data.



\#### Self-Scoring



\- \*\*Specificity:\*\* Passes because the narrative uses the exact category name, months, and verified -58.74% MoM figure.

\- \*\*Audience fit:\*\* Passes because it is written for a regional manager using clear business language rather than technical implementation details.

\- \*\*Completeness:\*\* Passes because Context, Insight, and Implication are all explicitly included.

\- \*\*Actionability:\*\* Passes because it specifies checking the promotional calendar, order activity, and possible operational changes.



\---



\## 3.3 — Chart-Choice Justification



\### 1. Which month had the highest total revenue?



\*\*Chart type: Bar chart\*\*



A bar chart is appropriate because this is a comparison of one numerical measure, total revenue, across three discrete months. The message can be understood quickly by comparing bar heights, and the y-axis should start at zero to avoid visually exaggerating the differences. No legend is needed because there is only one series.



\### 2. What percentage share does Ethnic Wear represent of April's total revenue?



\*\*Chart type: Pie chart\*\*



A pie chart is appropriate because this question asks about one category's share of a single total, making it a part-to-whole comparison. The chart should clearly show Ethnic Wear's 24.92% share of April's total revenue. The visualization should remain simple and avoid unnecessary 3D effects so the percentage share is clear quickly.



\### 3. How do the four regions compare on total revenue?



\*\*Chart type: Bar chart\*\*



A bar chart is appropriate because the question compares one numerical measure, total revenue, across four discrete regions. The bars allow the regional differences to be compared directly, with the y-axis starting at zero for an honest visual comparison. Because there is only one revenue series, a legend is unnecessary.## 



3.4 — Masking Policy



\### Top-Reseller Narrative



Reseller \*\*ALIAS-19\*\* in the \*\*West\*\* region has verified total spend of \*\*75295.09\*\* — \*\*FACT\*\*.



The raw reseller name is intentionally omitted. The narrative uses only the region and coded alias.



\### Masking Tests



\*\*Positive case:\*\*

`alias\_for("RS019")` returns `ALIAS-19`.



`assert\_no\_raw\_names\_leak(final\_narrative, reseller\_names)` returns `True`.



\*\*Negative case:\*\*

A test narrative containing `Mumbai Reseller 1` returns `False` from `assert\_no\_raw\_names\_leak`.



