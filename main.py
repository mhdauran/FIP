import math_tools

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("choose operation: ")

if choice == "1":
    print("Result:", math_tools.add(a,b))
elif choice == "2":
    print("Result:", math_tools.subtract(a,b))
elif choice =="3":
    print("REsult:", math_tools.multiply(a,b))
elif choice == "4":
    if b != 0:
        print("Rsult:", math_tools.divide(a,b))
    else:
        print("cannot divided by zero")
else:
    print("Invalid choice")