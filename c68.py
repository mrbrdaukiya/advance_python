# Writeline Data

# f = open('student.txt', mode='w')
f = open('student.txt', mode='a')

lst = ['Rahul\n', 'Raj\n','Guru\n', 'Priya\n', 'Rani\n', 'Seema\n']

f.writelines(lst)
f.close()
print("Success")