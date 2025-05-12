def find_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
       
        return f"{year} is aleap year"
    else:
      
       return f"{year} is not a leapyear"
year=int(input("Enter a year "))
print(find_leap(year))
