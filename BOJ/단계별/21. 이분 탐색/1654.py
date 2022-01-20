import sys

k, n = map(int, sys.stdin.readline().split())
cables = []
for _ in range(k):
    cables.append(int(sys.stdin.readline()))

s, e = 1, max(cables)

while s <= e:
    m = (s + e) // 2
    lines = 0
    for cable in cables:
        lines += cable // m

    if lines >= n:  # 필요한 랜선의 수보다 더 많이 나온다면 길이가 더 길어도 된다
        s = m + 1
    else:  # 필요한 랜선의 수보다 더 적게 나온다면 길이가 더 짧아야 한다
        e = m - 1
print(e)