import os

def chek(path):
    if not os.path.exists(path):
        print(f"path {path} does not exist")
        return
    if os.access(path, os.R_OK):
        print("Read is ok")
    else:
        print("Read is not ok")
    if os.access(path, os.W_OK):
        print("Write is ok")
    else:
        print("Write is not ok")
    if os.access(path, os.R_OK):
        print("Execute is ok")
    else:
        print("Execute is not ok")
    
path1 = input("Enter your path ")

chek(path1)
    

