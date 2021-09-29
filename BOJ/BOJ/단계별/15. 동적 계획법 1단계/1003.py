import sys


def solve(n):
    zero = 1
    one = 0
    for i in range(n):
        temp = one
        one += zero
        zero = temp
    print(zero, one)


t = int(sys.stdin.readline())

for i in range(t):
    solve(int(sys.stdin.readline()))