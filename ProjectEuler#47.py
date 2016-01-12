import time
init = time.time()
from math import sqrt
primes = [2]
composites = []
size = 300000
for i in range(3,size,2):
    for x in primes:
        if i % x == 0:
            break
        elif x > sqrt(i):
            primes.append(i)
            break
    else:
        primes.append(i)

# So if I test for each number, and when something does not have 4 factors I jump 5 ahead
#then work backwwards so I don't have to test as many #s
count = 1

def factored(number):
    for prime in primes:
        if number % prime == 0:
            factor = prime
            return (number / prime, prime)
    else:
        return (number,number)

def numFactors(number):
    factors = []
    factor = 1
    for b in primes:
        if b > number:
            return len(set(factors))
        while number > 1:
            number, factor = factored(number)
            factors.append(factor)
    return len(set(factors))

while count < size:          
    sequence = 0
    while sequence > (-4):
        copy = (count + sequence)
        if numFactors(copy) == 4:
            sequence -= 1
        else:
            count += (4 + sequence)
            break
    if(sequence == -4):
        print(count-3)
        print("time taken =",time.time()-init)
        break



