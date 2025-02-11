import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2006, 11, 6)

print(x)

print(x.strftime("%B"))