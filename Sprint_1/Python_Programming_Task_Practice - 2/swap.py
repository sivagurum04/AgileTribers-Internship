x=10
y=5
print("by using third variable")
temp=x
x=y
y=temp
print("after swapping x = ",x,"y = ",y)
print("without using third variable")
x,y=y,x
print("after swapping x = ",x,"y = ",y)