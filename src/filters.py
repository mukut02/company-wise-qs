from __future__ import annotations

import re
from typing import Iterable

import pandas as pd
import streamlit as st


DIFFICULTY_ORDER = ["Easy", "Medium", "Hard"]
SORT_OPTIONS = {
    "Most frequent": ("frequency %", False),
    "Highest acceptance": ("acceptance %", False),
    "A-Z problem name": ("title", True),
    "Difficulty": ("difficulty", True),
}
VIEW_MODES = ["Aesthetic mode", "Minimalistic mode"]


def _normalize_company_name(value: str) -> str:
    return re.sub(r"\s+", " ", str(value).strip().lower().replace("-", " ")).strip()


def _format_company_label(company: str) -> str:
    tokens = _normalize_company_name(company).split()
    formatted_tokens = []
    acronym_tokens = {"amd", "ibm", "lg", "meta", "npci", "tcs", "uber", "visa", "wix"}

    for token in tokens:
        if token in acronym_tokens or (token.isalpha() and len(token) <= 3):
            formatted_tokens.append(token.upper())
        else:
            formatted_tokens.append(token.capitalize())

    return " ".join(formatted_tokens)


def render_filters(df: pd.DataFrame) -> dict:
    st.markdown(
        """
        <div class="control-panel">
            <div class="control-kicker">Control Deck</div>
            <div class="control-title">Refine Your Hunt</div>
            <div class="control-copy">
                Tune the dataset with sharper filters and cleaner sorting.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    row1_col1, row1_col2, row1_col3 = st.columns([1.5, 1, 1])
    with row1_col1:
        company_options = sorted(df["company"].dropna().unique(), key=_format_company_label)
        companies = st.multiselect(
            "Companies",
            options=company_options,
            placeholder="Choose one or more companies",
            format_func=_format_company_label,
            key="main_companies",
        )
    with row1_col2:
        difficulty = st.multiselect(
            "Difficulty",
            options=DIFFICULTY_ORDER,
            placeholder="Any difficulty",
            key="main_difficulty",
        )
    with row1_col3:
        acceptance_range = st.slider(
            "Acceptance rate",
            min_value=0.0,
            max_value=100.0,
            value=(0.0, 100.0),
            key="main_acceptance_range",
        )

    row2_col1, row2_col2, row2_col3, row2_col4 = st.columns([1.45, 1, 1, 1])
    with row2_col1:
        search_query = st.text_input(
            "Search problem title",
            placeholder="Binary tree, graph, DP...",
            key="main_search_query",
        )
    with row2_col2:
        sort_label = st.selectbox("Sort by", options=list(SORT_OPTIONS.keys()), key="main_sort_label")
    with row2_col3:
        view_mode = st.selectbox("View mode", options=VIEW_MODES, index=0, key="main_view_mode")
    with row2_col4:
        cards_per_page = st.slider(
            "Cards per page",
            min_value=6,
            max_value=48,
            value=18,
            step=6,
            key="main_cards_per_page",
        )

    return {
        "companies": companies,
        "difficulty": difficulty,
        "acceptance_range": acceptance_range,
        "search_query": search_query.strip(),
        "sort_label": sort_label,
        "view_mode": view_mode,
        "cards_per_page": cards_per_page,
    }


@st.cache_data
def filter_data(
    df: pd.DataFrame,
    companies: Iterable[str],
    difficulty: Iterable[str],
    acceptance_range: tuple[float, float],
    search_query: str,
) -> pd.DataFrame:
    filtered = df.copy()

    if companies:
        selected_companies = {_normalize_company_name(company) for company in companies}
        filtered = filtered[
            filtered["company"].map(_normalize_company_name).isin(selected_companies)
        ]

    if difficulty:
        filtered = filtered[filtered["difficulty"].isin(difficulty)]

    filtered = filtered[
        filtered["acceptance %"].between(acceptance_range[0], acceptance_range[1], inclusive="both")
    ]

    if search_query:
        filtered = filtered[
            filtered["title"].str.contains(search_query, case=False, na=False)
        ]

    return filtered


def sort_data(df: pd.DataFrame, sort_label: str) -> pd.DataFrame:
    sort_column, ascending = SORT_OPTIONS[sort_label]

    if sort_column == "difficulty":
        difficulty_rank = {label: index for index, label in enumerate(DIFFICULTY_ORDER)}
        return (
            df.assign(_difficulty_rank=df["difficulty"].map(difficulty_rank).fillna(99))
            .sort_values(by=["_difficulty_rank", "frequency %"], ascending=[True, False])
            .drop(columns="_difficulty_rank")
        )

    return df.sort_values(by=sort_column, ascending=ascending, na_position="last")
