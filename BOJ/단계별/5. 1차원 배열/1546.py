import sys

n = int(sys.stdin.readline())

ls = list(map(int, sys.stdin.readline().split()))

temp = max(ls)
for i in range(n):
    ls[i] = ls[i] / temp * 100
print(sum(ls) / len(ls))
