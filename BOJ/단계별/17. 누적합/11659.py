import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sums = [0 for _ in range(n + 1)]
sums[1] = nums[0]

for i in range(2, n + 1):
    sums[i] = sums[i - 1] + nums[i - 1]

for _ in range(m):
    s, d = map(int, sys.stdin.readline().split())
    print(sums[d] - sums[s - 1])
