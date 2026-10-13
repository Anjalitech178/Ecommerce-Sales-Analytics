
import pandas as pd

# ==========================================
# E-COMMERCE SALES AND CUSTOMER ANALYTICS
# ==========================================

# Step 1: Load the dataset
df = pd.read_excel("data/sample_-_superstore.xls")

# Step 2: Display the first five records
print("\n========== FIRST FIVE RECORDS ==========")
print(df.head())

# Step 3: Find the number of rows and columns
print("\n========== DATASET SIZE ==========")
print("Rows and Columns:", df.shape)
print("Total Records:", df.shape[0])
print("Total Columns:", df.shape[1])

# Step 4: Display all column names
print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

# Step 5: Display dataset information
print("\n========== DATASET INFORMATION ==========")
df.info()

# Step 6: Display statistical information
print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# Step 7: Check missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Step 8: Check duplicate records
print("\n========== DUPLICATE RECORDS ==========")
print("Duplicate Rows:", df.duplicated().sum())

# ==========================================
# STEP 9: DATA QUALITY CHECKS
# ==========================================

print("\n========== DATA TYPES ==========")
print(df.dtypes)

# Check the date range
print("\n========== ORDER DATE RANGE ==========")

df["Order Date"] = pd.to_datetime(df["Order Date"])

print("Earliest Order Date:", df["Order Date"].min())
print("Latest Order Date:", df["Order Date"].max())

# Check sales values
print("\n========== SALES VALIDATION ==========")

print("Minimum Sales:", df["Sales"].min())
print("Maximum Sales:", df["Sales"].max())
print("Negative Sales Records:", (df["Sales"] < 0).sum())

# Check profit values
print("\n========== PROFIT VALIDATION ==========")

print("Minimum Profit:", df["Profit"].min())
print("Maximum Profit:", df["Profit"].max())
print("Negative Profit Records:", (df["Profit"] < 0).sum())

# Check quantity values
print("\n========== QUANTITY VALIDATION ==========")

print("Minimum Quantity:", df["Quantity"].min())
print("Maximum Quantity:", df["Quantity"].max())
print("Zero or Negative Quantity Records:", (df["Quantity"] <= 0).sum())

# ==========================================
# STEP 10: CHECK FUTURE-DATED ORDERS
# ==========================================

today = pd.Timestamp.today().normalize()

future_orders = df[df["Order Date"] > today]

print("\n========== FUTURE-DATED ORDERS ==========")

print("Today's Date:", today.date())

print("Number of Future-Dated Rows:", len(future_orders))

print("\nFuture-Dated Order Records:")
print(future_orders[["Order ID", "Order Date", "Sales", "Profit"]].head(10))

# ==========================================
# STEP 11: INVESTIGATE FUTURE-DATED ORDERS
# ==========================================

# Count unique orders with future dates
future_order_ids = future_orders["Order ID"].nunique()

print("\n========== FUTURE ORDER INVESTIGATION ==========")

print("Future-Dated Rows:", len(future_orders))

print("Unique Future-Dated Orders:", future_order_ids)

# Count future-dated rows by month
future_orders["Order Month"] = future_orders["Order Date"].dt.to_period("M")

print("\nFuture-Dated Rows by Month:")

print(future_orders["Order Month"].value_counts().sort_index())

# Show the first and last future dates
print("\nEarliest Future Order Date:",
      future_orders["Order Date"].min())

print("Latest Future Order Date:",
      future_orders["Order Date"].max())

# ==========================================
# STEP 12: PREPARE HISTORICAL ANALYSIS DATA
# ==========================================

# Create a separate copy of the original dataset
analysis_df = df.copy()

# Keep records dated on or before today's date
analysis_df = analysis_df[analysis_df["Order Date"] <= today].copy()

print("\n========== HISTORICAL DATASET ==========")

print("Original Rows:", len(df))

print("Historical Rows:", len(analysis_df))

print("Excluded Future-Dated Rows:", len(df) - len(analysis_df))

# Check missing values
print("\nMissing Values:")
print(analysis_df.isnull().sum().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(analysis_df.duplicated().sum())

# Save the historical dataset
analysis_df.to_csv("data/historical_sales.csv", index=False)

print("\nHistorical dataset saved successfully!")

# ==========================================
# STEP 13: CALCULATE BUSINESS KPIs
# ==========================================

total_sales = analysis_df["Sales"].sum()

total_profit = analysis_df["Profit"].sum()

total_orders = analysis_df["Order ID"].nunique()

total_customers = analysis_df["Customer ID"].nunique()

average_order_value = total_sales / total_orders if total_orders > 0 else 0

print("\n========== BUSINESS KPIs ==========")

print(f"Total Sales: {total_sales:,.2f}")

print(f"Total Profit: {total_profit:,.2f}")

print(f"Total Orders: {total_orders:,}")

print(f"Total Customers: {total_customers:,}")

print(f"Average Order Value: {average_order_value:,.2f}")

# ==========================================
# STEP 14: SALES AND PROFIT BY CATEGORY
# ==========================================

category_analysis = analysis_df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique"),
    Total_Quantity=("Quantity", "sum")
)

# Calculate profit margin as a percentage
category_analysis["Profit_Margin_Percent"] = (
    category_analysis["Total_Profit"]
    / category_analysis["Total_Sales"]
) * 100

# Sort categories by sales
category_analysis = category_analysis.sort_values(
    by="Total_Sales",
    ascending=False
)

print("\n========== CATEGORY ANALYSIS ==========")

print(category_analysis.round(2))

# ==========================================
# STEP 15: REGIONAL SALES AND PROFIT ANALYSIS
# ==========================================

region_analysis = analysis_df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique"),
    Total_Quantity=("Quantity", "sum")
)

# Calculate profit margin
region_analysis["Profit_Margin_Percent"] = (
    region_analysis["Total_Profit"]
    / region_analysis["Total_Sales"]
) * 100

# Sort regions by total sales
region_analysis = region_analysis.sort_values(
    by="Total_Sales",
    ascending=False
)

print("\n========== REGIONAL ANALYSIS ==========")

print(region_analysis.round(2))

# ==========================================
# STEP 16: MONTHLY SALES TREND ANALYSIS
# ==========================================

# Create a month column from Order Date
analysis_df["Order_Month"] = (
    analysis_df["Order Date"].dt.to_period("M")
)

# Group data by month
monthly_analysis = analysis_df.groupby("Order_Month").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique")
)

# Sort months chronologically
monthly_analysis = monthly_analysis.sort_index()

print("\n========== MONTHLY SALES ANALYSIS ==========")

print(monthly_analysis.round(2))

 # ==========================================
# STEP 17: MONTHLY SALES TREND CHART
# ==========================================

import matplotlib.pyplot as plt
import os

# Create the output folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Create a new figure
fig, ax = plt.subplots(figsize=(16, 7))

# Plot monthly sales
ax.plot(
    monthly_analysis.index.astype(str),
    monthly_analysis["Total_Sales"],
    marker="o",
    linewidth=2
)

# Add title and labels
ax.set_title("Monthly Sales Trend (2023–2026)", fontsize=16)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Total Sales", fontsize=12)

# Rotate month labels
plt.xticks(rotation=90)

# Add grid
ax.grid(True, linestyle="--", alpha=0.5)

# Adjust layout
fig.tight_layout()

# Save the figure BEFORE displaying it
image_path = os.path.abspath(
    os.path.join("outputs", "monthly_sales_trend.png")
)

fig.savefig(image_path, dpi=300, bbox_inches="tight")

print("Chart saved at:", image_path)
print("Image file exists:", os.path.exists(image_path))
print("Image file size:", os.path.getsize(image_path), "bytes")

# Display the chart
plt.show()

# Close the figure after displaying it
plt.close(fig)

# ==========================================
# STEP 18: EXPORT ANALYSIS RESULTS
# ==========================================

import os

# Create the outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Save category analysis
category_analysis.to_csv(
    "outputs/category_analysis.csv"
)

# Save region analysis
region_analysis.to_csv(
    "outputs/region_analysis.csv"
)

# Save monthly analysis
monthly_analysis.to_csv(
    "outputs/monthly_analysis.csv"
)

print("\n========== FILE EXPORT COMPLETED ==========")

print("Category analysis saved successfully.")
print("Region analysis saved successfully.")
print("Monthly analysis saved successfully.")
print("\nAll analysis files have been exported successfully!")
print("Check the outputs folder for your files.")