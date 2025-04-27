matrix = [["madam", "apple", "racecar"],
          ["level", "hello", "civic"],
          ["world", "deified", "rotor"]]

for row in matrix:
    for word in row:
        if word == word[::-1]:
            print(f"'{word}' is a palindrome")
        else:
            print(f"'{word}' is not a palindrome")
