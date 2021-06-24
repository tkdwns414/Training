def hanoi(n, src, dst):
    temp = 6 - src - dst
    if n == 0:
        return
    hanoi(n - 1, src, temp)
    print(src, dst)
    hanoi(n - 1, temp, dst)


n = int(input())
print(pow(2, n) - 1)
hanoi(n, 1, 3)
