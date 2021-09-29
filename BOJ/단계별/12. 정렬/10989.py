# 카운팅 정렬 사용하기 > 이게 맞나?
import sys

n = int(sys.stdin.readline())
ls = [0 for _ in range(10001)]

for i in range(n):
    temp = int(sys.stdin.readline())
    ls[temp] += 1

for i in range(1, 10001):
    if ls[i]:
        while ls[i] > 0:
            print(i)
            ls[i] -= 1
