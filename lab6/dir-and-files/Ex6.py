import os

for i in range(0,26):
    filename = chr(65 + i) + ".txt"
    f = open(filename,'w')
    print(f"{filename} is created")

f.close()
path = input("Enter 'Love' if you want to delate fails: ")

if path == "Love":
    for i in range(0,26):
        filename = chr(65 + i) + ".txt"
        os.remove(filename)
