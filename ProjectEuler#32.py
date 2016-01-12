products = []
answer = 0
filler = []
for a in range(1,10):
    filler.insert(0,str(a))
    for b in range(1,10):
        if str(b) in filler:
            continue
        filler.insert(1,str(b))
        for c in range(1,10):
            if str(c) in filler:
                continue
            filler.insert(2,str(c))
            for d in range(1,10):
                if str(d) in filler:
                    continue
                filler.insert(3,str(d))
                for e in range(1,10):
                    if str(e) in filler:
                        continue
                    filler.insert(4,str(e))
                    for f in range(1,10):
                        if str(f) in filler:
                            continue
                        filler.insert(5,str(f))
                        for g in range(1,10):
                            if str(g) in filler:
                                continue
                            filler.insert(6,str(g))
                            for h in range(1,10):
                                if str(h) in filler:
                                    continue
                                filler.insert(7,str(h))
                                for i in range(1,10):
                                    if str(i) in filler:
                                        continue
                                    filler.insert(8,str(i))
                                    one = int(filler[0])
                                    two = int(filler[0] + filler[1])
                                    three = int(filler[2] + filler[3] + filler[4])
                                    four = int(filler[1] + filler[2] + filler[3] + filler[4])
                                    product = int(filler[5] + filler[6] + filler[7] + filler[8])
                                    if one * four == product or two * three == product:
                                        products.append(product)
                                    filler.remove(str(i))
                                filler.remove(str(h))
                            filler.remove(str(g))
                        filler.remove(str(f))
                    filler.remove(str(e))
                filler.remove(str(d))
            filler.remove(str(c))
        filler.remove(str(b))
    filler.remove(str(a))        
products = set(products)
for item in products:
    answer += item
print(answer)
                
    
