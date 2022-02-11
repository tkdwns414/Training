import sys
import heapq

for T in range(int(sys.stdin.readline())):
    N, M, K = map(int, sys.stdin.readline().split())
    airports = [[] for __ in range(N)]
    dp = [[int(1e9)] * N for j in range(M + 1)]
    # dp[cost][a] cost로 a까지 가는데 걸리는 최소 거리

    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        airports[u - 1].append((v - 1, c, d))  # 도착 공항, 돈, 시간

    heap = []
    heapq.heappush(heap, (0, 0, 0))  # 출발 공항, 돈, 시간
    while heap:
        ap, c, d = heapq.heappop(heap)
        if d > dp[c][ap]:
            continue
        for airport in airports[ap]:
            cost = airport[1] + c
            dist = airport[2] + d
            if cost <= M and dist <= dp[cost][airport[0]]:
                for i in range(cost, M + 1):
                    # 비용이 cost 보다 높아도 거리가 더 짧으면 그 비용으로도 똑같이 갈 수 있음
                    if dp[i][airport[0]] > cost:
                        dp[i][airport[0]] = dist
                    else:
                        break
                heapq.heappush(heap, (airport[0], cost, dist))

    print(dp[M][N - 1] if dp[M][N - 1] != int(1e9) else "Poor KCM")

# 시간 초과로 Pypy3로 제출
# 메모리 초과 / 아무래도 힙에 계속 추가해서 다 확인하는거다보니...
"""
for T in range(int(sys.stdin.readline())):
    N, M, K = map(int, sys.stdin.readline().split())
    airports = [[] for __ in range(N)]
    res = [[] for i in range(N)]

    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        airports[u - 1].append((v - 1, c, d))  # 도착 공항, 돈, 시간

    heap = []
    heapq.heappush(heap, (0, 0, 0))  # 출발 공항, 돈, 시간

    while heap:
        ap, c, d = heapq.heappop(heap)
        for airport in airports[ap]:
            cost = airport[1] + c
            dist = airport[2] + d
            res[airport[0]].append((cost, dist))
            heapq.heappush(heap, (airport[0], cost, dist))

    for r in sorted(res[N - 1]):
        if r[0] <= M:
            print(r[1])
            break
    else:
        print("Poor KCM")
"""