import sys
import heapq


def dijkstra(s):
    heap = []
    heapq.heappush(heap, (0, s))
    res = [int(1e9) for _ in range(n)]
    res[s] = 0

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > res[node]:
            continue
        for next_n in road[node]:
            cost = dist + next_n[1]  # dist + node~next_n[0]까지의 거리
            if cost < res[next_n[0]]:
                res[next_n[0]] = cost
                heapq.heappush(heap, (cost, next_n[0]))  # 거리 순으로 다시 정렬

    return res


for T in range(int(sys.stdin.readline())):
    n, m, t = map(int, sys.stdin.readline().split())  # n은 노드, m은 선, t는 목적지 후보
    s, g, h = map(int, sys.stdin.readline().split())  # s는 시작점, g~h는 지나간 길
    prob = []  # 목적지 후보들
    road = [[] for _ in range(n)]  # 양방향 길

    for _ in range(m):  # 양방향 길 입력받기
        a, b, d = map(int, sys.stdin.readline().split())
        road[a - 1].append([b - 1, d])
        road[b - 1].append([a - 1, d])

    for _ in range(t):  # 목적지 후보들 입력받기
        x = int(sys.stdin.readline()) - 1
        prob.append(x)
    prob.sort()

    start = dijkstra(s - 1)  # s에서 다익스트라
    from_g = dijkstra(g - 1)  # g에서 다익스트라
    from_h = dijkstra(h - 1)  # h에서 다익스트라

    for p in prob:
        case_g = start[g - 1] + from_g[h - 1] + from_h[p]  # s - g - h - p
        case_h = start[h - 1] + from_h[g - 1] + from_g[p]  # s - h - g - p
        if start[p] == case_g or start[p] == case_h:
            print(p + 1, end=" ")

"""
(각 노드까지 최소 경로들을 같이 저장하고 g~h를 지나는지 확인)
틀렸는데 틀린 이유는 아마 최소 경로가 여러개일 때 g~h를 지나지 않는 상황이 저장될 수도 있어서
왜 틀렸는지는 정확히 모르지만 그냥 마지막 확인 조건이 너무 더러워서 위에 방법으로 바꿈
import sys
import heapq

for T in range(int(sys.stdin.readline())):
    n, m, t = map(int, sys.stdin.readline().split())  # n은 노드, m은 선, t는 목적지 후보
    s, g, h = map(int, sys.stdin.readline().split())  # s는 시작점, g~h는 지나간 길
    prob = []  # 목적지 후보들
    road = [[] for _ in range(n)]  # 양방향 길

    for _ in range(m):  # 양방향 길 입력받기
        a, b, d = map(int, sys.stdin.readline().split())
        road[a - 1].append([b - 1, d])
        road[b - 1].append([a - 1, d])

    for _ in range(t):  # 목적지 후보들 입력받기
        x = int(sys.stdin.readline()) - 1
        prob.append(x)
    prob.sort()

    heap = []
    heapq.heappush(heap, (0, s - 1))
    res = [[int(1e9), []] for _ in range(n)]
    res[s - 1][0] = 0

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > res[node][0]:
            continue
        for next_n in road[node]:
            cost = dist + next_n[1]  # dist + node~next_n[0]까지의 거리
            if cost < res[next_n[0]][0]:
                res[next_n[0]][0] = cost
                res[next_n[0]][1] = res[node][1] + [node]
                heapq.heappush(heap, (cost, next_n[0]))  # 거리 순으로 다시 정렬

    for p in prob:
        check = res[p][1]
        for i in range(len(check)):
            if (check[i] == g - 1 and check[i - 1] == h - 1) or (
                check[i] == h - 1 and check[i - 1] == g - 1
            ):
                print(p + 1, end=" ")
"""