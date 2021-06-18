n = int(input())

ans = 0

for i in range(1, n + 1):
    if i < 100:
        ans += 1
    else:
        if (i % 10 + i // 100) == 2 * (i // 10 % 10):
            ans += 1
print(ans)