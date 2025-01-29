class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40
print(p1.age)

del p1.name
#print(p1.name)

del p1
#print(p1)

class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement
