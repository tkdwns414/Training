import sys


def matrix_cal(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000000007

    return result


def solve(num):
    for_pow = [[1, 1], [1, 0]]
    if num == 1:
        return for_pow
    else:
        temp = solve(num // 2)
        if num % 2 == 0:
            return matrix_cal(temp, temp)
        else:
            return matrix_cal(matrix_cal(temp, temp), for_pow)


n = int(sys.stdin.readline())
print(solve(n)[1][0])

# 해당 문제는 찾아보지 않고 못 풀음...
# 피보나치를 행렬곱을 이용해서 푸는 문제
# https://st-lab.tistory.com/252
# 마지막 [[1],[0]] 연산은 구현 중 오류가 나서 그냥 연산된 결과 출력함