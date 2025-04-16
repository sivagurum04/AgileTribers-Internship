def add_digits(num):
    while num >= 10:
        num = sum(int(d) for d in str(num))
    return num
print(add_digits(38)) 