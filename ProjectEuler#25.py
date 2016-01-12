a,b = 1,1
term = 2
while len(str(a)) < 1000:
    a,b = a+b,a
    term += 1
print(a,term)
