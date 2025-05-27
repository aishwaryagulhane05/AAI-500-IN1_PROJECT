# Ecommerce Consumer Behavior Analysis Project

---

## 📖 Project Overview

This project analyzes consumer behavior data from an ecommerce platform to uncover insights, build predictive models, and provide actionable recommendations. The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/salahuddinahmedshuvo/ecommerce-consumer-behavior-analysis-data/data).

ecommerce-behavior-project/
│
├── 📁 data/
│   ├── raw/                            # Original dataset from Kaggle
│   ├── processed/                      # Cleaned & transformed datasets
│   └── data_dictionary.md              # Notes about variables and schema
│
├── 📁 notebooks/
│   ├── 01_data_cleaning.ipynb          # Data wrangling and missing value handling
│   ├── 02_eda.ipynb                    # Visualizations, outlier detection, stats
│   ├── 03_modeling.ipynb               # Modeling and evaluation
│   └── 04_summary.ipynb                # Final charts, summary stats, screenshots
│
├── 📁 src/                              # Source scripts if needed
│   ├── __init__.py
│   ├── data_utils.py                   # Functions for loading and preprocessing
│   ├── eda_utils.py                    # Reusable EDA functions
│   └── model_utils.py                  # Modeling helper functions
│
├── 📁 visuals/
│   ├── eda_charts/                     # Histogram, boxplot, pie chart, etc.
│   └── model_charts/                   # Confusion matrix, ROC curve, etc.
│
├── 📁 reports/
│   ├── Final-Project-Report-Team-YMA.pdf     # Final technical report
│   └── appendix/                              # Screenshots, notebook outputs
│
├── 📁 presentation/
│   ├── Final-Project-Presentation-Team-YMA.mp4
│   └── slides.pptx                      # Slide deck used in video
│
├── 📁 meta/
│   ├── team_contacts.txt               # Team contact details
│   ├── meeting_notes.md                # Weekly sync-up meeting notes
│   ├── role_assignment.md              # Roles: prep, EDA, modeling, report
│   └── ai_usage_notes.md               # Notes on ChatGPT or Copilot usage
│
├── requirements.txt                    # Libraries used
├── README.md                           # Project intro & how to run
└── .gitignore                          # Ignore unnecessary files

## 🚀 How to Run

1. Download the raw dataset from Kaggle and place it under `data/raw/`.

2. Run the notebooks sequentially:
   - `01_data_cleaning.ipynb`
   - `02_eda.ipynb`
   - `03_modeling.ipynb`
   - `04_summary.ipynb`

3. View visualizations in `visuals/`.

4. Refer to the final report in `reports/` for conclusions and recommendations.

---

## 👥 Team & Roles

- **Yogesh** – Data Cleaning & Preparation  
- **Meghesh** – Exploratory Data Analysis  
- **Aishwarya** – Modeling & Reporting  

---

## 📅 Timeline & Milestones

- Weeks 2–4: Dataset exploration, team setup, and initial brainstorming  
- Weeks 5–6: Data cleaning, EDA, model development, and collaborative coding  
- Week 7: Final report writing and presentation recording  

---

## 🧠 AI Usage

Tools like ChatGPT and Copilot were used for code suggestions and documentation.  
All AI-generated content was reviewed and adapted by the team to ensure understanding and correctness.

---

## 📄 References

- Dataset source: Kaggle - Ecommerce Consumer Behavior Analysis  
- Python libraries: pandas, numpy, matplotlib, seaborn, scikit-learn

