from math import sqrt
primes = [2]
for i in range(3,10000,2):
    for j in primes:
        if i % j == 0:
            break
        elif j > sqrt(i):
            primes.append(i)
            break
    else:
        primes.append(i)

answer = 0
result = []
for a in range(-999,1000):
    for b in range(2,1000):
        if abs(b) not in primes:
            continue
        length = [b]
        n = 1
        x = (n ** 2 + a * n + b)
        while abs(x) in primes:
            length.append(x)
            n += 1
            x = (n ** 2 + a * n + b)
        if len(length) > answer:
            answer = len(length)
            result = [a,b]

print(result,answer,result[0] * result[1])
