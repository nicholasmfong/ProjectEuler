def divisors(num):
    factors = []
    for i in range(1,(num//2)+1):
        if num % i == 0:
            factors.append(i)
    total = 0
    for j in factors:
        total += j
    return total
answer = 0
for elem in range(3,10000):
    test = divisors(elem)
    if divisors(test) == elem and test != elem:
        answer += elem
print(answer)
