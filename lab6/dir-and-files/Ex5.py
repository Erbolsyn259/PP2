import os

path = input("Enter your path ")
list = []
try:
    w = open(path,'w')
    for i in range(0,3):
        line = input("Enter your line")
        list.append(line)
    for i in list:
        w.write(f"{i}\n")

except NameError:
    print(f"Path {path} is not found")

