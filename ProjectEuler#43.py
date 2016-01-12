import time
initial_time = time.time()
pandigital = []
total = 0
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
                if d % 2 == 1:
                    continue
                filler += str(d)
                for e in range(0,10):
                    if str(e) in filler:
                        continue
                    if (100*c + 10*d + e) % 3 != 0:
                        continue
                    filler += str(e)
                    for f in range(0,6):
                        if str(f) in filler:
                            continue
                        if f % 5 != 0:
                            continue
                        filler += str(f)
                        for g in range(0,10):
                            if str(g) in filler:
                                continue
                            if (100*e + 10*f + g) % 7 != 0:
                                continue
                            filler += str(g)
                            for h in range(0,10):
                                if str(h) in filler:
                                    continue
                                if (100*f + 10*g + h) % 11 != 0:
                                    continue
                                filler += str(h)
                                for i in range(0,10):
                                    if str(i) in filler:
                                        continue
                                    if (100*g + 10*h + i) % 13 != 0:
                                        continue
                                    filler += str(i)
                                    for j in range(0,10):
                                        if str(j) in filler:
                                            continue
                                        if (100*h + 10*i + j) % 17 != 0:
                                            continue
                                        filler += str(j)
                                        pandigital.append(int(filler))
                                        total += int(filler)
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
print(total)
print('it took',time.time() - initial_time,'seconds to run')
