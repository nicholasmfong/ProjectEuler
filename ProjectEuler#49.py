from math import sqrt
import time
init = time.time()
primes = [2]
for i in range(3,10000,2):      #makes primes
    for x in primes:
        if i % x == 0:
            break
        elif x > sqrt(i):
            primes.append(i)
            break
    else:
        primes.append(i)
intermediate = []       #makes the primes 1000-9999
for j in primes:
    if j > 1000:
        intermediate.append(j)
primes = intermediate
ordered = []        #finds primes with the same digits
for k in primes:
    ordered.append(sorted(str(k)))
ordered = sorted(ordered)
triples = []        #finds the groups of primes that have 3 or more of the same digits
for l in range(len(ordered)):
    if ordered[l] not in triples:
        if ordered.count(ordered[l]) >= 3:
            triples.append(ordered[l])
for o in triples:
    copy = []
    for p in primes:        #finds the actual primes and groups them
        if o == sorted(str(p)):
            copy.append(p)
    copy = sorted(copy)
    for a in range(len(copy)):
        for b in range(a+1,len(copy)):
            if (copy[b] - copy[a] + copy[b]) in copy:   #finds the set of 3 primes with the same difference
                print(copy[a],copy[b],(copy[b] - copy[a] + copy[b]),"\n")

print("time taken =",time.time()-init)
