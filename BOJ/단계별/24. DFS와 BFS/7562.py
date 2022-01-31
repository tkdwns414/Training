import sys
from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]  # 나이트 이동 경로 맞추어서 dx, dy 모두 준비
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(int(sys.stdin.readline())):
    l = int(sys.stdin.readline())  # 판 크기 l X l
    sx, sy = map(int, sys.stdin.readline().split())  # 시작점
    fx, fy = map(int, sys.stdin.readline().split())  # 도착점
    visited = [[0 for i in range(l)] for j in range(l)]
    # visited[i][j] = i,j 위치까지 도달하는데의 최소 이동 횟수 + 1
    queue = deque()
    queue.append([sx, sy])
    visited[sx][sy] = 1

    while queue:
        x, y = queue.popleft()
        if x == fx and y == fy:
            break  # 최단 경로 완료
        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < l and 0 <= ty < l and visited[tx][ty] == 0:
                queue.append([tx, ty])
                visited[tx][ty] = visited[x][y] + 1
    print(visited[fx][fy] - 1)
