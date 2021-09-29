import sys

n = int(sys.stdin.readline())
papers = []
blue = 0
white = 0

for _ in range(n):  # 0은 하양 1은 파랑
    papers.append(list(map(int, sys.stdin.readline().split(" "))))


def solve(x, y, n):
    global white, blue
    all_same = True
    check = papers[x][y]

    for i in range(n):
        for j in range(n):
            if check != papers[x + i][y + j]:
                all_same = False

    if all_same:
        if check == 1:
            blue += 1
        elif check == 0:
            white += 1
    else:
        temp = n // 2
        solve(x, y, temp)
        solve(x + temp, y, temp)
        solve(x, y + temp, temp)
        solve(x + temp, y + temp, temp)


solve(0, 0, n)
print(white)
print(blue)