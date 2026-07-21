# Power BI Build Guide — Job Market Intelligence Dashboard

## Step 1 — Load data
Get Data → Text/CSV → import all 3 files from `raw_data/`:
- job_postings.csv
- skill_mentions_detailed_sample.csv
- salary_data.csv

Transform Data → verify `posted_date` is Date type, `mentioned` is
Whole Number.

## Step 2 — Relationships
- `skill_mentions_detailed_sample[job_id]` → `job_postings[job_id]` (many-to-one)
- `salary_data[job_id]` → `job_postings[job_id]` (many-to-one)

## Step 3 — DAX Measures
```dax
Total Postings = DISTINCTCOUNT(job_postings[job_id])

Skill Mention Count = SUM(skill_mentions_detailed_sample[mentioned])

Skill Mention Rate % =
DIVIDE(
    [Skill Mention Count],
    CALCULATE(DISTINCTCOUNT(skill_mentions_detailed_sample[job_id])),
    0
) * 100

Avg Salary Min = AVERAGE(salary_data[salary_min_pkr])
Avg Salary Max = AVERAGE(salary_data[salary_max_pkr])
```

## Step 4 — Pages

**Page 1: Market Overview**
- Card: Total Postings (29)
- Bar chart: Postings by city
- Donut chart: Postings by category (Data Analyst / BI Analyst / Business Analyst / Data Engineer / Other)
- Table: Recent postings (title, company, city, posted date)

**Page 2: Skill Demand**
- Bar chart: Skill Mention Rate % by skill (sorted descending) — this is
  your headline visual, it should clearly show SQL and Power BI leading
- Add a text box directly on this page: *"Based on full-text analysis of
  4 job postings (sample size disclosed for transparency). Skills
  tracked: SQL, Power BI, Excel, Python, R, DAX, Power Query, Tableau,
  ETL/Data Warehousing, PL-300 Certification."*
- This transparency note is not optional — it's what makes a recruiter
  trust the whole project instead of one chart

**Page 3: Methodology (this page is what makes the project stand out)**
- Simple text/card page explaining: data source (Indeed), collection
  date, sample size, and how to expand it
- This page signals analytical maturity — most people hide limitations,
  showing them openly is a stronger signal of competence

## Step 5 — Publish
Same as the retail project: Publish → Power BI Service → Publish to Web
→ copy the link into your README and LinkedIn Featured section.

## Why the Methodology page matters more than it seems
A recruiter reading "sample size: 4 of 29 postings, here's how to
expand it" trusts you MORE than a polished dashboard with no
methodology notes at all — because it shows you understand data
limitations, which is exactly the kind of judgment a real analyst job
requires. Don't skip this page to make the project "look more
finished" — the honesty is the selling point.
