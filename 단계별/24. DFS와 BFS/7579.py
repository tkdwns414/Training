import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

tomato = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        tomato[i].append(list(map(int, sys.stdin.readline().split(" "))))


queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append((i, j, k))

count = -1

while queue:
    x, y, z = queue.popleft()
    for i, j, k in zip([0, 0, 0, 0, 1, -1], [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0]):
        if (
            0 <= x + i < h
            and 0 <= y + j < n
            and 0 <= z + k < m
            and tomato[x + i][y + j][z + k] == 0
        ):
            tomato[x + i][y + j][z + k] = tomato[x][y][z] + 1
            queue.append((x + i, y + j, z + k))

result = 0
zero = False
for to in tomato:
    for t in to:
        if 0 in t:
            zero = True
            break
        result = max(result, max(t))

if zero:
    print(-1)
else:
    print(result - 1)