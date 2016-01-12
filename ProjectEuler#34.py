from math import factorial
total = 0
for i in range(10,2540000):
    test = 0
    for digit in str(i):
        test += factorial(int(digit))
    if test == i:
        total += i
print(total)
