import sys

temp = list(map(int, sys.stdin.readline().split()))
res = 0
for num in temp:
    res += pow(num, 2)
    res %= 10
print(res)