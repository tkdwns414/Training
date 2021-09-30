import sys

n, k = map(int, sys.stdin.readline().split())


def solve(n, k):
    k = k if k < n - k else n - k


# 이항계수 페르마 정리...? 나중에 공부할게요
