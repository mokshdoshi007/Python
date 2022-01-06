import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
a=int(input("Enter Radius  of Circle: "))
obj=circle(a)
print("Area of Circle:",obj.area())
print("Perimeter of Circle:",obj.perimeter())