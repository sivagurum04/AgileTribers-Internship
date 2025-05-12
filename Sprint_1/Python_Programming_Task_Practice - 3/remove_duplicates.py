def remove_dup(lst):
    seen=set()
    result=[]
    for items in lst:
        if items not in seen:
            seen.add(items)
            result.append(items)
    return result
print(remove_dup([1,2,2,3,1]))