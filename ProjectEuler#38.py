answer = 0
pandigital = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(1,10000):
    product = ''
    number = 1
    while len(product) < 9:
        product += str(i * number)
        number += 1
    if sorted(product) == pandigital:
        if int(product) > answer:
            answer = int(product)
print(answer)
