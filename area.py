class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input("Enter Length  of Rectangle: "))
b=int(input("Enter Breadth of Rectangle: "))
obj=rectangle(a,b)
print("Area of Rectangle:",obj.area())