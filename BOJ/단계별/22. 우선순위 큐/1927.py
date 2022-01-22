import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x > 0:
        heapq.heappush(heap, x)
    elif x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

# 파이썬에서 힙의 구현은 heapq를 이용
# 기본적으로 heapq.heappush는 최소힙을 만듦