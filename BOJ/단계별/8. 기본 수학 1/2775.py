# 시간 초과 때문에 Pypy3로 제출했음
import sys


def people(k, n):
    if n == 1:
        return 1
    elif k == 0:
        return n
    else:
        return people(k, n - 1) + people(k - 1, n)


t = int(sys.stdin.readline())

for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(people(k, n))
