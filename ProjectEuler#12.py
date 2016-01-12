triangle = 1
number = 2
factors = []
while len(factors) < 501:
    triangle += number
    number += 1
    factors = []
    if triangle % 12 != 0 or triangle < 500 **2:
        continue
    for i in range(1,triangle):
        if i > triangle ** 0.5:
            filler = factors[:]
            for i in filler:
                factors.append(i)
            break
        if triangle % i == 0:
                factors.append(i)
print(triangle,len(factors))
