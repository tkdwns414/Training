import sys
from collections import deque

n = int(sys.stdin.readline())
my_deque = deque()

for _ in range(n):
    ins = list(sys.stdin.readline().split())
    if ins[0] == "push_front":
        my_deque.appendleft(ins[1])
    elif ins[0] == "push_back":
        my_deque.append(ins[1])
    elif ins[0] == "pop_front":
        if my_deque:
            print(my_deque.popleft())
        else:
            print(-1)
    elif ins[0] == "pop_back":
        if my_deque:
            print(my_deque.pop())
        else:
            print(-1)
    elif ins[0] == "size":
        print(len(my_deque))
    elif ins[0] == "empty":
        if my_deque:
            print(0)
        else:
            print(1)
    elif ins[0] == "front":
        if my_deque:
            print(my_deque[0])
        else:
            print(-1)
    elif ins[0] == "back":
        if my_deque:
            print(my_deque[len(my_deque) - 1])
        else:
            print(-1)