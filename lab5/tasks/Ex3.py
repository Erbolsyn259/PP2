import re

with open('exampe.txt','r',encoding='utf-8') as row:
    content = row.read()
    pattern = r"[a-z]+_[a-z]*"
    matches = re.findall(pattern,content)
    print(matches)