import sys
from typing import Sequence

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

result = line[0] * price[0]
check = price[0]

for i in range(1, n - 1):
    if price[i] < check:
        check = price[i]
    result += line[i] * check

print(result)