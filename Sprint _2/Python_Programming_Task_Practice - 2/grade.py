score = int(input("Enter student score: "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"

status = "Pass" if grade in ['A', 'B', 'C'] else "Fail"
print(f"Grade: {grade}")
print(f"Status: {status}")
