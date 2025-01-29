def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction():
  pass           # having an empty function definition like this, would raise an error without the pass statement

def my_function(x, /):
  print(x)

my_function(3)

def my_function(x):
  print(x)

my_function(x = 3)

def my_function(*, x):
  print(x)

my_function(x = 3)

def my_function(x):
  print(x)

my_function(3)

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)