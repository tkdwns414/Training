import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

dis = [-1 for _ in range(k + 1)]
dis[n] = 0

queue = deque()
queue.append(n)

while queue:
    s = queue.popleft()
    for next_s in [s - 1, s + 1, 2 * s]:
        if 0 <= next_s <= k and dis[next_s] == -1:
            dis[next_s] = dis[s] + 1
            queue.append(next_s)

print(dis[k])
