# with statement 

with open('student.txt', mode='r') as f:
    data = f.read()
    print(data)
    print(f.closed)
print(f.closed)