import sys

T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    ls = [0] + list(map(int, sys.stdin.readline().split()))

    acc_sum = [0 for i in range(K + 1)]
    for i in range(1, K + 1):
        acc_sum[i] = acc_sum[i - 1] + ls[i]

    dp = [[0 for _ in range(K + 1)] for __ in range(K + 1)]
    # dp[i][j]는 i번째 숫자부터 j번째 숫자까지의 최소합(1번쨰 숫자부터 시작)
    for i in range(2, K + 1):  # 길이
        for j in range(1, K + 2 - i):  # 시작점
            end = j + i - 1  # 끝점
            dp[j][end] = min(dp[j][j + x] + dp[j + x + 1][end] for x in range(i - 1))
            # ^ 마지막 합치기 전 최소 비용
            dp[j][end] += acc_sum[end] - acc_sum[j - 1]  # 마지막 합칠 때 비용

    print(dp[1][K])  # 1번째 수부터 K번쨰 수까지의 최소 비용


# a번째 수부터 b 번째 수까지의 최소 비용은
# {(a번째 수부터 a+x번째 수까지의 최소 비용 + a+x번째 수부터 b번째 수까지의 최소비용) 중 최솟값} + [a번째 수부터 a+x번째 수까지의 누적합]
# 즉 (마지막 합치기 전 두개를 만들기까지의 최소 비용} + [마지막 그 두개를 합칠 때의 조합 비용(누적합으로 고정)]
# 시간초과 나서 Pypy3로 제출