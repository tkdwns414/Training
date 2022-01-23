import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(heap, (abs(x), x)) if x else print(
        heapq.heappop(heap)[1] if heap else 0
    )


"""
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        print(heapq.heappop(heap)[1] if heap else 0)
"""