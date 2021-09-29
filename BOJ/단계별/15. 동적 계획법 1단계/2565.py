import sys


def overlap(a, b):
    if (a[0] > b[0] and a[1] > b[1]) or (a[0] < b[0] and a[1] < b[1]):
        return False
    else:
        return True


n = int(sys.stdin.readline())

ls = []

for i in range(n):
    ls.append(list(map(int, sys.stdin.readline().split())))

dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if overlap(ls[i], ls[j]):
            dp[i] += 1

print(ls)
print(dp)

# 가장 겹치지 않게 만들고
# 없앤 줄의 개수 출력
# dp[i][0] 에는 i번째 줄을 없앴을 때 안 겹치는 애들 저장,
# dp[i][1] 에는 지금까지 몇개의 줄을 없앴는지 저장
# 많이 겹치는 애들을 없애면 되지 않을까?