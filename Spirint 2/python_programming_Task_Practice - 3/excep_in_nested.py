def inner_function():
    return 10/0
def outer_function():
    try:
        inner_function()
    except ZeroDivisionError:
        print("handled zero by outer function")
outer_function()
