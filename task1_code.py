import pandas as pd
import numpy as np

# Load the original dataset
df = pd.read_csv("customer_purchases_complex.csv")

# ------------------------
# Data Cleaning
# ------------------------

# 1. Fill missing Age with the median
df['Age'].fillna(df['Age'].median(), inplace=True)

# 2. Fill missing Gender with mode
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)

# 3. Fill missing Country with 'Unknown'
df['Country'].replace('', 'Unknown', inplace=True)

# 4. Fill missing Quantity with mode
df['Quantity'].fillna(df['Quantity'].mode()[0], inplace=True)

# 5. Fill missing Price with the median
df['Price'].fillna(df['Price'].median(), inplace=True)

# 6. Encode Gender: M -> 0, F -> 1
df['Gender'] = df['Gender'].map({'M': 0, 'F': 1})

# 7. Convert PurchaseDate to datetime format
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

# ------------------------
# Feature Engineering
# ------------------------

# 8. Create new feature: TotalAmount
df['TotalAmount'] = df['Quantity'] * df['Price']

# 9. One-hot encode 'Category'
df_encoded = pd.get_dummies(df, columns=['Category'], drop_first=True)

# 10. One-hot encode 'Country'
df_encoded = pd.get_dummies(df_encoded, columns=['Country'], drop_first=True)

# ------------------------
# Save final dataset
# ------------------------

df_encoded.to_csv("customer_purchases_engineered.csv", index=False)
