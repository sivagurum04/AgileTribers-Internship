try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero.")
    else:
        print("Operation successful:", result)
except ValueError:
    print("Error: Invalid input. Please enter integers.")
