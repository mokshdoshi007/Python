class gp():
    def f1(self):
        print("GrandParent Class")
class p(gp):
    def f2(self):
        print("Parent Class")
class c(p):
    def f3(self):
        print("Child Class")
ob=c()
ob.f1()
ob.f2()
ob.f3()