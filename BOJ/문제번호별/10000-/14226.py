import sys
from collections import deque

s = int(sys.stdin.readline())
dp = [[-1 for _ in range(s + 1)] for __ in range(s + 1)]
# dp[i][j] => 화면에 i+1개 클립보드에 j+1개일 때 최소 시간
dp[1][0] = 0

queue = deque()
queue.append((1, 0))

while queue:
    i, j = queue.popleft()
    if i == s:
        print(dp[i][j])
        break
    for x, y in zip([i, i + j, i - 1], [i, j, j]):
        if 0 < x <= s and dp[x][y] == -1:
            dp[x][y] = dp[i][j] + 1
            queue.append((x, y))
"""
이모티콘 한개 입력
1) 화면 내 모든 이모티콘 복사
2) 복사된 모든 이모티콘을 붙여넣기
3) 화면에 있는 이모티콘 중 하나 삭제
다이나믹 프로그래밍 냄새가 난다
1697번 문제랑 비슷한듯, 그런데 클립보드가 따로 있어서 조금 다르게
"""