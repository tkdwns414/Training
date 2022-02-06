import heapq
import sys

N, E = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edge[a - 1].append((b - 1, c))
    edge[b - 1].append((a - 1, c))

v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(start):
    res = [int(1e9)] * N
    res[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > res[node]:
            continue
        for next_n in edge[node]:
            cost = dist + next_n[1]
            if cost < res[next_n[0]]:
                res[next_n[0]] = cost
                heapq.heappush(heap, (cost, next_n[0]))
    return res


one = dijkstra(0)  # 정점 1에서 시작
V1 = dijkstra(v1 - 1)  # 정점 v1에서 시작
V2 = dijkstra(v2 - 1)  # 정점 v2에서 시작

res = min(one[v1 - 1] + V1[v2 - 1] + V2[N - 1], one[v2 - 1] + V2[v1 - 1] + V1[N - 1])
print(res if res < int(1e9) else -1)  # -1 출력 까먹어서 한번 틀림...

"""
해결법
1~v1까지의 최소 거리 + v1 ~ v2까지의 최소 거리 + v2~N까지 최소 거리 or
1~v2까지의 최소 거리 + v2 ~ v1까지의 최소 거리 + v1~N까지의 최소 거리
=> 1부터의 다익스트라, v1부터의 다익스트라, v2부터의 다익스트라 모두 구하기
"""