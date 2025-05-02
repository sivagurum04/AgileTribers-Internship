roll_no=float(input("Enter a number "))
s_no=input("Enter a serial number ")

try:
    sl_no=int(s_no)
    result=roll_no/sl_no
    print(result)
except ValueError :
    print("value error , Enter valid number")
except ZeroDivisionError as e:
    print(e,"error")
