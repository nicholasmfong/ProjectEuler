from math import sqrt
n = 286
while True:
    Triangle = n * (n + 1) / 2
    if (1 + sqrt(1 + 24 * Triangle)) / 6 == int((1 + sqrt(1 + 24 * Triangle)) / 6):
        if (1 + sqrt(1 + 8 * Triangle)) / 4 == int((1 + sqrt(1 + 8 * Triangle)) / 4):
            print(int(Triangle),n)
            break
    n += 1
