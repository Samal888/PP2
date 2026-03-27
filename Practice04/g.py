from datetime import datetime, date, timedelta
a=datetime(2025, 1, 1, 0, 0,0)
b=datetime(2026, 1, 1, 0, 0,0)
c=a
count=0
while c<b:
    if c.day==31:
        count+=1
    c=c+timedelta(days=1)
    print(c)
print(count)