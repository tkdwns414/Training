import sys


def check(x, y):
    key = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):  # 가로세로 검사
        if game[x][i] in key:
            key.remove(game[x][i])
        if game[i][y] in key:
            key.remove(game[i][y])

    x1 = x // 3
    y1 = y // 3

    for i in range(x1 * 3, x1 * 3 + 3):  # 3곱3 검사
        for j in range(y1 * 3, y1 * 3 + 3):
            if game[i][j] in key:
                key.remove(game[i][j])

    return key


def solve(n, count):

    if n == count:
        for i in range(9):
            sys.stdout.write(" ".join(map(str, game[i])) + "\n")
        exit()

    i, j = tosolve[n]
    for item in check(i, j):
        game[i][j] = item
        solve(n + 1, count)
        game[i][j] = 0


game = []

for i in range(9):
    game.append(list(map(int, sys.stdin.readline().split())))

tosolve = [(i, j) for i in range(9) for j in range(9) if game[i][j] == 0]

solve(0, len(tosolve))
