import re

with open('exampe.txt','r',encoding='utf-8') as row:
    content = row.read()
    component = content.split('_')
    camel_case_str = component[0] + ''.join(word.capitalize() for word in component[1:])
    print(camel_case_str)