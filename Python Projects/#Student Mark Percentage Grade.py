# Student Report Card 

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
n = int(input("Enter number of subjects: "))

total = 0
highest = 0
best_subject = ""

for i in range(1, n + 1):
    subject = input(f"Enter name of Subject {i}: ")
    mark = float(input(f"Enter mark for {subject}: "))
    total += mark

    if mark > highest:
        highest = mark
        best_subject = subject

percentage = total / n

if percentage >= 90:
    grade = "A+"
    performance = "Outstanding"
elif percentage >= 80:
    grade = "A"
    performance = "Excellent"
elif percentage >= 70:
    grade = "B"
    performance = "Very Good"
elif percentage >= 60:
    grade = "C"
    performance = "Good"
elif percentage >= 50:
    grade = "D"
    performance = "Average"
else:
    grade = "F"
    performance = "Needs Improvement"

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("\n--- Academic Performance ---")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Total Marks  :", total)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("Performance  :", performance)
print("Result       :", result)
print("Best Subject :", best_subject, "(", highest, ")")