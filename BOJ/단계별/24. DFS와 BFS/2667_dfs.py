import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []
visited = [[0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    graph.append(sys.stdin.readline())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = []
count = 0


def is_out(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    else:
        return False


def d_solve(x, y):
    global count
    if not is_out(x, y):
        if graph[x][y] == "1" and visited[x][y] == 0:
            visited[x][y] = 1
            count += 1
            for a, b in zip(dx, dy):
                d_solve(x + a, y + b)


for i in range(n):
    for j in range(n):
        if graph[i][j] == "1" and visited[i][j] == 0:
            d_solve(i, j)
            answer.append(count)
            count = 0

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)