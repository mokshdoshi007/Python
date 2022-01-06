class p1():
    def f1(self):
        print("Parent1 Class")
class p2():
    def f2(self):
        print("Parent2 Class")
class c(p1,p2):
    def f3(self):
        print("Child Class")
ob=c()
ob.f1()
ob.f2()
ob.f3()