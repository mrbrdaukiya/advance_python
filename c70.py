# Reading Data from file(readline())

f = open('student.txt', mode='r')
data1 = f.readline()
data2 = f.readline()
print(data1)
print(data2)
f.close()
print("Complrte.....!!!")

print("--------------------------------------------")

f = open('student.txt', mode='r')
data = f.readlines()
# print(data)
for i in data:
    print(i)

f.close()
print("Complrte.....!!!")