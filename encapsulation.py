class A :
    def __display(self,a,b,c):
        self.na = a
        self.nb = b
        self.nc = c
        print(self.na)
class B(A):
    def show(self):
        print(self.nb,self.nc)

obj = A()
obj._A__display(20,30,40)
obj = B()
obj.show()