import sys

sys.setrecursionlimit(10000)


def solve(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    else:
        if graph[x][y] == 1 and visited[x][y] == 0:
            visited[x][y] = 1
            solve(x - 1, y)
            solve(x + 1, y)
            solve(x, y - 1)
            solve(x, y + 1)


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