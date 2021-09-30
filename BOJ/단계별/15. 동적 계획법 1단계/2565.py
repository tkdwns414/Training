import sys

n = int(sys.stdin.readline())

ls = []

for i in range(n):
    ls.append(list(map(int, sys.stdin.readline().split())))

ls.sort(key=lambda x: x[0])
new_ls = [ls[i][1] for i in range(n)]

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if new_ls[i] > new_ls[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
# 한 전봇대를 기준으로 번호 순서대로 정렬할 경우
# 반대 전봇대에서 가장 긴 증가하는 수열을 계산해서 뺴준다