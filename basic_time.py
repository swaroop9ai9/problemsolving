import time;

print(time.localtime(time.time()))

#Formatted time

print(time.asctime(time.localtime(time.time())))

#We can use time.sleep(#no of seconds) to delay the execution
time.sleep(10)

import datetime;
#returns the current datetime object
print(datetime.datetime.now())

import calendar
cal = calendar.month(2020,4)
print(cal)

calendar.prcal(2019)
