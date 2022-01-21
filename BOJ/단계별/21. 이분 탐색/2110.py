import sys

n, c = map(int, sys.stdin.readline().split())
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline()))
houses.sort()

s, e = 1, houses[-1] - houses[0]

while s <= e:
    m = (s + e) // 2
    last = houses[0]
    count = 1

    for i in range(1, n):
        if houses[i] >= last + m:
            count += 1
            last = houses[i]

    if count >= c:
        s = m + 1
    else:
        e = m - 1

print(e)