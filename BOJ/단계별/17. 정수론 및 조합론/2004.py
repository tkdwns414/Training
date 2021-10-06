import sys


def count_two(n):
    two = 0
    while n != 0:
        n //= 2
        two += n
    return two


def count_five(n):
    five = 0
    while n != 0:
        n //= 5
        five += n
    return five


n, m = map(int, sys.stdin.readline().split())

print(
    min(
        count_two(n) - count_two(n - m) - count_two(m),
        count_five(n) - count_five(n - m) - count_five(m),
    )
)

# 팩토리얼 0의 개수 코드보다 훨씬 좋은 코드인듯
