total = 1
for i in range(1,101):
    total *= i
total = str(total)
answer = 0
for j in total:
    answer += int(j)
print(answer)
