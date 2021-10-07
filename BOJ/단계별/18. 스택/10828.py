import sys
from collections import deque

n = int(sys.stdin.readline())
my_stk = deque()

for _ in range(n):
    ins = list(sys.stdin.readline().split())
    if ins[0] == "push":
        my_stk.append(ins[1])
    elif ins[0] == "pop":
        if my_stk:
            print(my_stk.pop())
        else:
            print(-1)
    elif ins[0] == "size":
        print(len(my_stk))
    elif ins[0] == "empty":
        if my_stk:
            print(0)
        else:
            print(1)
    elif ins[0] == "top":
        if my_stk:
            print(my_stk[len(my_stk) - 1])
        else:
            print(-1)