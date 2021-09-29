# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16
# 1, 2, 3, 4, 5, 6, 7, 8(+3), 9(8+4), 10(9+5), 11(10+6), 12(11+7)
import sys

info = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(len(info), 101):
    info.append(info[i - 1] + info[i - 5])

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    print(info[n - 1])
