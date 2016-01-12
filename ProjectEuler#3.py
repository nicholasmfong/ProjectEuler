primes = [2]
factors = []
for i in range(3,10000):
    for x in primes:
        if i % x == 0:
            break
    else:
        primes.append(i)
def primefactors(w):
    for i in primes:
        if w % i == 0:
            if w / i == 1:
                factors.append(w)
                print('the largest prime factor is',w)
                assert False
            factors.append(i)
            primefactors(w/i)
    else:
        factors.append(w)
primefactors(600851475143)
print(factors)
