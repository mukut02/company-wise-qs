# 🚀 Company-wise LeetCode Questions Explorer

A **data-driven web app** to explore **LeetCode interview questions asked by different companies**, with filtering by **company, difficulty, frequency, and premium status**.

This project helps candidates **prepare efficiently for technical interviews** by identifying the most relevant questions asked in real company interviews.

---

## 📌 Features

- 🔍 **Company-wise filtering** – View questions asked by specific companies  
- 🎯 **Difficulty filtering** – Easy / Medium / Hard  
- 📊 **Frequency-based insights** – Identify commonly asked questions  
- 🔒 **Premium question indicator** – Filter premium and non-premium problems  
- 📋 **Interactive table view** – Clean UI for browsing problems  
- ⚡ **Fast data filtering** using Streamlit  

---

## 🖥️ Demo Interface

The interface allows users to:

- Select companies
- Filter by difficulty
- Filter premium questions
- Browse questions in a clean dashboard

This helps users **target interview preparation for specific companies efficiently.**

---

## 🏗️ Project Structure
company-wise-qs/
│
├── app.py                  # Main Streamlit application
├── leetcode_dataset.csv    # Dataset containing questions
├── requirements.txt        # Python dependencies

---


---

## 📊 Dataset

The dataset contains metadata about LeetCode problems such as:

| Column | Description |
|------|-------------|
| Title | Problem name |
| Difficulty | Easy / Medium / Hard |
| Company | Company where question appeared |
| Frequency | How often asked |
| Premium | Whether problem is premium |
| Link | Link to problem |

This enables **company-wise interview preparation and problem tracking.**

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mukut02/company-wise-qs.git
cd company-wise-qs

---
##  Credits

The dataset used in this project is inspired by and derived from the following open-source repository:

- https://github.com/snehasishroy/leetcode-companywise-interview-questions

This repository contains **company-wise LeetCode interview questions categorized by recency**, along with attributes such as difficulty, acceptance rate, and frequency. :contentReference[oaicite:0]{index=0}

Special thanks to **Snehasish Roy** for compiling and maintaining this valuable resource for interview preparation.
