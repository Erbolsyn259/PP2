class MyClass:
  x = 5

print(MyClass)

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"
  def myfunc(self):
    print("Hello my name is " + self.name)


p1 = Person("John", 36)

print(p1)

p1.myfunc()
