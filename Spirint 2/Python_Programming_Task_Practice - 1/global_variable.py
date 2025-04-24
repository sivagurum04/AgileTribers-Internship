counter = 0

def increment():
    global counter
    counter += 1
    print("Counter:", counter)

increment()
increment()