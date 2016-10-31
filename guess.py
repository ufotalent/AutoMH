import sys
s = min(int(sys.argv[1]), int(sys.argv[2]))
t = max(int(sys.argv[1]), int(sys.argv[2]))
ratios = [x / 10.0 for x in range(5, 16)]
for i in ratios:
    for j in ratios:
        if (abs(s / i * j - t) <= 1):
            print i, j, s / i
