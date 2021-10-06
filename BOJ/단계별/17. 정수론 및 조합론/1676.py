import sys

n = int(sys.stdin.readline())

two = 0
five = 0

for i in range(1, n + 1):
    n = i
    while n % 2 == 0:
        two += 1
        n /= 2
    while n % 5 == 0:
        five += 1
        n /= 5
print(two if two < five else five)