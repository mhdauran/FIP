import csv

student = [
    ["mustapha", "python", 85]
    ["sadik", "networking", 90]
    ["uwaisu", "cyber security", 78]
]

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "course", "score"])
    writer.writerows(students)

print("csv file created successfully! ")
