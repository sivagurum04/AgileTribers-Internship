set1={1,2,3,4}
set2={5,6,7,8}
print("union is ",set1|set2)
print("intersection is ", set1&set1)
print("Difference is ", set2-set1)
set1.add(7)
set2.discard(6)
print("Updated set1:", set1)
print("Updated set2:", set2)

print("Is 2 in set1?", 2 in set1)
