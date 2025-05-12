lst = [3, 5, 7]
for num in lst:
    fact=1
    for i in range(1,num):
        fact*=i
    print(f"factorial of {num} is {fact}")