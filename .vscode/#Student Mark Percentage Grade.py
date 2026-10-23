#Student Mark Percentage Grade
name= input("enter the student name: ")
n=int(input("enter the number of subjects: "))
total=0
for i in range (1,n+1):
    mark=float(input(f"enter the mark for subject {i}: "))
    total+=mark

percentage=total/n

if percentage>=90:
    grade="A+"
    performance="OUTSTANDING"    
elif percentage>=80:
    grade="A"
    performance="EXCELLENT"   
elif percentage>=70:
    grade="B"
    performance="VERY GOOD"
elif percentage>=60:
    grade="C"
    performance="GOOD"
elif percentage>=50:
    grade="D"
    performance="AVERAGE"
else:
    grade="F"
    performance="NEEDS IMPROVEMENT"

print("\n ---------ACADEMIC PERFORMANCE---------")
print("Student Name: ", name)
print("Total Marks: ",total)
print("Percentage: ", round(percentage,2),"%")
print("Grade: ",grade)
print("Performance :",performance)


