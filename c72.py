# File Text Mode 
# Read then Write

f = open('student.txt', mode='r+')
print(f.tell())
data = f.read()
print(f.tell())
# f.write('Guru Choudhay')
print(data)
print(f.tell())


print("---------------------------------------------------")

f = open('student.txt', mode='w+')
print(f.tell())
f.write('Guru Choudhay ')
print(f.tell())
f.seek(0)
data = f.read()
print(data)
print(f.tell())




print("---------------------------------------------------")

f = open('student.txt', mode='a+')
print(f.tell())
f.write('Guru Choudhay ')
f.seek(0)
data = f.read()
print(data)
print(f.tell())