dict1 = {'apple': 5, 'banana': 3}
dict2 = {'banana': 2, 'grape': 4}
merged =dict1.copy()
for key,value in dict2.items():
    if key in merged:
        merged[key]+=value
    else:
        merged[key]=value
print("merged is",merged)