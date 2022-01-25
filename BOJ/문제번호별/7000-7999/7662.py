import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    heap_x = []
    heap_n = []
    available = [True] * K
    for i in range(K):
        oper = sys.stdin.readline().split()

        if oper[0] == "I":
            heapq.heappush(heap_n, (int(oper[1]), i))
            heapq.heappush(heap_x, (-int(oper[1]), i))
        else:
            if heap_n and oper[1] == "-1":
                available[heap_n[0][1]] = False
            elif heap_x and oper[1] == "1":
                available[heap_x[0][1]] = False
                heapq.heappop(heap_x)

            while heap_n and not available[heap_n[0][1]]:
                heapq.heappop(heap_n)
            while heap_x and not available[heap_x[0][1]]:
                heapq.heappop(heap_x)

    if heap_x and heap_n:
        print(-heap_x[0][0], heap_n[0][0])
    else:
        print("EMPTY")

"""
매번 heap에서 remove하고 그러는 것은 비효율적(시간초과)
처음에 기본적인 실수(T마다 heap들 초기화 안함)

import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    heap_x = []
    heap_n = []
    for __ in range(K):
        oper, n = sys.stdin.readline().split()
        if oper == "I":
            heapq.heappush(heap_n, int(n))
            heapq.heappush(heap_x, -int(n))
        elif oper == "D":
            if heap_x and heap_n:
                if n == "-1":
                    heap_x.remove(-heapq.heappop(heap_n))
                    heapq.heapify(heap_x)
                else:
                    heap_n.remove(-heapq.heappop(heap_x))
                    heapq.heapify(heap_n)

    if heap_x and heap_n:
        print(-heap_x[0], heap_n[0])
    else:
        print("EMPTY")
"""