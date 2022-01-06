class gp():
    def f1(self):
        print("GrandParent Class")
class p1(gp):
    def f2(self):
        print("Parent1 Class")
class p2(gp):
    def f3(self):
        print("Parent2 Class")
class c1(p1):
    def f4(self):
        print("Child1 Class")
class c2(p1):
    def f5(self):
        print("Child2 Class")
class c3(p2):
    def f6(self):
        print("Child3 Class")
class c4(p2):
    def f7(self):
        print("Child4 Class")                        

ob1=c1()
ob2=c2()
ob3=c3()
ob4=c4()

ob1.f4()
ob1.f2()
ob1.f1()

ob2.f5()
ob2.f2()
ob2.f1()

ob3.f6()
ob3.f3()
ob3.f1()

ob4.f7()
ob4.f3()
ob4.f1()