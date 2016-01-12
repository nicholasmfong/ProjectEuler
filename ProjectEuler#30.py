answers = 0
for i in range(2,350000):
    test = 0
    for j in str(i):
        test += int(j) ** 5
    if test == i:
        answers += i
print(answers)
