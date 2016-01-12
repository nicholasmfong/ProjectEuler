import time
initial = time.time()
answer = 0
number = 1
while answer == 0:
    if sorted(str(number * 2)) == sorted(str(number)):
        if sorted(str(number * 3)) == sorted(str(number)):
            if sorted(str(number * 4)) == sorted(str(number)):
                if sorted(str(number * 5)) == sorted(str(number)):
                    if sorted(str(number * 6)) == sorted(str(number)):
                        answer = number
    number += 1
print(answer)
print('time =', time.time() - initial, 'seconds')
