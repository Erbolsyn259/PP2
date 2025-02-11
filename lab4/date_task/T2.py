from datetime import datetime,timedelta

datenow = datetime.now()

dateyes = datenow - timedelta(days=1)

datetom = datenow + timedelta(days=1)

print(f"today{datenow} yesterday{dateyes} tomorow{datetom}")