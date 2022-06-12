import sys

n, k = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))
sums = [0 for _ in range(n - (k - 1))]
sums[0] = sum(temp[0:k])

for i in range(1, n - (k - 1)):
    sums[i] = sums[i - 1] - temp[i - 1] + temp[i + k - 1]

print(max(sums))

# sums 범위를 n으로 잘못 잡아서 다 음수일 때 0이 나오게 해서 한번 틀림