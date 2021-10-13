import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
solve = deque(i for i in range(1, n + 1))
to_find = list(map(int, sys.stdin.readline().split()))
result = 0
while to_find:
    location = solve.index(to_find[0])
    cur_len = len(solve)

    if location <= cur_len // 2:  # 오른쪽
        solve.rotate(-location)
        result += location
        solve.popleft()
        to_find.remove(to_find[0])
    else:
        solve.rotate(cur_len - location)
        result += cur_len - location
        solve.popleft()
        to_find.remove(to_find[0])

print(result)