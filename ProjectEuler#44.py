import time
initial_time = time.time()
pentagons = []
answer = [0,0,9999999999]
for n in range(1,2500):
    pentagons.append(int(n * (3 * n - 1) / 2))
for j in range(len(pentagons)):
    for k in range(j):
        if abs(pentagons[j] - pentagons[k]) > answer[2]:
            continue
        if (pentagons[j] - pentagons[k] - 1)/3 != int((pentagons[j] - pentagons[k] - 1)/3):
            continue
        if pentagons[j] + pentagons[k] in pentagons:
            if pentagons[j] - pentagons[k] in pentagons:
                if abs(pentagons[j] - pentagons[k]) < answer[2]:
                    answer = [pentagons[j],pentagons[k],abs(pentagons[j]-pentagons[k])]
print(answer)
print(time.time() - initial_time,'seconds')
