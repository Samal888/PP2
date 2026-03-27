from datetime import datetime, date, timedelta

# Current datetime
now = datetime.now()

d1



# 1
a = now - timedelta(days=5)

# 2
yst = now - timedelta(days=1)
today = now
tmr = now + timedelta(days=1)

# 3
b= now.replace(microsecond=0)

# 4
d1 = datetime(2026, 2, 20, 10, 0, 0)
d2 = datetime(2026, 2, 27, 12, 0, 0)
diff = int((d2 - d1).total_seconds())


print("Now:", now)
print(a)

print(yst)
print(today)
print(tmr)

print(b)

print(diff)