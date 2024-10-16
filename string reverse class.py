class StringReversal:
    def id(self):
        self.n = (input("enter a string : "))
    def reverse(self):
        words = self.n.split()
        reversed_string = ' '.join(reversed(words))
        print(reversed_string)
    
obj = StringReversal()
obj.id()
obj.reverse()
