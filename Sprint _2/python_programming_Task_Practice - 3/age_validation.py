class AgeError(Exception):
    pass

def check_age():
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeError("You must be at least 18 years old.")
    else:
        print("Age accepted!")

try:
    check_age()
except AgeError as e:
    print("Error:", e)