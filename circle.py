class circle:
    def cir(s):
        s.r = float(input("enter radious :"))
    def pie(s):
        s.pi = 3.14
class area(circle):
    def par(self):
        print(2*self.pi*self.r)
class perimeter(area):
    def para(self):
        print(self.pi*self.r**2)
    
obj = perimeter()
obj.cir()
obj.pie()
obj.par()
obj.para()
