# Task-1-Elevate-Labs-
Data Cleaning
Missing Age
Action: Filled missing values in the Age column using the median age.

Missing Gender
Action: Filled missing values in the Gender column using the mode (most frequent gender).

Missing Country
Action: Replaced empty strings in the Country column with 'Unknown'.

Missing Quantity
Action: Filled missing values in the Quantity column using the mode.

Missing Price
Action: Filled missing values in the Price column using the median.

Preprocessing
Gender Encoding
Action: Converted categorical values in Gender to numeric codes:
'M' → 0
'F' → 1

Date Conversion
Action: Converted the PurchaseDate column to datetime format for time-based analysis.

Feature Engineering & Encoding:
TotalAmount column added:
Calculated as: Quantity × Price
One-Hot Encoding:
Applied to:
Category (e.g., Category_APP, Category_FUR)
Country (e.g., Country_UK, Country_Canada, etc.)
drop_first=True used to prevent multicollinearity.
