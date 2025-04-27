for i in range(1, 11):
    for j in range(1, 11):
        product = i * j
        if product % 2 == 0:
            print(f"{product:4}", end="")
        else:
            print("    ", end="")
    print()
