answers = []
for denominator in range(11,100):
    for numerator in range(10,denominator):
        fraction = numerator / denominator
        result = [numerator,denominator,fraction]
        numer = str(numerator)
        denom = str(denominator)
        num = 100
        den = 1
        for i in range(2):
            for j in range(2):
                if numer[i] == denom[j] and numer[i] != '0':
                    if i == 0:
                        num = numer[1]
                    else:
                        num = numer[0]
                    if j == 0:
                        den = denom[1]
                    else:
                        den = denom[0]
                    break
        if num == '0' or den == '0':
            continue
        new = int(num) / int(den)
        if new == fraction:
            answers.append(result)
            break
test = 1
for elem in answers:
    test *= elem[2]
print(round(1/test))
