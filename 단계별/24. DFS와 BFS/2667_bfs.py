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


def b_solve(x, y):
    global count
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()
        if not is_out(a, b):
            if graph[a][b] == "1" and visited[a][b] == 0:
                visited[a][b] = 1
                count += 1
                for i, j in zip(dx, dy):
                    queue.append((a + i, b + j))


for i in range(n):
    for j in range(n):
        if graph[i][j] == "1" and visited[i][j] == 0:
            b_solve(i, j)
            answer.append(count)
            count = 0

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)