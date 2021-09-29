def solution(n):
    result = n
    while n != 0:
        result += n % 10
        n = int(n / 10)
    return result


n = int(input())
for i in range(n):
    if solution(i) == n:
        print(i)
        break
    if i == n - 1:
        print(0)