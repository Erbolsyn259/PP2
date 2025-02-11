from datetime import datetime,timedelta

datenow = datetime.now()

newdate= datenow - timedelta(days=5)

print(newdate)