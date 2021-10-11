import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    queue = deque(map(int, sys.stdin.readline().split()))
    order = m  # 내가 관심 있는 종이의 현재 위치
    result = 0
    while queue:
        if queue[0] < max(queue):  # 중요도가 높은게 뒤에 있다면
            queue.append(queue.popleft())
            if order == 0:  # 내가 관심있는 종이가 후순위로 밀렸다면
                order = len(queue) - 1  # 위치 후순위로 재조정
            else:
                order -= 1
        else:  # 현재 출력 순서가 중요도가 제일 높은 거라면
            queue.popleft()
            result += 1
            if order == 0:  # 내가 관심 있는 종이라면
                break  #
            else:
                order -= 1

    print(result)