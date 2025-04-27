marks = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}
sorted=dict(sorted(marks.items(),key=lambda sort:sort[1], reverse=True))
print(sorted)