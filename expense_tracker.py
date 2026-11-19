expenses = []

while True:
    amount = input("\nenter amount(or 'exit' to stop): ")

    if amount.lower() == "exit":
        break

    category = input("enter category: ")
    note = input("enter note: ")
    date = input("enter date (optional): ")

    expense = {
        "amount": float(amount),
        "category": category,
        "note": note,
        "date": date
    }

    expenses.append(expense)

print("\n--- expense summary ---")

total = 0

for expense in expenses:
    total += expense["amount"]
    print(expense)

print("Total expense:", total)