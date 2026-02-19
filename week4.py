import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_dataset.csv")

df.columns = df.columns.str.strip()

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

total_revenue = df["Total Amount"].sum()
average_sales = df["Total Amount"].mean()

category_sales = df.groupby("Product Category")["Total Amount"].sum()

print("Total Revenue:", total_revenue)
print("Average Sales:", average_sales)
print("Top Category:", category_sales.idxmax())

plt.figure()
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.show()

df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total Amount"].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()