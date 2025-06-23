### `raw/`

* Contains the **original, unmodified datasets** downloaded directly from Kaggle or other sources.
* Acts as the source of truth to always go back to the untouched data.
* Keeps workflow reproducible by preserving the initial dataset.

Contents:
- data/Raw/Country_to_Region_Mapping.csv - has country to region mapping data
- data/Raw/Sales Transaction v.4a.csv
---

### `processed/`

* Contains **cleaned and transformed versions** of the datasets.
* Data here is ready for analysis or modeling after steps like:

  * Missing value imputation
  * Feature engineering
  * Encoding categorical variables
  * Normalization/scaling
* Separate from `raw/` to ensure raw data remains unchanged.

Contents:
- data/data_dictionary.md
---

## Data Dictionary for Sales Transaction Dataset

| Variable Name   | Data Type | Description                               | Possible Values / Notes                   |
| --------------- | --------- | ----------------------------------------- | ----------------------------------------- |
| `TransactionNo` | String    | Unique identifier for each transaction    | Alphanumeric transaction ID               |
| `Date`          | String    | Date of the transaction                   | Format: `dd/mm/yyyy`                      |
| `ProductNo`     | String    | Unique identifier for the product         | Alphanumeric product ID                   |
| `ProductName`   | String    | Name or description of the product        | Examples: `Set Of 2 Wooden Market Crates` |
| `Price`         | Float     | Price of a single item in the transaction | In currency units, e.g., `21.47`          |
| `Quantity`      | Integer   | Number of units sold                      | Positive integer                          |
| `CustomerNo`    | Float     | Unique identifier for the customer        | Alphanumeric customer ID                  |
| `Country`       | String    | Country where the transaction was made    | Examples: `United Kingdom`                |

---

## Notes

* `Date` is in `dd/mm/yyyy` format and should be parsed accordingly.
* `CustomerNo` contains `NaN` for some transactions, indicating anonymous or missing customers.
* `Price` is the unit price of a sold item.
* All transactions are sales data related to various products.
* The dataset can be used for trend analysis, forecasting, and customer behavior studies.

---

> *This data dictionary provides a quick reference for understanding the structure and characteristics of the dataset.*
