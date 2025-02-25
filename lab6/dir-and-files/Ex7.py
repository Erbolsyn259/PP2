import os

path = input("Enter your path for read ")

content = open(path,'r')

plagiat = open('plagiat.txt','w')

plagiat.write(content.read())

plagiat.close()

#os.remove('plagiat.txt')