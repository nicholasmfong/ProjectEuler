pascals = [1,2,1]
while len(pascals) < 41:
    intermediate = [1]
    for i in range(len(pascals)-1):
        intermediate.append(pascals[i] + pascals[i+1])
    intermediate.append(1)
    pascals = intermediate
print(pascals[20])
