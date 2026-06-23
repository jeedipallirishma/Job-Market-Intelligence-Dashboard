import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(
    page_title="Job Market Intelligence Dashboard",
    layout="wide"
)

# Load Data
df = pd.read_csv(r"C:\Users\ramla\Downloads\archive (2)\DataAnalyst.csv")

# Clean Company Name
df["Company Name"] = df["Company Name"].str.split("\n").str[0]

# Title
st.title("📊 Job Market Intelligence Dashboard")

# ==========================
# KPIs
# ==========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Jobs", len(df))
col2.metric("Companies", df["Company Name"].nunique())
col3.metric("Locations", df["Location"].nunique())
col4.metric("Avg Rating", round(df["Rating"].mean(), 2))

st.divider()

# ==========================
# Top Job Titles
# ==========================

st.subheader("Top Job Titles")

job_titles = df["Job Title"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,5))
job_titles.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# ==========================
# Top Industries
# ==========================

st.subheader("Top Hiring Industries")

industries = df["Industry"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,5))
industries.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# ==========================
# Top Companies
# ==========================

st.subheader("Top Hiring Companies")

companies = df["Company Name"].value_counts().head(15)

fig, ax = plt.subplots(figsize=(10,5))
companies.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# ==========================
# Top Locations
# ==========================

st.subheader("Top Hiring Locations")

locations = df["Location"].value_counts().head(15)

fig, ax = plt.subplots(figsize=(10,5))
locations.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# ==========================
# Competitor Analysis
# ==========================

st.subheader("Competitor Analysis")

competitors = df["Competitors"].value_counts().head(15)

fig, ax = plt.subplots(figsize=(10,5))
competitors.plot(kind="bar", ax=ax)
plt.xticks(rotation=90)
plt.tight_layout()

st.pyplot(fig)

# ==========================
# Skill Demand Analysis
# ==========================

skills = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Tableau",
    "Machine Learning"
]

skill_counts = {}

for skill in skills:
    count = df["Job Description"].str.contains(
        skill,
        case=False,
        na=False
    ).sum()

    skill_counts[skill] = count

skill_df = pd.DataFrame(
    list(skill_counts.items()),
    columns=["Skill","Count"]
)

st.subheader("Most Demanded Skills")

fig, ax = plt.subplots(figsize=(8,5))
ax.bar(skill_df["Skill"], skill_df["Count"])
plt.tight_layout()

st.pyplot(fig)

# ==========================
# Ratings Analysis
# ==========================

st.subheader("Company Ratings Distribution")

fig, ax = plt.subplots(figsize=(8,5))
ax.hist(df["Rating"], bins=20)

st.pyplot(fig)

# ==========================
# Raw Data
# ==========================

st.subheader("Dataset Preview")

st.dataframe(df.head(20))
