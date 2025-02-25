import os

def finding(path):
    if not os.path.exists(path):
        print(f"file {path} exist")
        return 
    
    all_items = os.listdir(path)

    directories = [item for item in all_items if os.path.isdir(os.path.join(path,item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path,item))]

    print(f"Directories in {path}")
    for i in directories:
        print(i)
    print(f"Files in {path}")
    for i in files:
        print(i)

path1 = input("Enter the path to list files and directories:")


finding(path1)

    
