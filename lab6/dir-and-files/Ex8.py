import os

def delet(path):
    if not os.path.exists(path):
        print(f"Path {path} is not found")
        return
    os.remove(path)

path1 = input("Enter your path ")

delet(path1)