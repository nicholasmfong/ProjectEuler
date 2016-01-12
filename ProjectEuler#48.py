import time
init = time.time()
total = 0
for i in range(1,1001):
    exp = str(pow(i,i))
    exp = exp[-10:]
    total += int(exp)
total = str(total)
total = total[-10:]
print(int(total))
print("time taken =",time.time()-init)
