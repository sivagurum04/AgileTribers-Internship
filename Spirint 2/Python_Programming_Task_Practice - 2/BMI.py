weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

print(f"BMI: {bmi:.2f}")
print(f"Category: {category}")
