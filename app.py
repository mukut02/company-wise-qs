import streamlit as st
import pandas as pd

# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="LeetCode Company Questions",
    layout="wide"
)

st.title("💻 LeetCode Company Interview Questions Explorer")

# ---------------------------------
# Load Data
# ---------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("leetcode_dataset.csv")

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    # Convert percentage columns safely
    df["acceptance %"] = pd.to_numeric(
        df["acceptance %"].astype(str).str.replace("%", ""),
        errors="coerce"
    )

    df["frequency %"] = pd.to_numeric(
        df["frequency %"].astype(str).str.replace("%", ""),
        errors="coerce"
    )

    return df


df = load_data()

# ---------------------------------
# Sidebar Filters
# ---------------------------------

st.sidebar.header("Filters")

companies = st.sidebar.multiselect(
    "Select Company",
    sorted(df["company"].unique())
)

difficulty = st.sidebar.multiselect(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

acceptance_range = st.sidebar.slider(
    "Acceptance Rate",
    0.0,
    100.0,
    (0.0, 100.0)
)

# ---------------------------------
# Search
# ---------------------------------

search_query = st.text_input("🔍 Search Problem")

# ---------------------------------
# Filter Function (Cached)
# ---------------------------------

@st.cache_data
def filter_data(df, companies, difficulty, acceptance_range, search_query):

    filtered = df.copy()

    if companies:
        filtered = filtered[filtered["company"].isin(companies)]

    if difficulty:
        filtered = filtered[filtered["difficulty"].isin(difficulty)]

    filtered = filtered[
        (filtered["acceptance %"] >= acceptance_range[0]) &
        (filtered["acceptance %"] <= acceptance_range[1])
    ]

    if search_query:
        filtered = filtered[
            filtered["title"].str.contains(search_query, case=False, na=False)
        ]

    return filtered


filtered_df = filter_data(
    df, companies, difficulty, acceptance_range, search_query
)

# ---------------------------------
# Statistics Cards
# ---------------------------------

col1, col2, col3 = st.columns(3)

col1.metric("Total Questions", len(filtered_df))

col2.metric("Unique Companies", filtered_df["company"].nunique())

col3.metric(
    "Average Acceptance",
    f"{filtered_df['acceptance %'].mean():.2f}%"
)

st.divider()

# ---------------------------------
# Difficulty Distribution Chart
# ---------------------------------

st.subheader("Difficulty Distribution")

difficulty_counts = filtered_df["difficulty"].value_counts()

st.bar_chart(difficulty_counts)

# ---------------------------------
# Sorting
# ---------------------------------

sort_option = st.selectbox(
    "Sort By",
    ["acceptance %", "frequency %", "difficulty"]
)

filtered_df = filtered_df.sort_values(by=sort_option, ascending=False)

# ---------------------------------
# Data Table
# ---------------------------------

st.subheader("Filtered Questions")

display_df = filtered_df[
    [
        "title",
        "difficulty",
        "acceptance %",
        "frequency %",
        "company",
        "url"
    ]
]

st.dataframe(
    display_df,
    column_config={
        "url": st.column_config.LinkColumn(
            "LeetCode Problem",
            display_text="Open"
        )
    },
    use_container_width=True,
    height=500
)

st.caption(f"Showing {len(display_df)} questions")