year = int(input("year:\n"))
month = int(input("month:\n"))
day = int(input("day:\n"))

#month = 31,28,31,30, 31, 30, 31, 31, 30, 31, 30,31
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print("Input Error!")
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and year % 100 != 0):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print("it is the %dth days." %sum)


year = int(input("year:\n"))
month = int(input("month:\n"))
day = int(input("day:\n"))
sum = 0
months = (0,31,28,31,30, 31, 30, 31, 31, 30, 31, 30)
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    months[2] += 1
for i in range(month):
    sum += months[i]
print("it is the %dth day." % (sum + day))
