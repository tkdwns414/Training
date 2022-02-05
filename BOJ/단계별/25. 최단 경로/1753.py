import sys
import heapq  # 우선순위 큐(힙의 형태)

V, E = map(int, sys.stdin.readline().split())
S = int(sys.stdin.readline())
edge = [[] for _ in range(V)]
res = [int(1e9)] * V  # res[i] = S-1노드(시작점) ~ i노드까지의 거리

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edge[u - 1].append((v - 1, w))  # 방향 그래프이므로 양쪽 추가 아님

heap = []
heapq.heappush(heap, (0, S - 1))  # 시작점~시작점 거리는 0, 시작점은 S-1(인덱스)
res[S - 1] = 0  # 시작점~시작점 거리 = 0

while heap:
    dist, node = heapq.heappop(heap)  # dist = 시작점~node(현재 노드) 까지의 거리
    if dist > res[node]:
        continue  # dist가 res에 있는 값보다 크면 작업할 필요 없음
    for next_n in edge[node]:
        cost = dist + next_n[1]  # dist + node~next_n[0]까지의 거리
        if cost < res[next_n[0]]:
            res[next_n[0]] = cost
            heapq.heappush(heap, (cost, next_n[0]))  # 거리 순으로 다시 정렬

for r in res:
    print(r if r != int(1e9) else "INF")


"""
우선순위 큐를 사용하지 않고 할 경우 틀림(거리 기준 정렬이 꼭 필요함)
import sys
from collections import deque

V, E = map(int, sys.stdin.readline().split())
S = int(sys.stdin.readline())
edge = [[] for _ in range(V)]
res = [-1] * V

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edge[u - 1].append((v - 1, w))  # 방향그래프이므로 얘만

queue = deque([S - 1])
res[S - 1] = 0  # 자기 자신까지의 거리

while queue:
    cur = queue.popleft()  # 현재 노드
    for info in edge[cur]:
        node = info[0]  # 다음 노드
        val = info[1]
        if res[node] == -1:  # 처음 방문한 곳이면
            res[node] = res[cur] + val  # 시작점부터 현재노드까지 거리 + 현재노드~다음노드 비용
            queue.append(node)
        else:
            res[node] = min(res[node], res[cur] + val)

for r in res:
    print(r if r != -1 else "INF")
"""