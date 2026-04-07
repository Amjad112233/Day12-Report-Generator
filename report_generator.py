import pandas as pd

# Load Data
data = pd.read_csv("../Month 1/Day 11/sales_data.csv")

data.columns = data.columns.str.strip()
# Group by category
summary = data.groupby("category")["amount"].sum()

# Convert to DataFrame
summary = summary.reset_index()

# Export to Excel
summary.to_excel("sales_report.xlsx", index=False)

print("Report generated successfully")