sumsquares = 0
total = 0
for i in range(1,101):
    total += i
    sumsquares += i**2
total = total ** 2
print('difference =',total-sumsquares)
