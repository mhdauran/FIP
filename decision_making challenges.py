# AGE VALIDATOR

age = int(input("enter your age: "))

if age < 0:
    print("invalid age")
elif age < 18:
      print("you are a minor")
else:
    print("you are an adult")

# LOGIN FLOW

correct_username = "mustapha dauran"
correct_password = "123456789"

username = input("enter username: ")
password = input("enter password: ")

if username == correct_username and password == correct_password:
    print("login successful!")
else:
    print("incorrect username or password.")


# LOGIN ELIGIBILITY CHEKER

age = int(input("enter your age: "))
income = float(input("enter your monthly income: "))
employed = input("are you employed? (yes/no): ").lower()

if age <18:
    print("not eligible: you must be at least 18.")

elif income < 50000:
    print("not eligible: income is below minimum.")

elif employed != "yes":
    print("not eligible: employment requirement not met.")

else:
    print("congratulations! you meet the basic eligibility criteria.")

# EXPENSE TRACKER

expenses = []

threshold = float(input("enter your spending limit: "))

number = int(input("how many expenses do you? "))

for i in range(number):
    expense = float(input(f"enter expenses {i + 1}: "))
    expenses.append(expense)

total = sum(expenses)

print("\n----- EXPENSE REPORT -----")

print("your expense:", expenses)
print("Total expenses:", total)
print("spending limit:", threshold)

if total > threshold:
    print("WARNING! You have exceed your spending limit.")

elif total == threshold:
    print("you have reached your spending limit.")

else:
    print("good job! you  are within your spending limit.")