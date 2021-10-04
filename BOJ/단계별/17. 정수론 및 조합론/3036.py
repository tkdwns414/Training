import sys
import math

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))

for i in range(1, n):
    temp = math.gcd(ls[0], ls[i])
    print(f"{ls[0]//temp}/{ls[i]//temp}")