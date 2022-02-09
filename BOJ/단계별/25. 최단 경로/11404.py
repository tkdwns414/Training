import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
buses = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    buses.append((a - 1, b - 1, c))

dist = [[0 if i == j else int(1e9) for i in range(n)] for j in range(n)]

for bus in buses:
    dist[bus[0]][bus[1]] = min(dist[bus[0]][bus[1]], bus[2])

for i in range(n):  # i를 중간노드로 하여 검사하기
    for j in range(n):
        for k in range(n):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

for i in range(n):
    for j in range(n):
        print(dist[i][j] if dist[i][j] != (1e9) else 0, end=" ")
    print()

# 단계별에 플로이드 와셜 알고리즘을 배우는 문제라고 돼있음
