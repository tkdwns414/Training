import sys

n = int(sys.stdin.readline())
papers = []
minus = 0
zero = 0
plus = 0

for _ in range(n):
    papers.append(list(map(int, sys.stdin.readline().split(" "))))


def solve(x, y, n):
    global minus, zero, plus
    all_same = True
    check = papers[x][y]

    for i in range(n):
        for j in range(n):
            if check != papers[x + i][y + j]:
                all_same = False

    if all_same:
        if check == -1:
            minus += 1
        elif check == 0:
            zero += 1
        elif check == 1:
            plus += 1
    else:  # 반복문 귀찮음
        temp = n // 3
        solve(x, y, temp)
        solve(x, y + temp, temp)
        solve(x, y + 2 * temp, temp)
        solve(x + temp, y, temp)
        solve(x + temp, y + temp, temp)
        solve(x + temp, y + 2 * temp, temp)
        solve(x + 2 * temp, y, temp)
        solve(x + 2 * temp, y + temp, temp)
        solve(x + 2 * temp, y + 2 * temp, temp)


solve(0, 0, n)
print(minus)
print(zero)
print(plus)