import sys
from math import factorial

n = int(sys.stdin.readline())

for _ in range(n):
    n, m = map(int, sys.stdin.readline().split())
    print(factorial(m) // (factorial(m - n) * factorial(n)))

# 수학 조교 한지 2년 됐다고 쉬운 확통 문제도 까먹네...
# 왼쪽 순서는 이미 정헤졌으니까 오른쪽에서 n개 뽑기만 하면 순서대로 쏴야함 -> 조합