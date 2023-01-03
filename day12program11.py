class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculateArea(self):
        temp=self.length*self.width
        return temp
    def calculatePerimeter(self):
        temp=2*(self.length+self.width)
        return temp


l=int(input())
w=int(input())
ob=Rectangle(1,w)
area=ob.calculateArea()
peri=ob.calculatePerimeter()
print('Area of Rectangle is',area)
print('Perimeter of Rectangle is',peri)
