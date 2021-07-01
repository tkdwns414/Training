# 시간초과 아직 해결 못함
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

    for i in range(3):  # 3곱3 검사
        for j in range(3):
            if game[x1 * 3 + i][y1 * 3 + j] in key:
                key.remove(game[x1 * 3 + i][y1 * 3 + j])

    return key


def solve(n, count):

    if n == count:
        for i in range(9):
            sys.stdout.write(" ".join(map(str, game[i])) + "\n")
        exit()

    for i in range(9):
        for j in range(9):
            if game[i][j] == 0:
                for item in check(i, j):
                    game[i][j] = item
                    solve(n + 1, count)
                    game[i][j] = 0


game = []

for i in range(9):
    game.append(list(map(int, sys.stdin.readline().split())))

count = 0
for col in game:
    count += col.count(0)

solve(0, count)
