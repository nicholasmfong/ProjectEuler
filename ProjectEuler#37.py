import time
start_time = time.time()
from math import sqrt
primes = [2]
answer = []
for i in range(3,740000,2):
    for j in primes:
        if i % j == 0:
            break
        if j > sqrt(i):
            primes.append(i)
            break

for elem in primes:
    if elem <10:
        continue
    item = str(elem)
    if item[0] == 1 or item[0] == 4 or item[0] == 6 or item[0] == 8 or item[0] == 9:
        continue
    if item[-1] == 1:
        continue
    test = 0
    while len(item) > 1:
        item = item[1:]
        if int(item) not in primes:
            test = True
            item = []
    if test:
        continue
    item = str(elem)
    while len(item) > 1:
        item = item[:-1]
        if int(item) not in primes:
            test += True
            item = []
    if test:
        continue
    answer.append(elem)

print(answer,len(answer))
print(sum(answer))
print('It took', time.time() - start_time, 'seconds to run')
