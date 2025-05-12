def duplicate_zeros(arr):
    n = len(arr)
    result = []
    i = 0
    while len(result) < n:
        if arr[i] == 0:
            result.append(0)
            if len(result) < n:
                result.append(0)
        else:
            result.append(arr[i])
        i += 1
    return result
print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))