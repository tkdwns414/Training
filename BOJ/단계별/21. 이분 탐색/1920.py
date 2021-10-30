import sys

n = int(sys.stdin.readline())
num_ls = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check_ls = list(map(int, sys.stdin.readline().split()))
num_ls.sort()

for i in range(m):
    s = 0
    e = n - 1
    while True:
        m = (s + e) // 2
        if s > e:
            print(0)
            break
        if num_ls[m] == check_ls[i]:
            print(1)
            break
        elif num_ls[m] > check_ls[i]:
            e = m - 1
        elif num_ls[m] < check_ls[i]:
            s = m + 1

# 이분 탐색을 이용하여 풀기