import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
count = 0

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

for coin in reversed(coins):
    if k == 0:
        break
    elif k >= coin:
        count += k // coin
        k %= coin

print(count)