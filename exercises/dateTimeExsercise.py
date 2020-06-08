import datetime
import time
import calendar




month=int(input("please enter your birthday month"))
day=int(input("please enter your birthday day"))


birth=datetime.date(year=2019,month=month,day=day)
datetime.time()
print(birth)

nowtime=datetime.date.today()

print(nowtime)



print(nowtime-birth)
if((nowtime-birth).days<0):
    print("you will have birthday in ",abs((nowtime-birth).days)," days")
else:
    print("your birtday passed in ",(nowtime-birth).days," days")




import datetime
from datetime import datetime
monday1 = 0
months = range(1,13)
for year in range(2018, 2020):
    for month in months:
        if datetime(year, month, 1).weekday() == 0:
            monday1 += 1
print(monday1)

months1=range(1,13)
for year1 in range(2019, 2020):
    for month1 in months1:
       print(month1," ",year1," First Monday is",datetime(year1,month1,1).weekday()+1)






