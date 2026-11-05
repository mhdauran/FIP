
name = input("enter your name: ")
level = int(input("enter your level: "))
course = input("enter your course: ")

print("\nSTUDENT INFORMATION")
print("name: ", name)
print("level: ", level)
print('course:', course)



score = float(input("\nenter your score: "))
if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 45:
    grade = "D"
elif score >= 40:
    grade = "E"
else:
    grade = "F"

print("\nSTUDENT RESULT")
print("name: ", name)
print("score: ", score)
print("grade: ", grade)