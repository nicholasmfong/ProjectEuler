lychrel = 9999
for number in range(1,10000):
    count = 0
    test = number
    while count < 50:
        test += int(str(test)[::-1])
        if test == int(str(test)[::-1]):
            lychrel -= 1
            break
        count += 1
print(lychrel)
