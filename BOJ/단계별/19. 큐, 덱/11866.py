import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()

for i in range(1, n + 1):
    queue.append(i)

result = []
while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")

# 사실 큐 안 쓰고 그냥 계산해서 하는 것도 괜찮을지도..? 나머지 계산 이용
