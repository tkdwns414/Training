n = int(input())
ls = list(map(int, input().split()))

count = 0
for num in ls:
    check = 1
    for i in range(2, num):
        if num % i == 0:
            check = 0
            break
    if check and num != 1:
        count += 1

print(count)