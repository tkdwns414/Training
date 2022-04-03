import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    ins = list(sys.stdin.readline().split())
    if ins[0] == "push":
        queue.append(ins[1])
    elif ins[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif ins[0] == "size":
        print(len(queue))
    elif ins[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif ins[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif ins[0] == "back":
        if queue:
            print(queue[len(queue) - 1])
        else:
            print(-1)

# 18258이랑 차이가 뭐지?
