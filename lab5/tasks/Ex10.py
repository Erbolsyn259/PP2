import re
with open('exape.txt','r', encoding='utf-8') as row:
    content = row.read()
    math = re.sub(r'([A-Z])', r'_\1',content).lower()
    print(math)