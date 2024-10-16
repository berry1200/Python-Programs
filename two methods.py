# 2.Write a Python class that has two methods: get_String and print_String , get_String accept a 
# string from the user and print_String prints the string in upper case.

class A:
    def get_String(s):
        s.n = input("enter a string :")

    def print_String(s):
        return s.n.upper()
obj = A()
obj.get_String()
print(obj.print_String())