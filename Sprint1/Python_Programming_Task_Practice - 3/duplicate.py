def duplicate(nums):
    return len(nums)==len(set(nums))
print(duplicate([1,2,3,1]))