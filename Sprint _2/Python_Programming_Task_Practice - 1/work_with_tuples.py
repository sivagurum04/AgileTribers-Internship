#creating tuple
fruits=("apple","banana","cherry")
print(fruits[0])
fruit=list(fruits)
fruit[1]="orange"
fruits=tuple(fruit)
print(fruit)