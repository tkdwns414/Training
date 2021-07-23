# 이웃한 집끼리 색깔이 같으면 안된다
# 각 집마다, 색깔마다 칠하는 비용이 다르다
import sys

n = int(sys.stdin.readline())

ls = []

# RGB 순서대로
for i in range(n):
    ls.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    ls[i][0] += min(ls[i - 1][1], ls[i - 1][2])  # i번째 집이 빨간색
    ls[i][1] += min(ls[i - 1][0], ls[i - 1][2])  # i번쨰 집이 초록색
    ls[i][2] += min(ls[i - 1][0], ls[i - 1][1])  # i번째 집이 파란색

print(min(ls[n - 1][0], ls[n - 1][1], ls[n - 1][2]))
