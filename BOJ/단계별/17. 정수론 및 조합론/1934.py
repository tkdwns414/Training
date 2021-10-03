import sys
import math

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a, b))

# 유클리드 호제법이 알고리즘 분류에 있는데 내장 함수 쓰는건 좀 그런가...?
