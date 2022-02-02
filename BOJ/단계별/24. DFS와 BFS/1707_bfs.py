import sys
from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 0  # 색이 없으면 일단 파랑으로 시작

    while queue:  # 여기서 v가 속한 그래프는 모두 색이 칠해짐
        n = queue.popleft()
        for j in edge[n]:
            if visited[j] == -1:  # 방문하지 않은 노드면 n과 색을 반대로 1 - 1 = 0 or 1 - 0 = 1
                visited[j] = 1 - visited[n]
                queue.append(j)  # 새로 칠한 노드도 검사하기 위해 queue에 삽입
            elif visited[j] == visited[n]:  # 방문한 노드인데 n과 같은 색이면 이분 그래프 불가
                return False
    return True


for _ in range(int(sys.stdin.readline())):
    V, E = map(int, sys.stdin.readline().split())
    edge = [[] for i in range(V)]
    visited = [-1 for i in range(V)]  # -1은 색 없음, 0은 파랑, 1은 빨강

    for i in range(E):
        a, b = map(int, sys.stdin.readline().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    result = 1
    for i in range(V):  # 모든 점 검사를 위해
        if visited[i] == -1:
            if not bfs(i):
                result = 0
                break

    print("YES" if result else "NO")

# 이분 그래프가 뭐인지 먼저 알아야 함
# 이분 그래프: 모든 꼭짓점을 빨강과 파란색으로 칠하되, 모든 변이 빨강과 파랑 꼭짓점을 포함할 수 있도록 색칠한 그래프
