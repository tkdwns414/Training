import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x > 0:
        heapq.heappush(heap, (-x, x))
    elif x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

# 파이썬에서 힙의 구현은 heapq를 이용
# 기본적으로 heapq.heappush는 최소힙을 만듦
# 최대 힙을 만들기 위해서는 튜플을 이용해 역순으로 정렬되게 해주기
# 튜플을 이용하지 않더라도 힙에 넣을 때 음수 값을 입력하고 힙에서 뺄 때 -를 붙여도 됨