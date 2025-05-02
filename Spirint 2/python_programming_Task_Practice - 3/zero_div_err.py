def safe_divide(a,b):
    try:
        c=a/b
        return c
    except Exception as e:
        return e
print(safe_divide(10, 2))  
print(safe_divide(5, 0))   