import re

with open('exampe.txt','r',encoding='utf-8') as row:
    content = row.read()
    math = r"a+[a-zA-Z]*b"
    matches = re.findall(math,content)
    print(matches)