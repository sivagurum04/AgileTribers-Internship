def input_number():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
    else:
        print("Success! You entered:", num)
input_number()