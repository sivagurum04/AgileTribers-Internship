x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
positive=[]
negative=[]
for num in x:
    if num>=0:
        positive.append(num)
    else:
        negative.append(num)
print(positive)
print(negative)