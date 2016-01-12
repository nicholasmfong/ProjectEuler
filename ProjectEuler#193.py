import time
init = time.time()
numbers = []
for i in range(1,33554433):   #all #s up to sqrt(2^50)
    numbers.append(i)
answers = numbers
numbers.remove(1)
for j in numbers:
    for k in answers:
        if j ** 2 > k:
            continue
        elif k % j == 0:
            answers.remove(k)
            continue

print(len(answers))
print("time taken =",time.time()-init)
