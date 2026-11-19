print("SMART STUDENT GRADE CALCULATOR")

test_score = float(input("enter your test score: "))
assingment_score = float(input("enter your assignment score: "))
exam_score = float(input("enter your exam score: "))

total_score = test_score + assingment_score + exam_score

average_score = total_score / 3

print("total score:", total_score)
print("average score:", average_score)

if average_score >= 40:
    print("result: passed")
else:
    print("result: failed")

if average_score >= 80 and exam_score >= 70:
    print("congratulations! you have qualify for an award.")
else:
    print("you do not qualify for an award.")