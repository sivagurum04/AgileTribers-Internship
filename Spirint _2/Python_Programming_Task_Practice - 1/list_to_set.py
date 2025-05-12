numbers=[2,5,3,2,5,7,5]
n_set=set(numbers)
print("unique elements ",n_set)
items={2,5,7,3}
common_elements = n_set&items
print("common elements are ", common_elements)
print("union is ", n_set|items)