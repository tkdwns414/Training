t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dis = (x2 - x1) ** 2 + (y2 - y1) ** 2

    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dis == (r1 + r2) ** 2 or dis == (r1 - r2) ** 2:
            print(1)
        elif dis < (r1 + r2) ** 2 and dis > (r1 - r2) ** 2:
            print(2)
        else:
            print(0)