from datetime import datetime 
now=datetime.now()
print(now)
day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
second=now.second
print(day,month,year,hour)
print(f"{month}/{day}/{year}, {hour}:{minute}")

# Formatting date output using strftime
now=datetime.now()
t=now.strftime("%H:%M:%S")
print("Time",t)

time_one=now.strftime("%d/%m/%Y, %H:%M:%S")
print(time_one)