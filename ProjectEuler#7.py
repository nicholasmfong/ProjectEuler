primes = [2]
i = 3
while len(primes)<10002:
    for x in primes:
        if i % x == 0:
            i += 1
            break
    else:
        primes.append(i)
        i += 1
print(primes[10000])
