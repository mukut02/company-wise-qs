from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st


DATASET_PATH = Path(__file__).resolve().parent.parent / "leetcode_dataset.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATASET_PATH)
    df.columns = df.columns.str.strip().str.lower()

    for column in ("acceptance %", "frequency %"):
        df[column] = pd.to_numeric(
            df[column].astype(str).str.replace("%", "", regex=False),
            errors="coerce",
        )

    df["difficulty"] = df["difficulty"].astype(str).str.title()
    df["company"] = df["company"].astype(str).str.strip()
    df["title"] = df["title"].astype(str).str.strip()

    return df

