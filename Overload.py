class days:
    def __init__(self,d):
        self.d=d
class perday:
    def __init__(self,pd):
        self.pd=pd
    def __mul__(self,a):
        return self.pd*a.d

m=int(input("Enter Days: "))
ob1=days(m)
n=int(input("Enter Salary Per Day: "))
ob2=perday(n)
print(ob2*ob1)