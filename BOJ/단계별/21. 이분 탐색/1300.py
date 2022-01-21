import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
s, e = 1, k
while s <= e:
    m = (s + e) // 2
    temp = 0

    for i in range(1, n + 1):
        temp += min(m // i, n)

    if temp >= k:
        res = m
        e = m - 1
    else:
        s = m + 1
print(res)