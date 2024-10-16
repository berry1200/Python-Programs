# 3.Write a Python class named Student with two instances regno & name and Create
#  Student_mark class (which inherit Student)with attributes mark1,mark2,mark3 out of 100 each.
#  Create another Result class(which inherit Student_mark) with attributes tot which calculate
# total and another attribute per to calculate percentage.
# Finally, Print Result sheet with regno,name ,marks, total and percentage.


class student:
    def stud(s):
        s.r = int(input("enter regester no :"))
        s.na = str(input("enter student name : ")) 
class Student_mark(student):
    def marks(s):
        s.m1 = int(input("enter mark1 :"))
        s.m2 = int(input("enter mark2 :"))
        s.m3 = int(input("enter mark3 :"))
class result(Student_mark):
    def tot(s):
        s.total = s.m1/100 + s.m2/100 + s.m3/100         
    def per(s):
        s.percentage = s.total * 100

    def result(s):
        print(f'STUDENT    SHEET  \n regester no:{s.r}\n student name:{s.na}\n mark1:{s.m1} \n mark2:{s.m2} \n mark3:{s.m3}')
        print("total mark :",s.total)
        print("percentage :",s.percentage)

obj = result()
obj.stud()
obj.marks()
obj.tot()
obj.per()
obj.result()
