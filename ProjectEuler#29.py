terms = []
for i in range(2,101):
    for j in range(2,101):
        terms.append(i ** j)
terms = set(terms)
print(len(terms))
