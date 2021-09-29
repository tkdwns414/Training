def d(n):
    ans = n
    while n > 0:
        ans += n % 10
        n //= 10
    return ans


ls = []
for i in range(1, 10001, 1):
    ls.append(i)

for i in range(1, 10001, 1):
    if d(i) in ls:
        ls.remove(d(i))

for i in range(len(ls)):
    print(ls[i])