import sys

a, x = map(int, sys.stdin.readline().split())
ls = sys.stdin.readline().split()

for item in ls:
    if int(item) < x:
        print(item, end=" ")
