import sys

a, b, c = map(int, sys.stdin.readline().split(" "))


def solve(a, b, c):
    if b == 1:
        return a % c
    else:
        temp = solve(a, b // 2, c)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c


print(solve(a, b, c))
# 시간 초과 -> 곱셈 연산 수를 줄이기
