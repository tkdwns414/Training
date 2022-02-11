import sys

V, E = map(int, sys.stdin.readline().split())
roads = []
dist = [[int(1e9) for i in range(V)] for j in range(V)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    dist[a - 1][b - 1] = c

for i in range(V):
    for j in range(V):
        for k in range(V):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

result = int(1e9)
for i in range(V):
    result = min(result, dist[i][i])  # 본인에서 본인으로 돌아오는 최소값으로 갱신
if result == int(1e9):
    print(-1)
else:
    print(result)

# pypy3로 제ㄹ
