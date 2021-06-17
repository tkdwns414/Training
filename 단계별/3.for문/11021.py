import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    a, b = sys.stdin.readline().split()
    print(f"Case #{i+1}: {a} + {b} = {int(a) + int(b)}")
