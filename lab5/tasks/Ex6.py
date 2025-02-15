import re

with open('exampe.txt','r',encoding='utf-8') as row:
    content = row.read()
    matches = re.sub("[,]|[.]|\s",":",content)
    print(matches)