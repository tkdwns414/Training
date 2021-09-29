while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for num in range(n + 1, 2 * n + 1):
        check = 1
        for i in range(2, int(pow(num, 0.5)) + 1):
            if num % i == 0:
                check = 0
                break
        if check == 1 and num != 1:
            count += 1
    print(count)
