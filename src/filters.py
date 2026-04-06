from __future__ import annotations

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


def render_filters(df: pd.DataFrame) -> dict:
    st.sidebar.markdown(
        """
        <div class="sidebar-panel">
            <div class="sidebar-kicker">Control Deck</div>
            <div class="sidebar-title">Refine Your Hunt</div>
            <div class="sidebar-copy">
                Tune the dataset with sharper filters and cleaner sorting.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    companies = st.sidebar.multiselect(
        "Companies",
        options=sorted(df["company"].dropna().unique()),
        placeholder="Choose one or more companies",
    )

    difficulty = st.sidebar.multiselect(
        "Difficulty",
        options=DIFFICULTY_ORDER,
        placeholder="Any difficulty",
    )

    acceptance_range = st.sidebar.slider(
        "Acceptance rate",
        min_value=0.0,
        max_value=100.0,
        value=(0.0, 100.0),
    )

    search_query = st.sidebar.text_input(
        "Search problem title",
        placeholder="Binary tree, graph, DP...",
    )

    sort_label = st.sidebar.selectbox("Sort by", options=list(SORT_OPTIONS.keys()))
    view_mode = st.sidebar.selectbox("View mode", options=VIEW_MODES, index=0)
    cards_per_page = st.sidebar.slider(
        "Cards per page",
        min_value=6,
        max_value=48,
        value=18,
        step=6,
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
        filtered = filtered[filtered["company"].isin(companies)]

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
