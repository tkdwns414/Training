import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(sys.stdin.readline().rstrip())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()
queue.append([0, 0, 0])
visited = [[[0, 0] for _ in range(m)] for __ in range(n)]
# visited[i][j][k]: i,j 자리에 k = 0(벽을 부시지 않았을 때) k = 1(벽을 부셨을 때) 최단거리
visited[0][0][0] = 1

while queue:
    x, y, is_crashed = queue.popleft()
    if x == n - 1 and y == m - 1:  # 목적지에 도착하는 순간 끝
        print(visited[x][y][is_crashed])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == "0" and visited[nx][ny][is_crashed] == 0:
                # 벽을 부시지 않고 이동 / 해당 구역이 길이고 현재 상태(벽을 부셨는지 아닌지)에 맞게 visited 에 추가
                queue.append([nx, ny, is_crashed])
                visited[nx][ny][is_crashed] += visited[x][y][is_crashed] + 1
            if graph[nx][ny] == "1" and is_crashed == 0:  # 벽을 부시고 이동
                # 해당 구역이 벽이고 지금까지 벽을 부신 적 없으면 이번에 벽을 부순다
                queue.append([nx, ny, is_crashed + 1])
                visited[nx][ny][is_crashed + 1] += visited[x][y][is_crashed] + 1
else:  # while문이 break로 끝나지 않으면
    print(-1)

# 시간 초과라 Pypy3로 제출
