# File Object Method

# f = open('student.txt', mode='r', encoding='utf-8')
# f = open('student.txt', mode='w', encoding='utf-8')
# f = open('student.txt', mode='a', encoding='utf-8')
f = open('student1.txt', mode='x', encoding='utf-8')
# f = open('student.txt', mode='r+', encoding='utf-8')
# f = open('student.txt', mode='w+', encoding='utf-8')
# f = open('python.png', mode='rb')
# f = open('python.png', mode='wb')
# f = open('python1.png', mode='xb')
# f = open('python.png', mode='rb+')
# f = open('python.png', mode='wb+')
# f = open('python.png', mode='ab+')

print('File Name :', f.name)
print('File Mode :', f.mode)
print('File Readable :', f.readable())
print('File Writable :', f.writable())
print('File Closed :', f.closed)


f.close()

print()
print('File Closed :', f.closed)