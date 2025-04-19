import random
length = int(input("How long the password should be? (min 6): "))
if length < 6:
    print("Password must be at least 6 characters long.")
else:
    letters ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols="~`!@#$%^&*()_+[]{}:<>,.?/'|"
    password = random.choice(letters) + random.choice(numbers) + random.choice(symbols)
    all_characters=letters+numbers+symbols
    remaining_ch=length-3
    for i in range(remaining_ch):
        password+=random.choice(all_characters)
print(f"The password is : {password}")