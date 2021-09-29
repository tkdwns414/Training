import sys
from collections import deque


def solve(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()
        if a < 0 or a >= n or b < 0 or b >= m:
            continue
        else:
            if graph[a][b] == 1 and visited[a][b] == 0:
                visited[a][b] = 1
                for i, j in zip(dx, dy):
                    queue.append((a + i, b + j))


t = int(sys.stdin.readline())

for test in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for __ in range(n)]
    visited = [[0 for _ in range(m)] for __ in range(n)]
    count = 0

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                solve(i, j)
                count += 1
    print(count)