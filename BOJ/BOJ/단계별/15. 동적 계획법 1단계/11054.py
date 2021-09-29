import sys

n = int(sys.stdin.readline())

ls = list(map(int, sys.stdin.readline().split()))

dp = [[1, 1] for _ in range(n)]  # 증가하는 수열, 내려오는 수열 저장

for i in range(1, n):
    for j in range(i):
        if ls[i] > ls[j]:  # 증가만 하는 수열
            dp[i][0] = max(dp[j][0] + 1, dp[i][0])
        elif ls[i] < ls[j]:
            dp[i][1] = max(dp[j][0] + 1, dp[j][1] + 1, dp[i][1])

print(max(map(max, dp)))

# 가장 긴 바이토닉 수열을 만들기 위해서는 어떻게 해야할까?
# 내려올 때는 쭉 내려오기만 해야하므로 따로 저장해주기