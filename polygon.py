class A:
    def polygon(s):
        s.n = int(input("enter no of side : "))
class B(A):
    def triangle(self):
        if self.n==3:
            print("this is triangle")
        else:
            print("its an other polygon")
class C(A):
    def square(self):
        if self.n==4:
            print("this is square")
        else:
            print("its an other polygon")
class D(A):
    def pentagon(self):
        if self.n==5:
            print("this is pentagon")
        else:
            print("its an other polygon")
obj = B()
obj.polygon()
obj.triangle()
obj = C()
obj.polygon()
obj.square()
obj = D()
obj.polygon()
obj.pentagon()
