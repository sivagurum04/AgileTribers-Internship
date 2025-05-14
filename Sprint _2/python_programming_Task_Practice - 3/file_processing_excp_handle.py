def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
#name=input("Enter file name")
print(read_file("D:\AgileTribers-Internship\Spirint 2\python_programming_Task_Practice - 3\data.txt"))