s = int(input())
e = int(input())

ls = []

for num in range(s, e + 1):
    check = 1
    for i in range(2, num):
        if num % i == 0:
            check = 0
            break
    if check and num != 1:
        ls.append(num)

if ls:
    print(sum(ls))
    print(min(ls))
else:
    print(-1)
