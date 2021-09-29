import sys

n = int(sys.stdin.readline())

ls = [[0 for i in range(10)] for _ in range(n)]

for i in range(1, 10):
    ls[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0:
            ls[i][j] = ls[i - 1][j + 1]
        elif j == 9:
            ls[i][j] = ls[i - 1][j - 1]
        else:
            ls[i][j] = ls[i - 1][j - 1] + ls[i - 1][j + 1]

print(sum(ls[n - 1]) % 1000000000)

# 문제에서 중요한 것은 이전거에 나온 0이나 9의 개수
# 0이나 9가 마지막에 오는 애들은 각자 한개씩만 가능
# 그 외에는 이전 길이 자기 옆 수들 만큼 합