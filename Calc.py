class Calc():
    def __init__(self,a,b):
        self.n1=a
        self.n2=b
    def Addition(self):
        return self.n1+self.n2
    def Subtraction(self):
        return self.n1-self.n2
    def Multiplication(self):
        return self.n1*self.n2
    def Division(self):
        return self.n1/self.n2
        
n1=int(input("Enter Number 1: "))
n2=int(input("Enter Number 2: "))
c=Calc(n1,n2)

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
n=int(input("Enter your choice: "))

if n==1:
    print(c.Addition())
elif n==2:
    print(c.Subtraction())
elif n==3:
    print(c.Multiplication())
elif n==4:
    print(c.Division())
else:
    print("Invalid Choice")