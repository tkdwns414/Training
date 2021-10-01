import sys

n = int(sys.stdin.readline())
ls = []

for _ in range(n):
    ls.append(list(map(int, sys.stdin.readline().split())))

ls.sort(key=lambda x: (x[1], x[0]))
# 끝나는 시간이 앞인 순서대로 -> 시작하는 시간이 앞인 순서대로
count = 0
temp = 0

for conf in ls:
    if conf[0] >= temp:
        temp = conf[1]
        count += 1

print(count)

# 회의 시작 시간을 기준으로 회의 개수를 결정하는 이유는 3,3 같은 것을 골라내기 위해
# 테스트 케이스 : 4
# 5
# 1 3
# 2 3
# 1 2
# 3 3
# 3 4