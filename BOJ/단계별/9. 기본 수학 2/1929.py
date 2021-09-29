import sys

s, e = map(int, sys.stdin.readline().split())

for num in range(s, e + 1):
    check = 1
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            check = 0
            break
    if check and num != 1:
        print(num)