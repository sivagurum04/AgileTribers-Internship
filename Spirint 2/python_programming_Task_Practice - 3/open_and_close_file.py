try:
    f=open('D:\AgileTribers-Internship\Spirint 2\python_programming_Task_Practice - 3\data.txt','r+')
    content=f.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    f.close()
    print("file succesfully closed")