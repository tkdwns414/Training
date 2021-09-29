import sys

n = int(sys.stdin.readline())

for i in range(n):
    check = 0
    ls = list(map(int, input().split()))
    avg = (sum(ls) - ls[0]) / ls[0]
    for j in range(1, ls[0] + 1):
        if ls[j] > avg:
            check += 1

    print("{:.3f}%".format(check / ls[0] * 100))
