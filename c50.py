from threading import *
from time import sleep

class MyExam:
    def solve_que(self):
        self.q1()
        self.q2()
        self.q3()
        self.q4()
    def q1(self):
        print("Question  1 Solved")
        sleep(3)

    def q2(self):
        print("Question  2 Solved")
        sleep(3)
    
    def q3(self):
        print("Question  3 Solved")
        sleep(3)

    def q4(self):
        print("Question  4 Solved")

mye = MyExam()
t = Thread(target=mye.solve_que)
t.start()