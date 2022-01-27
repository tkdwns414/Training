import sys


N = int(sys.stdin.readline())
ls = []

for _ in range(N):
    ls.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(N)] for __ in range(N)]

for i in range(1, N):
    for j in range(N - i):
        end = i + j
        dp[j][end] = 2 ** 32 - 1
        for k in range(j, end):
            dp[j][end] = min(  # dp[j][end]는 i부터 j까지의 최솟값
                dp[j][end], dp[j][k] + dp[k + 1][end] + ls[j][0] * ls[k][1] * ls[end][1]
            )  # (지금까지의 조합값 + 이번 조합값 들 중 최솟값)

print(dp[0][N - 1])

# i는 시작점, 끝점 차이
# j는 시작점, end는 끝점, k는 j와 end 사이의 수들
# 시간초과 Pypy3로 제출
