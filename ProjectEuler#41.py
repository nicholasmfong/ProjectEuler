import time
initial_time = time.time()
from math import sqrt
primes = [2]
for number in range(3,31624,2):
    for elem in primes:
        if number % elem == 0:
            break
        if elem > sqrt(number):
            primes.append(number)
            break
answer = 0
filler = ''
for a in range(1,10):
    filler += str(a)
    for b in range(1,10):
        if str(b) in filler:
            continue
        filler += str(b)
        for c in range(1,10):
            if str(c) in filler:
                continue
            filler += str(c)
            for d in range(1,10):
                if str(d) in filler:
                    continue
                filler += str(d)
                for e in range(1,10):
                    if str(e) in filler:
                        continue
                    filler += str(e)
                    for f in range(1,10):
                        if str(f) in filler:
                            continue
                        filler += str(f)
                        for g in range(1,10):
                            if str(g) in filler:
                                continue
                            filler += str(g)
                            if '8' not in filler and '9' not in filler and g % 2 == 1:
                                    test = True
                                    for prime in primes:
                                        if int(filler) % prime == 0:
                                            test = False
                                            break
                                    if test:
                                        if int(filler) > answer:
                                            answer = int(filler)
                            for h in range(1,10):
                                if str(h) in filler:
                                    continue
                                filler += str(h)
                                if '9' not in filler and h % 2 == 1:
                                    test = True
                                    for prime in primes:
                                        if int(filler) % prime == 0:
                                            test = False
                                            break
                                    if test:
                                        if int(filler) > answer:
                                            answer = int(filler)
                                for i in range(1,10):
                                    if str(i) in filler:
                                        continue
                                    if i % 2 == 0:
                                        continue
                                    filler += str(i)
                                    test = True
                                    for prime in primes:
                                        if int(filler) % prime == 0:
                                            test = False
                                            break
                                    if test:
                                        if int(filler) > answer:
                                            answer = int(filler)
                                    filler = filler[:8]
                                filler = filler[:7]
                            filler = filler[:6]
                        filler = filler[:5]
                    filler = filler[:4]
                filler = filler[:3]
            filler = filler[:2]
        filler = filler[:1]
    filler = ''

print(answer)
print('it took',time.time() - initial_time,'seconds to run')
