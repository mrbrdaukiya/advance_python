# File and File Handling

# lst = []

# for i in range(3):
#     name = input('Enter Name :')
#     lst.append(name)

# for i in lst:
#     print(i)



print()
print("************************************************")
print()

f = open('student.txt', mode='w')
f.write('Hello Guru!, How are you ')
f.close()