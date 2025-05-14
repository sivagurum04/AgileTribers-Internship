from datetime import datetime

def print_datetime():
    now = datetime.now()
    print(now.strftime("Today is %B, %d, %Y, and the time is %I:%M %p"))
print(print_datetime())