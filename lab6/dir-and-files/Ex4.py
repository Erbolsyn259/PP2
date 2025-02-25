import os

def count(path):
    if not os.path.exists(path):
        print(f"Path {path} is not found")
        return
    file = open(path,'r')
    pathes = file.readlines()
    count = len(pathes)
    print(f"count of lines {count}")

path1 = input("Enter your path")

count(path1)