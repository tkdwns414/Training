import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

tomato = []
for i in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split(" "))))
