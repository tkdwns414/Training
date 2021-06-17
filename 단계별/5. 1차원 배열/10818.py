import sys

n = sys.stdin.readline()

ls = list(map(int, sys.stdin.readline().split()))
print(min(ls), max(ls))
