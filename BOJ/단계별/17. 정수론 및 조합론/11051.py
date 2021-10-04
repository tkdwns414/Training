import sys
from math import factorial

input = sys.stdin.readline

n, k = map(int, input().split())
print((factorial(n) // (factorial(n - k) * factorial(k))) % 10007)
