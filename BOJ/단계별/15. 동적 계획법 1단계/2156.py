import sys

n = int(sys.stdin.readline())
ls = [0 for i in range(10001)]
for i in range(n):
    ls[i] = int(sys.stdin.readline())

dp = []
dp.append(ls[0])
dp.append(ls[0] + ls[1])
dp.append(max(ls[0] + ls[1], ls[0] + ls[2], ls[1] + ls[2]))

for i in range(3, n):
    dp.append(max(dp[i - 1], dp[i - 2] + ls[i], dp[i - 3] + ls[i - 1] + ls[i]))

print(max(dp))