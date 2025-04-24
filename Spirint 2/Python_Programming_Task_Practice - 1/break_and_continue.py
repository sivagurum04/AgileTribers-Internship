total = 0
while True:
    num = int(input("Enter a number (0 to quit): "))
    if num < 0:
        continue
    if num == 0:
        break
    total += num
print("Sum of positive numbers:", total)