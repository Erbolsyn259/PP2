class square:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        if self.a > self.b:
            raise StopIteration
        else:
            x = self.a
            self.a +=1
            return x*x
        return self.__next__()

a = int(input("enter start num"))

b = int(input("enter end num"))

myclass = square(a,b)

myiter = iter(myclass)

for i in myiter:
    print(i)