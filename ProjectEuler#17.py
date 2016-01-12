letters = 11 #letters in one thousand    
for i in range(1,1000):
    hundreds = i // 100
    tens = (i - 100 * hundreds) // 10
    ones = i - 10 * tens - 100 * hundreds
    if hundreds > 0:
        if i % 100 == 0:
            letters += 7
        else:
            letters += 10
    if tens == 2 or tens == 3 or tens == 8 or tens == 9:
        letters += 6
    if tens == 4 or tens == 5 or tens == 6:
        letters += 5
    if tens == 7:
        letters += 7
    filler = tens * 10 + ones
    if filler == 10:
        letters += 3
    if filler == 11 or filler == 12:
        letters += 6
    if filler == 13 or filler == 14 or filler == 18 or filler == 19:
        letters += 8
    if filler == 15 or filler == 16:
        letters += 7
    if filler == 17:
        letters += 9
    test = [hundreds,ones]
    if 10 < filler < 20:
        test[1] = 0
    for elem in test:
        if elem == 1 or elem == 2 or elem == 6:
            letters += 3
        if elem == 3 or elem == 7 or elem == 8:
            letters += 5
        if elem == 4 or elem == 5 or elem == 9:
            letters += 4
print(letters)
