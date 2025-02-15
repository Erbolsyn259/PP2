import re

with open('exampe.txt','r',encoding='utf-8') as row:
    content = row.read()
    component = re.split('(?=[A-Z])',content)
    print(component)