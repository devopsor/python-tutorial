################################ DataTime ################################ 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone

#Get current datetime:
now = datetime.now()
print('now =', now)  #now = 2022-08-12 21:08:51.324786
print('type(now) =', type(now))  #type(now) = <class 'datetime.datetime'>

# Create datetime with specified datetime
dt = datetime(2015, 4, 19, 12, 20, 10)
print('dt =', dt) #dt = 2015-04-19 12:20:10

# Convert datetime to timestamp:
print('datetime -> timestamp:', dt.timestamp()) #datetime -> timestamp: 1429413610.0

# Convert timestamp to datetime:
t = dt.timestamp()
#timestamp -> datetime: 2015-04-19 12:20:10
print('timestamp -> datetime:', datetime.fromtimestamp(t)) 

#timestamp -> datetime as UTC+0: 2015-04-19 03:20:10
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t)) 

# Read datetime from str:
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print('strptime:', cday) #strptime: 2015-06-01 18:19:59

# Format datetime output:
print('strftime:', cday.strftime('%a, %b %d %H:%M')) #strftime: Mon, Jun 01 18:19

# Add or subtract dates:
print('current datetime =', cday) #current datetime = 2015-06-01 18:19:59
print('current + 10 hours =', cday + timedelta(hours=10)) #current + 10 hours = 2015-06-02 04:19:59
print('current - 1 day =', cday - timedelta(days=1)) #current - 1 day = 2015-05-31 18:19:59
print('current + 2.5 days =', cday + timedelta(days=2, hours=12)) #current + 2.5 days = 2015-06-04 06:19:59

#Convert time from UTC+0 time zone to UTC+8:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt) #UTC+0:00 now = 2022-08-12 12:09:31.478413+00:00    
print('UTC+8:00 now =', utc8_dt) #UTC+8:00 now = 2022-08-12 20:09:31.478413+08:00    







