# pickling and unpickling

import pickle, c75stu


# with open('student.dat', mode='wb') as f:
#     stu1 = c75stu.Student('Rahul', 101, 'Ranchi')
#     stu2 = c75stu.Student('Sonam', 102, 'kanpur')
#     pickle.dump(stu1,f)
#     pickle.dump(stu2,f)
#     print('Pickling Done')

# with open('student.dat', mode='rb') as f:
#     obj1 = pickle.load(f)
#     obj2 = pickle.load(f)
#     print('Unpickling Done')
#     obj1.disp()
#     obj2.disp()


print("----------------------------------------------------")



n = int(input('Enter Number of Student: '))

with open('student.dat', mode='wb') as f:
    for i in range(n):
        name = input('Enter Student Name: ')
        roll = int(input('Enter Roll Number: '))
        addrs = input('Enter Address: ')
        stu1 = c75stu.Student(name, roll, addrs)
        pickle.dump(stu1, f)
print('Pickling Done')





with open('student.dat', mode='rb') as f:
    while True:
        try:
            obj = pickle.load(f)
            obj.disp()
        except EOFError:
            print('Done...........!!')
            break