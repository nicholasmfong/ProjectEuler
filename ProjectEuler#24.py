import time
initial_time = time.time()
pandigital = []
filler = ''
for a in range(0,10):
    filler += str(a)
    for b in range(0,10):
        if str(b) in filler:
            continue
        filler += str(b)
        for c in range(0,10):
            if str(c) in filler:
                continue
            filler += str(c)
            for d in range(0,10):
                if str(d) in filler:
                    continue
                filler += str(d)
                for e in range(0,10):
                    if str(e) in filler:
                        continue
                    filler += str(e)
                    for f in range(0,10):
                        if str(f) in filler:
                            continue
                        filler += str(f)
                        for g in range(0,10):
                            if str(g) in filler:
                                continue
                            filler += str(g)
                            for h in range(0,10):
                                if str(h) in filler:
                                    continue
                                filler += str(h)
                                for i in range(0,10):
                                    if str(i) in filler:
                                        continue
                                    filler += str(i)
                                    for j in range(0,10):
                                        if str(j) in filler:
                                            continue
                                        filler += str(j)
                                        pandigital.append(int(filler))
                                        filler = filler[:9]
                                    filler = filler[:8]
                                filler = filler[:7]
                            filler = filler[:6]
                        filler = filler[:5]
                    filler = filler[:4]
                filler = filler[:3]
            filler = filler[:2]
        filler = filler[:1]
    filler = ''

pandigital = sorted(pandigital)
print(pandigital[999999])
print('it took',time.time() - initial_time,'seconds to run')
