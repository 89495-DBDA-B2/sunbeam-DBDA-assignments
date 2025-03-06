# 2.
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of the rectangle. 
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepiped child class inheriting from the Rectangle class and with a  attribute and another Volume() method to calculate the volume of the Parallelepiped.


class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def Perimeter(self):
        return 2*self.length+self.width

    def Area(self):
        return self.length*self.width

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.Perimeter()}")
        print(f"Area: {self.Area()}")


class Parallelepiped(Rectangle):
    def __init__(self,length,width,height):
        Rectangle.__init__(self,length,width)
        self.height=height
        
    def volume(self):
        print(f"Volume: {self.Area()*self.height}")


r=Rectangle(10,20)
r.Perimeter()
r.display()
p=Parallelepiped(10,20,30)
p.volume()