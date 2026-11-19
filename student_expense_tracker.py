tasks = []
expenses = []

while True:
    print("\n1. add Task")
    print("2. View Tasks")
    print("3. Completed Task")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Add Expense")
    print("7. Filter Expenses")
    print("8. Exit")

    choice = input("choose an option: ")

    if choice == "1":
        tasks.append({"task": input ("assigment: "), "done": False})
    elif choice == "2":
        for i, task in enumerate(tasks):
            print(i, task["task"], "completed" if task["done"] else "pending")

    elif choice == "3":
        i = int(input("Task number:"))
        tasks[i]["done"] = True

    elif choice == "4":
        i = int(input("Task number: "))
        tasks[i]["task"] = input("New assingment: ")

    elif (choice == "5"):
        i = int(input("task number: "))
        tasks.pop(i)

    elif choice == "6":
        item = input("Expense item: ")
        category = input("Category: ")
        amount = float(input("Amount: "))
        expenses.append({"item": item, "category": category, "amount": amount})

    elif choice == "7":
        category = input("category to filter: ")
        filtered = [e for e in expenses if e["category"].lower() == category.lower()]
        above = [e for e in expenses if e["amount"] > 1000]

        print("filtered expenses:", filtered)
        print("Expenses Above 1000:", above)

    elif choice == "8":
        print("goodbye!")
        break

    else:
        print("invalid choice!")