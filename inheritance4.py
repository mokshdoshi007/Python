class gp():
    def f(self):
        print("GrandParent Class")
class p1(gp):
    def f1(self):
        print("Parent1 Class")
class p2(gp):
    def f2(self):
        print("Parent2 Class")
class c(p1,p2):
    def f3(self):
        print("Child Class")
class gc(c):
    def f4(self):
        print("GrandChild Class")
ob=gc()
ob.f()
ob.f1()
ob.f2()
ob.f3()
ob.f4()