import sys

n = int(sys.stdin.readline())
ls = [0 for _ in range(300)]
dp = []
for i in range(n):
    ls[i] = int(sys.stdin.readline())

dp.append(ls[0])
dp.append(ls[0] + ls[1])
dp.append(max(ls[0] + ls[2], ls[1] + ls[2]))

for i in range(3, n):
    dp.append(max(dp[i - 2] + ls[i], dp[i - 3] + ls[i - 1] + ls[i]))

print(dp[n - 1])
# 맨 뒤 계단은 무조건 밟아야 한다
# 뒤에서부터 생각해봤을 때 내가 이 층 바로 전 층을 밟았다면 그 이전은 2개 전 층이다
# 계단이 3개 이하인 것도 생각하기
