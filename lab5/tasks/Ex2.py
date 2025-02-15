import re

with open('exampe.txt','r',encoding='utf-8') as row:
    content = row.read()
    pattern = r"ab{2,3}"
    matches = re.findall(pattern,content)
    print(matches)