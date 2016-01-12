for i in range(1,333):
    for j in range(i+1,450):
        cc = (i**2 + j**2) ** 0.5
        if cc == round(cc,0):
            if i + j + cc == 1000:
                print('answer =', int(i * j * cc))
            
    
