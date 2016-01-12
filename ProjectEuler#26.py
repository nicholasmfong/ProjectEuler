recur = 0
answer = 0
for i in range(2,1001):
    repeats = []
    divide = 10
    while divide not in repeats:
        repeats.append(divide)
        divide = (divide % i) * 10
        if divide == 0:
            break
    if divide == 0:
        recurring = 0
    else:
        recurring = len(repeats) - repeats.index(divide)
    if recurring > recur:
        recur = recurring
        answer = i
print(answer)
