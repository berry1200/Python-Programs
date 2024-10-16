# 1.Write a Python class named Rectangle constructed from length and width and a method that will compute the area of a rectangle.

class rectangle:
    def lw(self):
        self.l = int(input("enter length :"))
        self.w = int(input("enter width :"))
    def area(self):
        self.A = self.l*self.w
        print(self.A)
        
obj = rectangle()
obj.lw()
obj.area()
