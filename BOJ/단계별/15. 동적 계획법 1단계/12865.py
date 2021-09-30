import sys

n, k = map(int, sys.stdin.readline().split())
ls = []

for _ in range(n):
    ls.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(k + 1)] for __ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= ls[i - 1][0]:  # 현재 물건의 무게를 수용 가능 하다면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - ls[i - 1][0]] + ls[i - 1][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(max(dp[-1]))