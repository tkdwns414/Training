import sys

n = int(sys.stdin.readline())
ls = []
for i in range(n):
    ls.append(sys.stdin.readline())

for line in ls:
    total = 0
    check = 0
    for k in line:
        if k == "O":
            check += 1
            total += check
        elif k == "X":
            check = 0
    print(total)
