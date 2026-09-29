\# Part 4 — Agentic Workflow Specification



\## 4.1 — Five Required Agent Components



\### 1. Goal



Keep category managers informed of any category moving beyond the 8% month-on-month revenue threshold, while requiring human approval before any message is considered sent.



\### 2. Tools



The agent uses the following existing project functions:



\- `validate\_feed()` from `part2\_engine/growth\_engine.py`

\- `mom\_growth()` from `part2\_engine/growth\_engine.py`

\- `is\_flagged()` from `part2\_engine/growth\_engine.py`

\- Part 3's deterministic template-fill narrative function



No real email or SMTP integration is used.



\### 3. Memory / State



The agent retains the previous month's revenue for each category. This state is required to calculate month-on-month growth when the next monthly feed is processed.



\### 4. Planner



The agent follows this exact ordered workflow:



1\. Load the monthly revenue feed.

2\. Run `validate\_feed()`.

3\. If the feed is INVALID, perform a hard stop: report validation errors and run nothing further.

4\. If the feed is VALID, compute `mom\_growth()` for every category against the previous month's revenue.

5\. Run `is\_flagged()` on every category.

6\. Sort flagged categories by absolute MoM percentage in descending order.

6b. Draft a message using Part 3's template for at most the top 3 flagged categories by magnitude.

7\. Log remaining flagged categories beyond the top-3 cap as `suppressed, review manually`.

7b. Separately log any `escalate\_exact\_boundary` category in `escalated\_categories`.

8\. Emit one structured JSON object per run.



The order is mandatory. Sorting occurs only after flagging, suppression is decided only after the draft cap is applied, and exact-boundary cases remain separate from both flagged and suppressed categories.



\### 5. Feedback Loop



Every drafted message is held for human approval. The system only drafts and records the message; it never automatically sends an email or other external message.



The human-approval state is represented as a flag in the final JSON output.



\---



\## 4.2 — Ordered Workflow



\### Step 1 — Load the Monthly Revenue Feed



Load the validated monthly revenue CSV containing:



\- `month`

\- `category`

\- `revenue`

\- `n\_orders`



\### Step 2 — Validate the Feed



Run:



`validate\_feed()`



The validation must pass before any MoM calculation or narrative drafting occurs.



\### Step 3 — Invalid Feed Hard Stop



If validation returns `False`:



\- Set `validation\_status` to `"invalid"`.

\- Set `action\_taken` to `"hard\_stop"`.

\- Surface all `validation\_errors`.

\- Do not calculate MoM.

\- Do not create drafts.



\### Step 4 — Calculate MoM Growth



For a valid feed, calculate MoM revenue growth for every category using:



`mom\_growth(previous\_revenue, current\_revenue)`



\### Step 5 — Flag Categories



Run:



`is\_flagged(mom\_pct)`



for every category.



Possible results are:



\- `"flagged"`

\- `"not\_flagged"`

\- `"escalate\_exact\_boundary"`



\### Step 6 — Sort and Draft



Sort only the categories with `"flagged"` status by:



`abs(mom\_pct)`



in descending order.



Draft messages for at most the top 3 flagged categories using Part 3's template-fill function.



\### Step 7 — Suppression and Escalation



Any flagged category beyond the top-3 drafting limit is recorded as:



`"suppressed, review manually"`



An exact-boundary category is recorded separately in:



`escalated\_categories`



It must never be placed in either `flagged` or `suppressed`.



\### Step 8 — Emit Structured Output



The runner emits one structured JSON object for the run.



\---



\## 4.3 — Three Required Guardrails



\### Input Guardrail



`validate\_feed()` must pass before any other processing occurs.



This prevents invalid or incomplete input data from reaching the growth calculation and narrative stages.



\### Action Guardrail



No message is ever automatically sent.



Messages are only drafted and held for human approval. There is no real email or SMTP integration.



\### Output Guardrail



Every number appearing in a drafted message must trace back to a verified Part 1 or Part 2 value.



No supporting figures may be invented.



\---



\## 4.4 — Invalid Data Hard Stop



When invalid data is detected:



`validation\_status = "invalid"`



`action\_taken = "hard\_stop"`



All validation errors are surfaced in full.



The workflow stops immediately.



No MoM calculation is performed.



No narrative drafts are produced.



Invalid data is never silently skipped.



\---



\## 4.5 — Human Approval



Drafted messages require human approval before they are considered sent.



The mock runner only represents this state using a flag in the structured JSON output.



No real message is sent by the system.

