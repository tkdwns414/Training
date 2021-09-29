import sys


def solve(d, n, m):
    if d == m:
        print(" ".join(map(str, result)))
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result.append(i + 1)
            solve(d + 1, n, m)
            visited[i] = False
            result.pop()


n, m = map(int, sys.stdin.readline().split())

visited = [False] * n
result = []
solve(0, n, m)
