fib1 = 1
fib2 = 2
fib3 = 3
total = 0
while fib2 < 4000000:
    if fib2 % 2 == 0:
        total += fib2
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
print(total)
    
