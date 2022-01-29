import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
quests = list(list(map(int, sys.stdin.readline().split())) for _ in range(M))

dp = [[0 for _ in range(N)] for __ in range(N)]  # dp[i][j]는 i~j가 펜릴드롬인지 아닌지 의미

for nums_len in range(N):  # 확인할 길이
    for start in range(N - nums_len):  # 시작점
        end = start + nums_len  # 끝점
        if start == end:  # 길이가 1인 수열은 무조건 펜릴드롬
            dp[start][end] = 1
        elif nums[start] == nums[end]:
            if start + 1 == end:  # 마지막 대칭이 같은데 길이가 2인 수열은 무조건 펜릴드롬
                dp[start][end] = 1
            elif dp[start + 1][end - 1] == 1:  # 마지막 대칭이 같은데 그 내부가 펜릴드롬인 수열은 무조건 펜릴드롬
                dp[start][end] = 1

for quest in quests:
    print(dp[quest[0] - 1][quest[1] - 1])
