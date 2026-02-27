from datetime import datetime, date, timedelta

# Current datetime
now = datetime.now()

# 1
five_days_ago = now - timedelta(days=5)

# 2
yesterday = now - timedelta(days=1)
today = now
tomorrow = now + timedelta(days=1)

# 3
without_microseconds = now.replace(microsecond=0)

# 4
date1 = datetime(2026, 2, 20, 10, 0, 0)
date2 = datetime(2026, 2, 27, 12, 0, 0)
difference_seconds = int((date2 - date1).total_seconds())

# Print results
print("Now:", now)
print("5 days ago:", five_days_ago)

print("\nYesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

print("\nWithout microseconds:", without_microseconds)

print("\nDifference in seconds:", difference_seconds)