import sys

n = int(sys.stdin.readline())
v = int(sys.stdin.readline())

edge = [[] for i in range(n)]

for i in range(v):
    a, b = map(int, sys.stdin.readline().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

for e in edge:
    e.sort()


def solve():
    stk = [0]
    visited = [0 for i in range(n)]
    path = []

    while stk:
        v = stk.pop()
        if visited[v] == 0:
            visited[v] = 1
            path.append(v)
            stk += edge[v]
    return len(path) - 1


print(solve())