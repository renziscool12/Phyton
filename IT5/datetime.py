import datetime
from datetime import date

date1 = datetime.date.today()
#date1 = datetime.date(2027,1,1)
#print(date1)
#print(date1.year)
#print(date1.month)
#print(date1.day)
#print(datetime.datetime.fromisoformat('2026-09-03 13:09:19.103249'))
#print(datetime.datetime.fromisoformat('04:23:01+04:00'))
#print(date.fromisoformat('2019-01-04'))

date2 = datetime.datetime.today()
#print(date2)
#print(date2.month)
#print(date2.day)
#print(date2.hour)
#print(date2.minute)
#print(date2.second)
#print(date2.microsecond)

date3 = datetime.timedelta(days=4)
date4 = datetime.timedelta(days=4, seconds=0, microseconds=0,\
                           milliseconds=0, minutes=3, hours=1,\
                           weeks=2)
print(date3)
print(date4)
print(date2 + date3)
print(3 * date3)
print(date3 / 2)
print(date4 % date3)
print(abs(date3 - date4))
print(date3.total_seconds())

date5 = date1 + date3
date6 = date1 + date4

print(date5)
print(date6)
print(date5 > date6)

print(date.today().strftime("%d/%m/%y"))
print(date.today().strftime("%A %d %B %Y"))
arawNgDavao = date.fromordinal(730920)
print(arawNgDavao)
print('The {1} is {0:%d}, the {2} is {0:%B}.'.format(arawNgDavao, "day", "month"))


