#0 = sunday, 1 = monday, 2 = tuesday, 3 = wed, 4 = thu, 5 = fri, 6 = sat
count = 0
day = 2
year = 1901
while year < 2001:
    time = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        time[1] = 1
    for i in time:
        if day % 7 == 0:
            count += 1
        day += i
    time[1] = 0
    year += 1
print(count)
