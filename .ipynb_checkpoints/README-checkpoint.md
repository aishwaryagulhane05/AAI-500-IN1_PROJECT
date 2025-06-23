# E-commerce Sales Insights & Strategic Recommendations

## Project Structure

```
ecommerce-sales-project/
│
├── 📁 data/
│   ├── raw/                            # Original dataset from Kaggle
│   ├── processed/                      # Cleaned & transformed datasets
│   └── data_dictionary.md              # Notes about variables and schema
│
├── 📁 notebooks/
│   ├── 01_data_cleaning.ipynb          # Data wrangling and missing value handling
│   ├── 02_eda_part1.ipynb              # Visualizations, outlier detection, stats
│   ├── 02_eda_part1.ipynb              # Visualizations, outlier detection, stats
│   ├── 03_modeling.ipynb               # Modeling and evaluation
│
├── 📁 visuals/
    ├── data_cleansing_charts/          # Histogram, boxplot, pie chart, etc.
│   ├── eda_charts/                     # Histogram, boxplot, pie chart, etc.
│   └── model_charts/                   # Forecasts etc.
│
├── 📁 reports/
│   ├── Final-Project-Report-Group3.pdf     # Final technical report
│
├── 📁 presentation/
│   ├── Final-Project-Presentation-Group3.mp4
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
```

## How to Run

- Download the raw dataset from Kaggle and place it under `data/raw/`.
- Run the notebook:
  - `01_data_cleaning.ipynb`
- refer `data/processed/` for processed dataset.
- Run the notebooks sequentially:
  - `02_eda.ipynb`
  - `03_modeling.ipynb`
- View visualizations in the `visuals/` folder.
- Refer to the final report in `reports/` for conclusions and recommendations.
- Note: replace ~ with your home directory path before running files

## Team & Roles

- Yogesh – Data Cleaning & Preparation  
- Meghesh – Exploratory Data Analysis  
- Aishwarya – Modeling & Reporting  

## Timeline & Milestones

- Weeks 2–4: Dataset exploration, team setup, and initial brainstorming  
- Weeks 5–6: Data cleaning, EDA, model development, and collaborative coding  
- Week 7: Final report writing and presentation recording  

## AI Usage

Tools like ChatGPT and Copilot were used for code suggestions and documentation.  
All AI-generated content was reviewed and adapted by the team to ensure understanding and correctness.

## References

- Dataset source: Kaggle - E-commerce Business Transaction (https://www.kaggle.com/datasets/gabrielramos87/an-online-shop-business)
- Python libraries: pandas, numpy, matplotlib, seaborn, scikit-learn