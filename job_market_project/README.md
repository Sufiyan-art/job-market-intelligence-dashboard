# Pakistan Data Analyst Job Market Intelligence Dashboard

A unique portfolio project that turns the data analyst job market itself
into the dataset — analyzing real, live job postings pulled from Indeed
to answer: what do employers actually want from entry-level Data
Analysts in Pakistan right now?

## Why this project is different
Most entry-level portfolios analyze retail/sales/HR sample data. This
project instead analyzes **real, current job postings** — the exact
market the analyst is trying to enter — and turns that into a
market-intelligence dashboard. It demonstrates self-directed research,
initiative, and the ability to apply analytics to a genuinely useful
business (career) question.

## Data Source & Methodology (be transparent about this — recruiters respect honesty)
- **29 real job postings** pulled from Indeed (July 2026) across Karachi,
  Lahore, Islamabad/Rawalpindi — titles, companies, locations, post dates,
  job types (`raw_data/job_postings.csv`)
- **4 job postings analyzed in full detail** (complete job description
  text reviewed) to extract genuine skill requirements — not guessed
  from titles (`raw_data/skill_mentions_detailed_sample.csv`)
- **1 real salary data point** found in postings that disclosed pay
  (`raw_data/salary_data.csv`) — Rs 90,000-100,000/month for a Lahore
  Data Analyst role
- **Sample size note:** the skill-frequency analysis is based on 4
  fully-read postings, not all 29 — this is disclosed honestly in the
  dashboard itself (see "Methodology" page) rather than presented as if
  it covers the full sample. This is intentionally a v1 with room to
  expand.

## How to expand this dataset (recommended next step)
Read the remaining 25 job descriptions (links included in
`job_postings.csv`... well, not included yet, but each job_id maps to a
real Indeed posting) and add their skill mentions to the CSV the same
way. Going from a 4-job sample to a 29-job sample is the single most
valuable upgrade to this project's credibility.

## Key Findings (from the analyzed sample)
- **SQL and Power BI appear in every single fully-analyzed posting** —
  the two most consistently required skills
- **Excel appears in 3 of 4** — still highly relevant despite Power BI's
  dominance
- Postings explicitly titled "Power BI [Analyst/Developer]" expect
  **DAX and Power Query as required, not optional** skills — generic
  "Data Analyst" titles are more Excel/SQL-first
- **PL-300 (Power BI certification)** appeared as a preferred
  qualification in a senior-level posting — a signal that certification
  helps even if not required at entry level
- Real disclosed salary for an entry/mid Data Analyst role in Lahore:
  **Rs 90,000–100,000/month**
- **Karachi and Lahore had the most Data Analyst postings**, Islamabad
  skewed more toward "Power BI Business Analyst" / BI-specialist titles

## Data Cleaning (Python)
The raw postings were mostly clean (structured data pulled directly from
Indeed), but still needed light standardization — real-world data always
does:
- **6 unclear `job_type` values** (blank or "N/A") standardized to
  "Not Specified" instead of being left inconsistent
- **City names simplified** — e.g. "Islamabad Dha Phase-Ii" →
  "Islamabad", "Karachi Gulshan-E-Iqbal" → "Karachi" (original values
  preserved in a `city_raw` column for reference) so city-level charts
  group correctly instead of fragmenting into near-duplicate categories
- **Date type validation** — `posted_date` converted to a proper date
  type for time-based analysis
- **Text fields stripped** of leading/trailing whitespace

See `scripts/clean_data.py` — run with `python3 clean_data.py` from
inside the `scripts/` folder.

## Tech Stack
| Tool | Purpose |
|---|---|
| Indeed job search (via API) | Real job posting data source |
| Python (Pandas) | Cleaning, standardization, structuring postings into analysis-ready tables |
| Power BI | Interactive dashboard — skill demand, city distribution, salary |

## Project Structure
```
├── raw_data/
│   ├── job_postings.csv                    # 29 real postings, as collected
│   ├── skill_mentions_detailed_sample.csv  # skill extraction from 4 full descriptions
│   └── salary_data.csv                     # real disclosed salary
├── clean_data/                             # output of clean_data.py
│   ├── job_postings_clean.csv
│   ├── skill_mentions_clean.csv
│   └── salary_data_clean.csv
├── scripts/
│   └── clean_data.py
├── docs/
│   └── PowerBI_Build_Guide.md
└── README.md
```

## Power BI Dashboard
See `docs/PowerBI_Build_Guide.md` for the full build steps. Pages:
1. **Market Overview** — total postings, city distribution, job category breakdown
2. **Skill Demand** — which skills appear most in analyzed postings (with the honest sample-size caveat displayed on the page itself)
3. **Methodology** — transparency page explaining data source and sample size (this is what makes the project credible, not a weakness to hide)

**[Live dashboard link — add after publishing]**

---
**Author:** Sufiyan Khan
**Contact:** sufiyankhan61900@gmail.com | [LinkedIn](https://www.linkedin.com/in/sufiyan-khandata-analyst)
