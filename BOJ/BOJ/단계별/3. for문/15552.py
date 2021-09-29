import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    a, b = sys.stdin.readline().split()
    print(int(a) + int(b))
