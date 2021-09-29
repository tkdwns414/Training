from math import ceil

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        floor = h
    else:
        floor = n % h
    print("%d%02d" % (floor, ceil(n / h)))
