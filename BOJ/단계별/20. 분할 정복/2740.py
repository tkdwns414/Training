import sys

n, m = map(int, sys.stdin.readline().split())
A = []
B = []
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

m, k = map(int, sys.stdin.readline().split())
for _ in range(m):
    B.append(list(map(int, sys.stdin.readline().split())))

result = [[0 for _ in range(k)] for __ in range(n)]

for x in range(n):
    for y in range(k):
        for z in range(m):
            result[x][y] += A[x][z] * B[z][y]

for nums in result:
    print(" ".join(map(str, nums)))

# 행렬곱 계산 방법 까먹은게 좀...
