class gen:
    def __init__(self,b):
        self.a = 0
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        if self.a % 2 == 0:
            x = self.a
            self.a+=1
            return x
        if self.b <= self.a:
            raise StopIteration
        self.a += 1
        return self.__next__()
    
n = int(input("enter your int"))

myclass = gen(n)

myiter = iter(myclass)


print(', '.join(str(i) for i in myiter))
