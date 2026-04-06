# Company-Wise LeetCode Radar

A Streamlit app for exploring company-tagged LeetCode questions from a local dataset with a custom red / neon-pink UI.

## Features

- Filter by company, difficulty, acceptance range, and problem title
- Browse spotlight cards in `Aesthetic mode`
- Switch to `Minimalistic mode` for a larger table-first layout
- Move through card results with page controls
- Explore questions from a local CSV dataset

## Project Structure

```
company-wise-qs/
|-- app.py
|-- leetcode_dataset.csv
|-- requirements.txt
|-- README.md
`-- src/
    |-- __init__.py
    |-- data.py
    |-- filters.py
    |-- theme.py
    `-- views.py
```

## Requirements

- Python 3.10+
- pip

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

Open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Usage

1. Use the left sidebar to choose your filters.
2. Pick a sort option.
3. Select a view mode:
   - `Aesthetic mode` for cards, stats, and highlights
   - `Minimalistic mode` for a larger table layout
4. Use the page controls in aesthetic mode to browse more problems.

## Main Files

- [`app.py`](./app.py): main app entrypoint and page flow
- [`src/data.py`](./src/data.py): dataset loading and cleanup
- [`src/filters.py`](./src/filters.py): sidebar filters and sorting
- [`src/theme.py`](./src/theme.py): custom theme and styling
- [`src/views.py`](./src/views.py): hero, metrics, cards, and table rendering

## Dataset

The app expects a file named `leetcode_dataset.csv` in the project root.

Main columns used by the app:

- `Title`
- `Difficulty`
- `Acceptance %`
- `Frequency %`
- `company`
- `URL`

## Status

- Topic-wise tags will be added soon

## Credits

The dataset used in this project is inspired by and derived from the following open-source repository:

- https://github.com/snehasishroy/leetcode-companywise-interview-questions

This repository contains company-wise LeetCode interview questions categorized by recency, along with attributes such as difficulty, acceptance rate, and frequency.

Special thanks to Snehasish Roy for compiling and maintaining this valuable resource for interview preparation.
