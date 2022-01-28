import sys

sys.setrecursionlimit(10 ** 8)

M, N = map(int, sys.stdin.readline().split())
road = []
for i in range(M):
    road.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dp = [[-1 for _ in range(N)] for __ in range(M)]
# dp[i][j]는 그 위치에서 도착점까지 갈 수 있는 경우의 수 / -1은 아직 사용하지 않았음을 의미


def solve_dfs(x, y):
    if x == M - 1 and y == N - 1:  # 도착점에 도착했으면 방법 하나를 찾은 것이므로 1을 더해준다.
        return 1
    if dp[x][y] != -1:  # dp의 값이 -1이 아니라면 이 길을 이미 사용한 것이므로 그 값을 반환한다.
        return dp[x][y]
    dp[x][y] = 0  # 아직 사용하지 않은 길이고(== -1)반환하기 전에 더해줄 것이기 때문에 값을 일단 0으로 해준다
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if 0 <= cx < M and 0 <= cy < N:
            if road[cx][cy] < road[x][y]:
                dp[x][y] += solve_dfs(cx, cy)  # 아직 사용하지 않은 길에 도착점까지 가는 방법이 몇개인지 더하기

    return dp[x][y]


print(solve_dfs(0, 0))
# 어떻게 해야하는지 감이 안와서 알고리즘 열어봤더니 dfs
# recursionerror 걸려서 재귀 제한 올려줌