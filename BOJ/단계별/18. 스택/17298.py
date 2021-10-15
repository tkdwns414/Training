import sys
from collections import deque

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
stk = deque()
result = [-1 for _ in range(n)]

for i in range(n):
    while stk and (nums[stk[-1]] < nums[i]):
        result[stk.pop()] = nums[i]
    stk.append(i)

print(" ".join(map(str, result)))

# 그냥 for문으로 돌리면 시가초과 날 문제(골드에 문제 수준 보면 나옴)
# 스택에는 인덱스를 넣는다.
# 앞에서부터 순서대로 확인하는데 스택 가장 위에 있는 인덱스의 수가 현재 수보다 작으면
# result의 stk.pop()의 위치에 현재 숫자를 넣는다.
# i번째 인덱스의 오큰수도 구해야하니 앞의 결과와 관계 없이 stk에 자꾸 넣어준다.
