import sys

n = int(sys.stdin.readline())

f = 1
s = 2

for i in range(n - 1):
    temp = s
    s = (s + f) % 15746
    f = temp
print(f)
