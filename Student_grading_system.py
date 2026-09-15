name = input("Enter student name: ").strip()

print("="*50)
print(f"Welcome {name}")

print("Enter student exam marks: ")
Exam1 = float(input("Exam 1: "))
Exam2 = float(input("Exam 2: "))
Exam3 = float(input("Exam 3: "))
Exam4 = float(input("Exam 4: "))
Exam5 = float(input("Exam 5: "))
print("="*50)

total = Exam1 + Exam2 + Exam3 + Exam4 + Exam5
average = total/5
print(f"Total marks: {total}")
print(f"Average: {average}")

if average >=90:
    print("Student Grade: A+")
    print("WOW, TRULY AMAZING!!!")
elif average >=80 and average <89:
    print("Student Grade: A")
    print("EXCELLENT!!")
elif average >=70 and average <79:
    print("Student Grade: B+")
    print("Amazing work!")
elif average >=60 and average <69:
    print("Student Grade: B")
    print("Great work")
elif average >=50 and average <59:
    print("Student Grade: C")
    print("Well Done")
else:
    print("Student Grade: F")
    print("Terrible. Please see me for intervention")