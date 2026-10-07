import pandas as pd

file_path = "data/sales.csv"

df = pd.read_csv(file_path)


#Convert order_date to date format
df["order_date"] = pd.to_datetime(df["order_date"],  format="%d-%m-%Y")

#Remove duplicate records
df = df.drop_duplicates()

#handle missing values
df["quantity"] = df["quantity"].fillna(0)

#Calculate sales amount
df["sales_amount"] = df["quantity"] * df["price"]

print("Transformation completed.")

print(df)
