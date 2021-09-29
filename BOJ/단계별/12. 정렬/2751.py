# 내장 함수 이용하는 문제
import sys

n = int(sys.stdin.readline())
ls = []

for i in range(n):
    ls.append(int(sys.stdin.readline()))

for item in sorted(ls):
    sys.stdout.write(str(item) + "\n")
