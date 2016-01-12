longest_chain = 0
number = 0
for i in range(3,1000000):
    value = i
    chain = 1
    if i % 2 == 0:
        continue
    while value != 1:
        if value % 2 == 0:
            value = value / 2
            chain += 1
        else:
            value = value * 3 + 1
            chain += 1
    if chain > longest_chain:
        longest_chain = chain
        number = i
print(number,longest_chain)
        
