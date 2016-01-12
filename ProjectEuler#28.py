answer = 1
number = 1
n = 1
while n < 501:
    for i in range(4):
        number += 2 * n
        answer += number
    n += 1
print(answer)
