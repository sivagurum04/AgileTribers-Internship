def remove_replace(lst,remove):
    count=lst.count(remove)
    result=[lsts for lsts in lst if lsts!=remove]
    result+=('_')*count
    return result
print(remove_replace([3,2,2,3],3))

