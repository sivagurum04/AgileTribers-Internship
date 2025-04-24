x=0
def demonstrating():
    global x
    x+=1
    print("value of x is ",x)
def local():
    y=0
    print("val of y is ",y)
demonstrating()
print("global x outside the function ", x)
local()
#print("y outside ",y) cause name error.
