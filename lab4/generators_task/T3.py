class gen:
    def __init__(self,b):
        self.a = 0
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        if self.a >= self.b:
            raise StopIteration
        if self.a % 3 ==0 and self.a % 4 == 0:
            x = self.a 
            self.a += 1
            return x
        self.a += 1
        return self.__next__()
n = int(input("enter your num"))
myclass = gen(n)
myiter = iter(myclass)

for i in myiter:
    print(i)