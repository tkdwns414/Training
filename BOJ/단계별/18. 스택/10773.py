import sys
from collections import deque

k = int(sys.stdin.readline())
my_stk = deque()

for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        my_stk.pop()
    else:
        my_stk.append(n)

print(sum(my_stk))
