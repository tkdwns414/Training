import sys

n = int(sys.stdin.readline())
ls = []

for i in range(n):
    ls.append(list(map(int, sys.stdin.readline().split())))

# 위에서 두번쨰 줄부터 시작해서
# 1)맨 왼쪽은 윗층 맨 왼쪽
# 2)맨 오른쪽은 윗층 맨 오른쪽
# 3)둘 다 해당 안되면  윗층 양 옆 중 큰 숫자 더하기

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            ls[i][j] += ls[i - 1][0]
        elif j == i:
            ls[i][j] += ls[i - 1][j - 1]
        else:
            ls[i][j] += max(ls[i - 1][j], ls[i - 1][j - 1])

print(max(ls[n - 1]))