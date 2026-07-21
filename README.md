# Pakistan Data Analyst Job Market Intelligence Dashboard

A unique portfolio project that turns the data analyst job market itself
into the dataset — analyzing real, live job postings pulled from Indeed
to answer: what do employers actually want from entry-level Data
Analysts in Pakistan right now?

## Why this project is different
Most entry-level portfolios analyze retail/sales/HR sample data. This
project instead analyzes real, current job postings — the exact
market the analyst is trying to enter — and turns that into a
market-intelligence dashboard.

## Data Source & Methodology
- **29 real job postings** pulled from Indeed (July 2026) across Karachi,
  Lahore, Islamabad/Rawalpindi
- **4 job postings analyzed in full detail** to extract genuine skill
  requirements
- **1 real salary data point** — Rs 90,000-100,000/month for a Lahore
  Data Analyst role
- **Sample size note:** skill-frequency analysis is based on 4 fully-read
  postings, not all 29 — disclosed honestly on the Methodology page

## Data Cleaning (Python)
- 6 unclear `job_type` values standardized to "Not Specified"
- City names simplified (e.g. "Islamabad Dha Phase-Ii" → "Islamabad")
- Date type validation for `posted_date`
- Text fields stripped of whitespace

See `scripts/clean_data.py`

## Key Findings
- **SQL and Power BI appeared in 100% of the analyzed postings**
- Excel appeared in 3 of 4 postings
- Power BI-titled roles expect DAX and Power Query as required skills
- Real disclosed salary: Rs 90,000–100,000/month (Lahore, entry/mid level)
- Karachi and Lahore had the most Data Analyst postings

## Tech Stack
| Tool | Purpose |
|---|---|
| Indeed job search (via API) | Real job posting data source |
| Python (Pandas) | Cleaning and structuring postings |
| Power BI | Interactive dashboard |

## Power BI Dashboard
3 pages: Market Overview, Skill Demand, Methodology (transparency page)

**[Live dashboard link — add after publishing]**

---
**Author:** Sufiyan Khan
**Contact:** sufiyankhan61900@gmail.com | [LinkedIn](https://www.linkedin.com/in/sufiyan-khandata-analyst)
