### `raw/`

* Contains the **original, unmodified datasets** downloaded directly from Kaggle or other sources.
* Acts as the source of truth to always go back to the untouched data.
* Keeps your workflow reproducible by preserving the initial dataset.

---

### `processed/`

* Contains **cleaned and transformed versions** of the datasets.
* Data here is ready for analysis or modeling after steps like:

  * Missing value imputation
  * Feature engineering
  * Encoding categorical variables
  * Normalization/scaling
* Separate from `raw/` to ensure raw data remains unchanged.

---

### `data_dictionary.md`

* A Markdown file containing **descriptions and notes** about the dataset variables.
* Typically includes:

  * Variable names
  * Data types
  * Possible value ranges or categories
  * Definitions or explanations for each feature
  * Any assumptions or preprocessing notes
* Serves as a quick reference guide for anyone working with the data.

---

# sample `data_dictionary.md` based on dataset

## Data Dictionary for Ecommerce Consumer Behavior Dataset

| Variable Name         | Data Type   | Description                                                  | Possible Values / Notes                            |
|-----------------------|-------------|--------------------------------------------------------------|---------------------------------------------------|
| `User_ID`             | String      | Unique identifier for each user                               | Alphanumeric ID                                    |
| `Gender`              | Categorical | Gender of the user                                           | `Male`, `Female`                                  |
| `Age`                 | Integer     | Age of the user                                              | Numeric, e.g., 18–70                              |
| `Annual_Income`       | Float       | User's annual income in USD                                   | Numeric, e.g., 10000.00                           |
| `Spending_Score`      | Integer     | Score assigned based on purchasing behavior                   | Scale 1-100, higher means higher spending         |
| `Product_Category`    | Categorical | Category of product purchased                                 | Examples: `Electronics`, `Clothing`, `Home Decor` |
| `Purchase_Amount`     | Float       | Amount spent on the purchase                                  | Numeric, USD                                     |
| `Purchase_Date`       | DateTime    | Date and time of the purchase                                 | Format: YYYY-MM-DD HH:MM:SS                       |
| `Payment_Method`      | Categorical | Payment mode used for the purchase                            | Examples: `Credit Card`, `PayPal`, `Cash`         |
| `Customer_Loyalty`    | Categorical | Loyalty tier of the customer                                  | Examples: `Silver`, `Gold`, `Platinum`            |
| `Location`            | Categorical | Geographic location of the user                               | City or Region names                              |

---

## Notes
- Missing values in `Gender` and `Payment_Method` columns were imputed with the mode.
- `Spending_Score` is derived from user transaction history and updated monthly.
- `Purchase_Date` is in UTC timezone.
- Numerical variables like `Annual_Income` and `Purchase_Amount` were scaled during preprocessing.

---

> _This document is intended to serve as a quick reference for understanding the dataset variables and their characteristics throughout the project._
