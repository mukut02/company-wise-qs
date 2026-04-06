import streamlit as st

from src.data import load_data
from src.filters import filter_data, render_filters, sort_data
from src.theme import APP_CSS
from src.views import render_hero, render_metrics, render_react_cards, render_table


def go_prev_page() -> None:
    st.session_state.card_page = max(1, st.session_state.card_page - 1)


def go_next_page() -> None:
    st.session_state.card_page = min(st.session_state.total_card_pages, st.session_state.card_page + 1)


st.set_page_config(
    page_title="Company-Wise LeetCode Radar",
    page_icon=":sparkles:",
    layout="wide",
)

st.markdown(APP_CSS, unsafe_allow_html=True)

df = load_data()
filters = render_filters(df)

filtered_df = filter_data(
    df,
    filters["companies"],
    filters["difficulty"],
    filters["acceptance_range"],
    filters["search_query"],
)
filtered_df = sort_data(filtered_df, filters["sort_label"])

cards_per_page = filters["cards_per_page"]
total_card_pages = max(1, (len(filtered_df) + cards_per_page - 1) // cards_per_page)
st.session_state.total_card_pages = total_card_pages
is_minimal_mode = filters["view_mode"] == "Minimalistic mode"

if is_minimal_mode:
    st.markdown(
        """
        <style>
            .block-container {
                max-width: 96vw;
                padding-top: 1.2rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

if "card_page" not in st.session_state:
    st.session_state.card_page = 1

st.session_state.card_page = min(max(st.session_state.card_page, 1), total_card_pages)
card_page = st.sidebar.slider(
    "Card page",
    min_value=1,
    max_value=total_card_pages,
    value=st.session_state.card_page,
    key="card_page",
)

sidebar_nav_col1, sidebar_nav_col2 = st.sidebar.columns(2)
with sidebar_nav_col1:
    st.button(
        "< Prev",
        use_container_width=True,
        disabled=card_page <= 1 or is_minimal_mode,
        key="sidebar_prev_page",
        on_click=go_prev_page,
    )
with sidebar_nav_col2:
    st.button(
        "Next >",
        use_container_width=True,
        disabled=card_page >= total_card_pages or is_minimal_mode,
        key="sidebar_next_page",
        on_click=go_next_page,
    )

if not is_minimal_mode:
    render_hero(total_rows=len(df), total_companies=df["company"].nunique())
    render_metrics(filtered_df)

    st.markdown('<div class="section-label">Problem Spotlight</div>', unsafe_allow_html=True)
    start_card = 0 if len(filtered_df) == 0 else (card_page - 1) * cards_per_page + 1
    end_card = min(card_page * cards_per_page, len(filtered_df))
    st.markdown(
        f'<div class="spotlight-meta">Page {card_page} of {total_card_pages} | Showing cards {start_card}-{end_card} of {len(filtered_df):,}</div>',
        unsafe_allow_html=True,
    )

    nav_col1, nav_col2 = st.columns([1, 1.2])
    with nav_col1:
        st.button(
            "< Previous",
            use_container_width=True,
            disabled=card_page <= 1,
            key="main_prev_page",
            on_click=go_prev_page,
        )
    with nav_col2:
        st.button(
            "Next Page >",
            use_container_width=True,
            disabled=card_page >= total_card_pages,
            key="main_next_page",
            on_click=go_next_page,
        )
    render_react_cards(filtered_df, card_page, cards_per_page)
    st.markdown(
        """
        <div class="update-panel">
            <div class="update-kicker">Updates</div>
            <p class="update-copy">Topic-wise tags will be added soon.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown('<div class="section-label">Full Results Table</div>', unsafe_allow_html=True)
    render_table(filtered_df, height=900)
    st.markdown(
        """
        <div class="update-panel">
            <div class="update-kicker">Updates</div>
            <p class="update-copy">Topic-wise tags will be added soon.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
