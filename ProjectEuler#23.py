abundant = []
numbers = []
answer = 0
for i in range(12,28123):
    divisors = []
    for j in range(1,i):
        if i % j == 0:
            divisors.append(j)
    value = 0
    for k in divisors:
        value += k
    if value > i:
        abundant.append(i)
abundant = sorted(abundant)
for term in abundant:
    for elem in abundant:
        if term + elem > 28123:
            continue
        else:
            numbers.append(term+elem)
numbers = set(numbers)
for a in range(1,28123):
    if a not in numbers:
        answer += a
    else:
        numbers.remove(a)
print(answer)
