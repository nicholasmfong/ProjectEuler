from math import sqrt
buckets = []
for i in range(1001):
    buckets.append([0,i])

for a in range(1,1000):
    for b in range(1,1000):
        c = sqrt(a ** 2 + b ** 2)
        if c != int(c):
            continue
        perimeter = a + b + int(c)
        if perimeter > 1000:
            continue
        buckets[perimeter][0] += 1

buckets = sorted(buckets)
print(buckets[1000])
