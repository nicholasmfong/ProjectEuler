ways = 2
for a in range(2):
    total = a * 100
    if total < 200:
        for b in range(5):
            total = a * 100 + b * 50
            if total < 200:
                for c in range(11):
                    total = a * 100 + b * 50 + c * 20
                    if total < 200:
                        for d in range(21):
                            total = a * 100 + b * 50 + c * 20 + d * 10
                            if total < 200:
                                for e in range(41):
                                    total = a * 100 + b * 50 + c * 20 + d * 10 + e * 5
                                    if total < 200:
                                        for f in range(101):
                                            total = a * 100 + b * 50 + c * 20 + d * 10 + e * 5 + f * 2
                                            if total < 201:
                                                ways += 1
                                            else:
                                                continue
                                    else:
                                        if total == 200:
                                            ways += 1
                            else:
                                if total == 200:
                                    ways += 1
                    else:
                        if total == 200:
                            ways += 1
            else:
                if total == 200:
                    ways += 1
    else:
        if total == 200:
            ways += 1

print(ways)
