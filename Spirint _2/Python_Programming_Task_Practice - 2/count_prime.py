def is_prime(n):
    for i in range(1,n):
        if i==1 or i==n:
            continue
        elif n%i==0:
            return False
    return True
matrix = [[2, 4, 5], [7, 9, 11], [13, 16, 19]]
prime_count=sum(1 for row in matrix for num in row if is_prime(num))
print("total prime numbers", prime_count)
