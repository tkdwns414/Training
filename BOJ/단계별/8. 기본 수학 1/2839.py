n = int(input())
env = 0
while n > 0:
    if n % 5 == 0:
        env += n // 5
        break
    else:
        n -= 3
        env += 1
if n < 0:
    print(-1)
else:
    print(env)