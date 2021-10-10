import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(1, n + 1):
    queue.append(i)

throw = True
while len(queue) != 1:
    if throw:
        queue.popleft()
        throw = False
    else:
        queue.append(queue.popleft())
        throw = True

print(queue[0])