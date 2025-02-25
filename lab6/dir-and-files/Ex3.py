import os

def chek(path):
    if not os.path.exists(path):
        print(f"path {path} does not exist")
        return
    
    directory =  os.path.dirname(path)
    print(f"Directory portion of the path {path}")

    files = os.path.basename(path)
    print(f"Files portion of the path {path}")

path1 = input("Enter your path")

chek(path1)