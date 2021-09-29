import sys


def solve(d, s, n, m):
    if d == m:
        print(" ".join(map(str, result)))
        return
    for i in range(s, n):
        if visited[i] == False:
            visited[i] = True
            result.append(i + 1)
            solve(d + 1, i, n, m)
            visited[i] = False
            result.pop()


n, m = map(int, sys.stdin.readline().split())

visited = [False] * n
result = []
solve(0, 0, n, m)
