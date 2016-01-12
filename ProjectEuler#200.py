##citing:
##    http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
##    http://en.wikipedia.org/wiki/Fermat_primality_test
from math import sqrt
primes = [2]        # finds the primes to use to find squbes
for i in range(3,200000,2):
    for j in primes:
        if i % j == 0:
            break
        elif j > sqrt(i):
            primes.append(i)
            break
    else:
        primes.append(i)

def proof(number):   # tests the numbers to see if they are prime proof. See citations for how this works
    '''number is real number // 10'''
    number = number * 10 + 1
    numbers = [number,number + 2,number + 6,number + 8]
    n = [number-1,number + 1,number + 5,number +7]
    x = [2,3,5,7,11,13,17]
    for i in range(4):
        fermat = 0
        for j in x:
            if pow(j,n[i],numbers[i]) == 1:
                fermat += 1
            if fermat > 2:
                return False
    else:
        return True

def sqube(p,q):         
    return (p ** 2) * (q ** 3)

squbes = []

for a in primes:        # where all the work happens
    x = sqube(2,a)
    y = sqube(a,2)
    n = sqube(5,a)
    m = sqube(a,5)
    if '200' in str(n):
        if proof(n//10):
            squbes.append(n)
    if '200' in str(m):
        if proof(m//10):
            squbes.append(m)
    if '200' in str(x):
        if proof(x//10):
            squbes.append(x)
    if '200' in str(y):
        if proof(y//10):
            squbes.append(y)

squbes = sorted(squbes)
#print(len(squbes))
print(squbes[200])
    
