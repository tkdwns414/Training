import sys

n = int(sys.stdin.readline())
papers = []

for _ in range(n):
    papers.append(sys.stdin.readline().rstrip())


def solve(x, y, n):
    all_same = True
    check = papers[x][y]

    for i in range(n):
        for j in range(n):
            if check != papers[x + i][y + j]:
                all_same = False

    if all_same:
        if check == "1":
            print(1, end="")
        elif check == "0":
            print(0, end="")
    else:
        print("(", end="")
        temp = n // 2
        solve(x, y, temp)
        solve(x, y + temp, temp)
        solve(x + temp, y, temp)
        solve(x + temp, y + temp, temp)
        print(")", end="")


solve(0, 0, n)