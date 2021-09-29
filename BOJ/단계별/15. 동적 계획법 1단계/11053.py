import sys

n = int(sys.stdin.readline())

ls = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if ls[i] > ls[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))

# 가장 긴 증가하는 수열을 만들기 위해서는 어떻게 해야할까?
# 어떤 수 a가 마지막으로 오는 수열의 길이 최댓값은 a보다 작고 먼저 나와있는 수 중 길이 최댓값 +1이다.