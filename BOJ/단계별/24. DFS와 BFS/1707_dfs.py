import sys

sys.setrecursionlimit(100000)  # RecursionError 방지(1만으로 했는데도 떠서 10만으로)


def dfs(v, color):
    visited[v] = color  # color로 색 지정
    for n in edge[v]:
        if visited[n] == -1:  # 색이 칠해져있지 않다면
            dfs(n, 1 - color)  # v와 연결된 다른 노드들은 v와 다른 색(1-color)으로 칠하기


for _ in range(int(sys.stdin.readline())):
    V, E = map(int, sys.stdin.readline().split())
    edge = [[] for i in range(V)]
    visited = [-1 for i in range(V)]  # -1은 색 없음, 0은 파랑, 1은 빨강

    for i in range(E):
        a, b = map(int, sys.stdin.readline().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    for i in range(V):
        if visited[i] == -1:  # 색이 칠해져 있지 않다면
            dfs(i, 0)

    result = all(all(visited[i] == 1 - visited[j] for j in edge[i]) for i in range(V))
    # result = 이분 그래프의 조건을 만족하는지 / 각자 자기와 연결된 노드와 색깔이 모두 다른지 all()로 확인
    print("YES" if result else "NO")

# 이분 그래프가 뭐인지 먼저 알아야 함
# 이분 그래프: 모든 꼭짓점을 빨강과 파란색으로 칠하되, 모든 변이 빨강과 파랑 꼭짓점을 포함할 수 있도록 색칠한 그래프
