import sys

n = int(sys.stdin.readline())

ls = list(map(int, sys.stdin.readline().split()))

ls.sort()
length = len(ls)

result = 0

for i in range(n):
    result += ls[i] * (length - i)

print(result)