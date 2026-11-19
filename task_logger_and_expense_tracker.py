import csv
import pandas as pd
from datetime import datetime

file = "expenses.csv"

with open(file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Item", "Amount", "Time"])

    while True:
        item = input("Enter expense (or exit): ")
        if item.lower() == "exit":
            break

        amount = float(input("Enter amount: "))
        writer.writerow([item, amount, datetime.now()])

df = pd.read_csv(file)

df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

print("Total spent:", df["Amount"].sum())
print("Average expense:", df["Amount"].mean())