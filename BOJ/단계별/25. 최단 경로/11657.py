import sys

N, M = map(int, sys.stdin.readline().split())

road = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    road.append((A - 1, B - 1, C))

res = [int(1e9) for _ in range(N)]
temp = [0 for _ in range(N)]
res[0] = 0
cycle = False

for i in range(N):
    for j in range(M):
        c, n, d = road[j]
        if res[c] != int(1e9) and res[n] > res[c] + d:
            res[n] = res[c] + d
            if i == N - 1:
                cycle = True

if cycle:
    print(-1)
else:
    for i in range(1, N):
        print(res[i] if res[i] != int(1e9) else -1)
# 단계별에 벨만 포드 알고리즘을 배우는 문제라 돼 있음
# 다익스트라를 이용하면 while문에서 값을 비교할 때 반복할수록 더 작아지기 때문에 빠져나오지 못하고 무한 반복함
# 예전에 학교에서 배운 벨만 포드 알고리즘 적용했음 -> 왜 틀렸는지는 블로그에 작성할 때 볼 예정
"""
cycle = False

for i in range(N):
    for j in range(M):
        temp = res.copy()
        a, b, c = road[j]
        temp_ = res[b]
        res[b] = min(temp[b], temp[a] + c)
        if i == N - 1:
            if res[b] != temp_:
                cycle = True

if cycle:
    print(-1)
else:
    for i in range(1, N):
        print(res[i] if res[i] != int(1e9) else -1)
"""