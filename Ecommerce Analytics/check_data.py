import pandas as pd

file_path = r"C:\Users\anjal\Desktop\Ecommerce Analytics\data\historical_sales.csv"

df = pd.read_csv(file_path)

print("Total rows:", len(df))

print("\nFirst 10 Sales and Profit values:")
print(df[["Row ID", "Sales", "Profit"]].head(10).to_string(index=False))

print("\nData types:")
print(df[["Sales", "Profit"]].dtypes)

print("\nMissing values:")
print(df[["Sales", "Profit"]].isnull().sum())

print("\nOriginal CSV totals:")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))

print("\nOriginal CSV minimum and maximum:")
print("Minimum Sales:", df["Sales"].min())
print("Maximum Sales:", df["Sales"].max())
print("Minimum Profit:", df["Profit"].min())
print("Maximum Profit:", df["Profit"].max())