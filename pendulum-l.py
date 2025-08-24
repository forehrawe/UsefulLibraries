import pendulum 

# time = pendulum.Date(1994, 4, 10)
# print(time)

# time2 = pendulum.time(10,20,30,40)
# print(time2)

time3 = pendulum.now()
print(time3)

shift = time3.add(days=3).strftime('%Y/%M/%d')
print(shift)