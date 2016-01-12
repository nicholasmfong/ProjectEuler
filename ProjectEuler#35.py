from math import sqrt
primes = [2]
circular = 1   #starts at one to account for the fact that the optimization process will try to subtract it

for i in range(3,1000000,2):
    for j in primes:
        if i % j == 0:
            break
        elif j > sqrt(i):
            primes.append(i)
            break
    else:
        primes.append(i)
        
for elem in primes:
    string = str(elem)
    rotated = string[1:] + string[0:1]
    for digit in string:
        if int(digit) % 2 == 0:
            rotated = string
            circular -= 1
            break
    while rotated != string:
        if int(rotated) not in primes:
            break
        rotated = rotated[1:] + rotated[0:1]
    if rotated == string:
        circular += 1

print(circular)
