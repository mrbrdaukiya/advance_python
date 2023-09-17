# text mode and Binary Mode 




f = open('student.txt', mode='w')
f.write('Hello\n')
f.write('Guru\n')
f.write('How are you')
f.close()
print('Writing Success')

f = open('student.txt', mode='r')
data = f.read()
print(data)
f.close()

f = open('student.txt', mode='rb')
data =  f.read()
print(data)
f.close()