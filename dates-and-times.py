"""
Dates and times
"""

import datetime

date = datetime.date(2024, 1, 1)
today = datetime.date.today()

time = datetime.time(12, 30, 45)
now = datetime.datetime.now()

print(date)
print(today)

print(time)
print(now)

formatted_now = now.strftime("%H:%M:%S")

print(formatted_now)
