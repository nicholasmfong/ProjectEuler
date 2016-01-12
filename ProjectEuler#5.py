nums = [7,9,11,13,15,16,17,19]
for i in range(10000,500000000,10):
    for j in nums:
        if i % j != 0:
            break
    else:
        print(i)
    
