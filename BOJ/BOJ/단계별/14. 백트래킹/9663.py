# 퀸을 놓으려면 놓으려는 자리에 가로,세로, 대각선에 다른 퀸이 없는지 확인해야함
import sys

count = 0


def check(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[x] - visited[i]) == x - i:
            return False
    return True


def queen(x, n):
    global count
    if x == n:
        count += 1
    else:
        for i in range(n):
            visited[x] = i
            if check(x):
                queen(x + 1, n)


n = int(sys.stdin.readline())
visited = [0] * n
queen(0, n)
print(count)