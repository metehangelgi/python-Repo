# datetime module
from datetime import date
date.today()

today = date.today()
today

import time
time.time()


"""
time.asctime([t]) : Convert a tuple or struct_time representing a time
as returned by gmtime() or localtime() to a string of the following form: ,
'Sun Jun 20 23:21:05 1993'.
If t is not provided, the current time as returned by localtime() is used.
"""
time.asctime()
#'Sat Jul 28 14:39:59 2018'
"""
Convert a time expressed in seconds since the epoch to a string
representing local time.
If secs is not provided or None, the current time as returned by time() is used. 
"""
time.ctime()
#'Sat Jul 28 14:42:21 2018'
time.localtime()
#time.struct_time(tm_year=2018, tm_mon=7, tm_mday=28, tm_hour=14, tm_min=44, tm_sec=47, tm_wday=5, tm_yday=209, tm_isdst=0)

time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
#'Sat, 28 Jul 2018 11:49:53 +0000'
today == date.fromtimestamp(time.time())

time.strptime("28 Jul 18", "%d %b %y")
#time.struct_time(tm_year=2018, tm_mon=7, tm_mday=28, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=209, tm_isdst=-1)

d = date.fromordinal(736920)
d
t = d.timetuple()
#time.struct_time(tm_year=2018, tm_mon=8, tm_mday=14, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=226, tm_isdst=-1)
#handling date tuple
for i in t:     
    print(i)

d.isoformat()
#'2018-08-14'
d.strftime("%d/%m/%y")
#'14/08/18'
d.strftime("%A %d. %B %Y")
#'Tuesday 14. August 2018'
'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
#'The day is 14, the month is August.'

from datetime import datetime
datetime.now().isoformat(timespec='minutes')
#'2018-07-28T15:35'
dt=datetime.now()
dt
#datetime.datetime(2018, 7, 28, 15, 36, 59, 804733)

dt.isoformat(timespec='microseconds')
#'2018-07-28T15:36:59.804733'

from datetime import date
d1 = date(2018, 7, 28)
d1
#datetime.date(2018, 7, 28)

d2=date(2018,8,11)
d2-d1
#datetime.timedelta(14)

from datetime import time
t = time(12, 30)
t
#datetime.time(12, 30)
dt=datetime.combine(d, t)
dt
#datetime.datetime(2018, 7, 28, 12, 30)

from datetime import time
time(hour=12, minute=34, second=56, microsecond=123456).isoformat(timespec='minutes')
#'12:34'
dt = time(hour=12, minute=34, second=56, microsecond=0)
dt.isoformat(timespec='microseconds')
#'12:34:56.000000'
dt.isoformat(timespec='auto')
#'12:34:56'

#TIMEDELTA 
from datetime import timedelta
datetime.today()
#datetime.datetime(2018, 7, 28, 23, 31, 5, 81522)
today = datetime.today()

timedelta(days=1)
#datetime.timedelta(1)

one_day = timedelta(days=1)
yesterday = today - one_day
yesterday
#datetime.datetime(2018, 7, 27, 23, 31, 16, 695693)

tomorrow = today + one_day
tomorrow
#datetime.datetime(2018, 7, 29, 23, 31, 16, 695693)

tomorrow - yesterday
#datetime.timedelta(2)

yesterday - tomorrow
#datetime.timedelta(-2)

today > tomorrow
#False
today < tomorrow
#True

#calendar module
import calendar
c=calendar.TextCalendar(calendar.MONDAY)
c
#<calendar.TextCalendar object at 0x000000E19B5A2668>
print(c)
#<calendar.TextCalendar object at 0x000000E19B5A2668>
cm1=c.formatmonth(2018,8)
print(cm1)

c_2018=calendar.TextCalendar(calendar.SUNDAY).formatyear(2018, 2, 1, 1, 2)
print(c_2018)

# HTML calendar
c1=calendar.HTMLCalendar(calendar.MONDAY)
cm1=c1.formatmonth(2018,8)
fh=open('calendar.html','w')
fh.write(cm1)
fh.close()

ch_2018=calendar.HTMLCalendar(calendar.SUNDAY).formatyear(1998, width=4)
fh=open('calendar_2018.html','w')
fh.write(ch_2018)
fh.close()

