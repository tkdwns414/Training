import sys

first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()
l_f = len(first) + 1
l_s = len(second) + 1

dp = [[0 for _ in range(l_s)] for __ in range(l_f)]

for i in range(1, l_f):
    for j in range(1, l_s):
        if first[i - 1] == second[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max(dp[-1]))

# 점화식 잘 생각해보기