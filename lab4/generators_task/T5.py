class gen:
    def __init__(self,a):
        self.a = a
    def __iter__(self):
        return self
    def __next__(self):
        x = self.a
        if self.a == 0:
            raise StopIteration
        if self.a < 0:
            self.a +=1
        elif self.a > 0:
            self.a -=1
        return x
a = int(input("enter num"))
myclass = gen(a)
myiter = iter(myclass)

for i in myiter:
    print(i)

