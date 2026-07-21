"""
Data Cleaning Pipeline — Job Market Intelligence Project
Cleans job_postings.csv: standardizes city names, fills missing job
types, and validates data types.

Run: python3 clean_data.py
"""

import pandas as pd
import os

RAW = "../raw_data/"
CLEAN = "../clean_data/"
os.makedirs(CLEAN, exist_ok=True)

# ---------- JOB POSTINGS ----------
jobs = pd.read_csv(RAW + "job_postings.csv")

before_types = jobs["job_type"].isna().sum() + (jobs["job_type"] == "N/A").sum()

# Standardize missing/unclear job types
jobs["job_type"] = jobs["job_type"].replace("N/A", "Not Specified")
jobs["job_type"] = jobs["job_type"].fillna("Not Specified")

# Simplify city names (remove neighborhood-level detail for cleaner grouping)
city_map = {
    "Islamabad Dha Phase-Ii": "Islamabad",
    "Karachi Gulshan-E-Iqbal": "Karachi",
}
jobs["city_raw"] = jobs["city"]  # keep original for reference
jobs["city"] = jobs["city"].replace(city_map)

# Ensure posted_date is proper date type
jobs["posted_date"] = pd.to_datetime(jobs["posted_date"], errors="coerce")

# Strip whitespace from text fields
for col in ["job_title", "company", "city", "category"]:
    jobs[col] = jobs[col].astype(str).str.strip()

jobs.to_csv(CLEAN + "job_postings_clean.csv", index=False)

print(f"Standardized {before_types} unclear job_type values -> 'Not Specified'")
print(f"Simplified city names for: {list(city_map.keys())}")
print(f"Rows: {len(jobs)}")
print("\nCity distribution after cleaning:")
print(jobs["city"].value_counts())
print("\nCategory distribution:")
print(jobs["category"].value_counts())

# ---------- SKILL MENTIONS (pass-through, already clean) ----------
skills = pd.read_csv(RAW + "skill_mentions_detailed_sample.csv")
skills.to_csv(CLEAN + "skill_mentions_clean.csv", index=False)

# ---------- SALARY DATA (pass-through, already clean) ----------
salary = pd.read_csv(RAW + "salary_data.csv")
salary.to_csv(CLEAN + "salary_data_clean.csv", index=False)

print("\nCleaning complete. Clean files saved to clean_data/")
