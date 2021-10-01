import sys

n = int(sys.stdin.readline())

ls = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]
dp[0] = ls[0]

for i in range(1, n):
    if dp[i - 1] + ls[i] > ls[i]:
        dp[i] = dp[i - 1] + ls[i]
    else:
        dp[i] = ls[i]

print(max(dp))