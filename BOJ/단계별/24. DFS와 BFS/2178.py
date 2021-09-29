import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(sys.stdin.readline().rstrip())

visited = [[0 for _ in range(m)] for __ in range(n)]
visited[0][0] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()
queue.append((0, 0))
count = 0

while queue:
    x, y = queue.popleft()
    if graph[x][y] == "1":
        for i, j in zip(dx, dy):
            if (
                not (x + i < 0 or x + i >= n or y + j < 0 or y + j >= m)
                and visited[x + i][y + j] == 0
            ):
                visited[x + i][y + j] = visited[x][y] + 1
                queue.append((x + i, y + j))

print(visited[n - 1][m - 1])
# 사실 x,y가 우리가 아는 x,y가 아니긴 한데...
