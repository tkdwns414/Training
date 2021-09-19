import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(n)] for __ in range(n)]
visited_DFS = deque([0 for i in range(n)])
visited_BFS = deque([0 for i in range(n)])
DFS_root = deque()
BFS_root = deque()
BFS_queue = deque()

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1


def DFS(graph, visited, root, v):
    visited[v] = 1
    root.append(v + 1)
    print(v + 1, end=" ")
    for i in range(len(graph)):
        if graph[v][i] == 1 and visited[i] == 0:
            DFS(graph, visited, root, i)
    return root


def BFS(graph, visited, root, queue, v):
    visited[v] = 1
    root.append(v + 1)
    print(v + 1, end=" ")
    queue.append(v)

    while queue:
        nextv = queue.popleft()

        for i in range(len(graph)):
            if graph[nextv][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                root.append(i + 1)
                print(i + 1, end=" ")
    return root


DFS(graph, visited_DFS, DFS_root, v - 1)
print()
BFS(graph, visited_BFS, BFS_root, BFS_queue, v - 1)
