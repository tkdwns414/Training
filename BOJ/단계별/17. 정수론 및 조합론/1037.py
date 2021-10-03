import sys

n = sys.stdin.readline()
ls = sorted(list(map(int, sys.stdin.readline().split())))

print(ls[0] * ls[-1])
