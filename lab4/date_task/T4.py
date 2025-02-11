from datetime import datetime,timedelta

date1 = datetime(2005,1,28)

date2 = datetime(2006,11,6)

date  = date1 - date2

sec = date.total_seconds()

print(sec)