from __future__ import annotations

import json

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components


def render_hero(total_rows: int, total_companies: int) -> None:
    st.markdown(
        f"""
        <section class="hero-shell">
            <div class="eyebrow">Interview Prep Command Center</div>
            <h1 class="hero-title">
                Crack smarter with
                <span class="accent">company-wise leetcode radar</span>
            </h1>
            <p class="hero-copy">
                Browse <strong>{total_rows:,}</strong> company-tagged entries across
                <strong> {total_companies}</strong> companies in a cleaner, faster, and more visual layout.
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_metrics(filtered_df: pd.DataFrame) -> None:
    unique_questions = filtered_df.drop_duplicates(subset="title")
    col1, col2, col3 = st.columns(3)

    avg_acceptance = unique_questions["acceptance %"].mean()
    avg_frequency = unique_questions["frequency %"].mean()

    col1.metric("Unique problems", f"{unique_questions['title'].nunique():,}")
    col2.metric("Companies in view", f"{filtered_df['company'].nunique():,}")
    col3.metric("Avg acceptance", f"{0.0 if pd.isna(avg_acceptance) else avg_acceptance:.1f}%")

    col4, col5 = st.columns(2)
    col4.metric("Avg frequency", f"{0.0 if pd.isna(avg_frequency) else avg_frequency:.1f}%")
    col5.metric("Rows matched", f"{len(filtered_df):,}")


def render_react_cards(filtered_df: pd.DataFrame, page: int, page_size: int) -> None:
    start_index = max(0, (page - 1) * page_size)
    end_index = start_index + page_size
    card_df = filtered_df.iloc[start_index:end_index].copy()

    if card_df.empty:
        st.info("No questions match the current filters. Try widening the search.")
        return

    records = (
        card_df[["title", "difficulty", "acceptance %", "frequency %", "company", "url"]]
        .fillna("")
        .to_dict(orient="records")
    )

    payload = json.dumps(records)

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
        <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                font-family: "Segoe UI Variable Display", "Bahnschrift", "Segoe UI", sans-serif;
                background: transparent;
                color: #fff5f7;
            }}

            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 16px;
                padding: 4px 2px 6px;
            }}

            .card {{
                position: relative;
                display: flex;
                flex-direction: column;
                min-height: 340px;
                padding: 18px;
                border-radius: 24px;
                border: 1px solid rgba(255, 112, 153, 0.2);
                background:
                    linear-gradient(180deg, rgba(255, 78, 125, 0.18), rgba(255, 255, 255, 0.03)),
                    rgba(14, 7, 16, 0.96);
                box-shadow:
                    0 0 0 1px rgba(255,255,255,0.02) inset,
                    0 18px 40px rgba(255, 49, 92, 0.15);
                overflow: hidden;
            }}

            .card::after {{
                content: "";
                position: absolute;
                width: 140px;
                height: 140px;
                border-radius: 50%;
                top: -48px;
                right: -28px;
                background: radial-gradient(circle, rgba(255, 79, 216, 0.22), transparent 70%);
                pointer-events: none;
            }}

            .company {{
                display: inline-flex;
                padding: 6px 10px;
                border-radius: 999px;
                background: rgba(255, 79, 216, 0.12);
                color: #ffb7d6;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                font-size: 11px;
                font-weight: 700;
            }}

            .title {{
                margin: 14px 0 12px;
                font-size: 22px;
                line-height: 1.05;
                font-weight: 900;
                text-transform: uppercase;
                letter-spacing: 0.02em;
                font-family: "Arial Black", "Bahnschrift SemiBold", sans-serif;
            }}

            .title span {{
                background: linear-gradient(90deg, #ffffff 0%, #ff92b8 45%, #ff55d0 100%);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
            }}

            .difficulty {{
                display: inline-block;
                margin-bottom: 14px;
                padding: 6px 10px;
                border-radius: 10px;
                font-size: 12px;
                font-weight: 800;
                color: #080108;
                background: linear-gradient(90deg, #ff6a70, #ff6cd9);
            }}

            .stats {{
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 10px;
                margin-top: auto;
                padding-top: 12px;
            }}

            .stat {{
                padding: 12px;
                border-radius: 16px;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255,255,255,0.06);
            }}

            .label {{
                font-size: 11px;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                color: #f6b6c9;
                margin-bottom: 4px;
            }}

            .value {{
                font-size: 18px;
                font-weight: 800;
                color: #fff5f7;
            }}

            .link {{
                display: inline-flex;
                align-items: center;
                justify-content: center;
                margin-top: 16px;
                padding: 12px 14px;
                width: 100%;
                border-radius: 14px;
                color: #fff;
                text-decoration: none;
                font-weight: 800;
                background: linear-gradient(90deg, #ff315c, #ff4fd8);
                box-shadow: 0 10px 30px rgba(255, 49, 92, 0.24);
            }}

            @media (max-width: 640px) {{
                .title {{
                    font-size: 18px;
                }}

                .card {{
                    min-height: 320px;
                }}
            }}
        </style>
    </head>
    <body>
        <div id="root"></div>
        <script>
            const records = {payload};
            const rootElement = document.getElementById("root");

            function fallbackMarkup() {{
                rootElement.innerHTML = `
                    <div class="grid">
                        ${{records.map((record) => `
                            <article class="card">
                                <div class="company">${{record.company}}</div>
                                <h3 class="title"><span>${{record.title}}</span></h3>
                                <div class="difficulty">${{record.difficulty}}</div>
                                <div class="stats">
                                    <div class="stat">
                                        <div class="label">Acceptance</div>
                                        <div class="value">${{Number(record["acceptance %"] || 0).toFixed(1)}}%</div>
                                    </div>
                                    <div class="stat">
                                        <div class="label">Frequency</div>
                                        <div class="value">${{Number(record["frequency %"] || 0).toFixed(1)}}%</div>
                                    </div>
                                </div>
                                <a class="link" href="${{record.url}}" target="_blank" rel="noreferrer">Open Problem</a>
                            </article>
                        `).join("")}}
                    </div>
                `;
            }}

            function App() {{
                const e = React.createElement;
                return e(
                    "div",
                    {{ className: "grid" }},
                    records.map((record, index) =>
                        e("article", {{ className: "card", key: `${{record.title}}-${{index}}` }}, [
                            e("div", {{ className: "company", key: "company" }}, record.company),
                            e("h3", {{ className: "title", key: "title" }}, e("span", null, record.title)),
                            e("div", {{ className: "difficulty", key: "difficulty" }}, record.difficulty),
                            e("div", {{ className: "stats", key: "stats" }}, [
                                e("div", {{ className: "stat", key: "acceptance" }}, [
                                    e("div", {{ className: "label", key: "label-a" }}, "Acceptance"),
                                    e("div", {{ className: "value", key: "value-a" }}, `${{Number(record["acceptance %"] || 0).toFixed(1)}}%`)
                                ]),
                                e("div", {{ className: "stat", key: "frequency" }}, [
                                    e("div", {{ className: "label", key: "label-f" }}, "Frequency"),
                                    e("div", {{ className: "value", key: "value-f" }}, `${{Number(record["frequency %"] || 0).toFixed(1)}}%`)
                                ])
                            ]),
                            e("a", {{
                                className: "link",
                                key: "link",
                                href: record.url,
                                target: "_blank",
                                rel: "noreferrer"
                            }}, "Open Problem")
                        ])
                    )
                );
            }}

            if (window.React && window.ReactDOM) {{
                window.ReactDOM.createRoot(rootElement).render(window.React.createElement(App));
            }} else {{
                fallbackMarkup();
            }}
        </script>
    </body>
    </html>
    """

    components.html(html, height=_component_height(len(records)), scrolling=False)


def render_table(filtered_df: pd.DataFrame, height: int = 640) -> None:
    display_df = filtered_df[
        ["title", "difficulty", "acceptance %", "frequency %", "company", "url"]
    ].rename(
        columns={
            "title": "Problem",
            "difficulty": "Difficulty",
            "acceptance %": "Acceptance %",
            "frequency %": "Frequency %",
            "company": "Company",
            "url": "Link",
        }
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        height=height,
        column_config={
            "Link": st.column_config.LinkColumn("LeetCode Link", display_text="Visit"),
            "Acceptance %": st.column_config.NumberColumn(format="%.1f%%"),
            "Frequency %": st.column_config.NumberColumn(format="%.1f%%"),
        },
    )


def _component_height(card_count: int) -> int:
    rows = max(1, (card_count + 2) // 3)
    return max(520, min(2400, rows * 390))
