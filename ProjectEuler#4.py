#Find the largest palindrome made from the product of two 3-digit numbers.
product = 1
for i in range(1,1000):
    for j in range(1,1000):
        test = str(i * j)
        reverse = ''
        for k in range(-1,-len(test)-1,-1):
            reverse = reverse + test[k]
        if test == reverse:
            if int(test) > product:
                product = int(test)
print(product)
