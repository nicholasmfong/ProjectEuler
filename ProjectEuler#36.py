total = 0
for i in range(1,1000000):
    if str(i) == str(i)[::-1]:
        binary = bin(i)[2:]
        if binary == binary[::-1]:
            total += i

print(total)
