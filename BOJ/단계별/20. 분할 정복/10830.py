import sys


def matrix_cal(a, b):
    result = [[0 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= m

    return result


def solve(a, x):
    if x == 1:
        return a
    else:
        temp = solve(a, x // 2)
        if x % 2 == 0:
            return matrix_cal(temp, temp)
        else:
            return matrix_cal(matrix_cal(temp, temp), a)


n, b = map(int, sys.stdin.readline().split())
A = []
m = 1000

for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

for line in solve(A, b):
    for num in line:
        print(num % m, end=" ")
    print()

# n 제곱하라 해서 n번 연산하면 당연히 시간초과
# 자연수 n 제곱 문제처럼 최대한 나누어서 연산 횟수를 줄이기
# 마지막 출력에서 %m 을 하지 않았을 때 틀렸다고 나왔는데 아마 solve의 x==1 일 때 그냥 a를 반환해서 1000을 넘는 적이 있었나보다