# 안정 정렬 (값이 같은 원소의 순서가 바뀌지 않는 정렬)
import sys

t = int(sys.stdin.readline())
ls = []
for i in range(t):
    ls.append(list(sys.stdin.readline().split()))

ls.sort(key=lambda x: int(x[0]))

for i in range(t):
    print(ls[i][0], ls[i][1])
