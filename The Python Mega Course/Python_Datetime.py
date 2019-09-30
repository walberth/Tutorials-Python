import datetime
import time

now = datetime.datetime.now()
yesterday = datetime.datetime(2016, 5, 13, 11, 0, 0, 0)

delaytime = now + datetime.timedelta(days=2)

delta = now - yesterday

#print(delta.total_seconds())
#print(delaytime)

list = []

for i in range(5):
    list.append(datetime.datetime.now())
    time.sleep(1)

for x in list:
    print(x)
