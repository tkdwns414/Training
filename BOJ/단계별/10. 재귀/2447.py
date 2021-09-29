def rect_star(x, y, n, ls):
    if n == 3:
        ls[x + 1][y + 1] = " "
    else:
        temp = n // 3
        for i in range(x + temp, x + 2 * temp):
            for j in range(y + temp, y + 2 * temp):
                ls[i][j] = " "
        for i in range(0, n, temp):
            for j in range(0, n, temp):
                rect_star(x + i, y + j, temp, ls)


n = int(input())
ls = [["*" for i in range(n)] for i in range(n)]

rect_star(0, 0, n, ls)
for i in range(0, n):
    for j in range(0, n):
        print(ls[i][j], end="")
    print()

# n은 3의 거듭제곱
# 중심을 계산 공백 넣기
# x,y로 현재 위치를 잡아서 그 위치 기준 중심 넣기
