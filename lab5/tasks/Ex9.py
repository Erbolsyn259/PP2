import re

with open('exampe.txt','r',encoding='utf-8') as row:
    content = row.read()
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', content)
    print(result)