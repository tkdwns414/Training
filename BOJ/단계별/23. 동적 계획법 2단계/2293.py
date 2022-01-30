import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
dp = [0 for _ in range(k + 1)]  # dp[i] => i원을 만들 수 있는 경우의 수
dp[0] = 1  # 0원을 만들 수 있는 경우의 수는 0개

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

for coin in coins:
    for cost in range(1, k + 1):
        if cost - coin >= 0:
            dp[cost] += dp[cost - coin]

print(dp[k])
# 더 이상 사용되지 않는 값을 버림으로써 공간 복잡도를 향상시키는 문제. 메모리 제한에 주목하세요.
