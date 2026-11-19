import csv

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "score"])

    while True:
        name = input("\nstudent name(exit): ")
        if name.lower() =="exit":
            break

        score = float(input("Enter score: "))
        writer.writerow([name,score])

with open("student.csv", "r") as file:
    reader = list(csv.DictReader(file))

    scores = [float(row["score"]) for row in reader]

    average = sum(scores) / len(scores)
    top = max(reader, key=lambda x: float(x["score"]))

    print("\nclass Average:", average)
    print("Top performer:", top["name"])
    print("Highesr Score:", top["score"])