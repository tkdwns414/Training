import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

tomato = []
for i in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split(" "))))

queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))

count = -1

while queue:
    x, y = queue.popleft()
    for i, j in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        if 0 <= x + i < n and 0 <= y + j < m and tomato[x + i][y + j] == 0:
            tomato[x + i][y + j] = tomato[x][y] + 1
            queue.append((x + i, y + j))

result = 0
zero = False
for to in tomato:
    if 0 in to:
        zero = True
        break
    result = max(result, max(to))

if zero:
    print(-1)
else:
    print(result - 1)
