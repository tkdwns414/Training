import sys


def my_power(a, k, p):
    if k == 1:
        return a % p
    else:
        temp = my_power(a, k // 2, p)
        if k % 2 == 0:
            return temp * temp % p
        else:
            return a * temp * temp % p


n, k = map(int, sys.stdin.readline().split())
fact = [1 for _ in range(n + 1)]  # fact[i] = i! % p
p = 1000000007

for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % p

up = fact[n]
down = fact[n - k] * fact[k] % p
print(up * my_power(down, p - 2, p) % p)

# 페르마 소정리
# p가 소수이고 a가 p로 나누어지지 않는 정수라면
# a^p-1 = 1 (mod p)
# a * a^p-2 = 1 (mod p)
# a^p-2 = a^-1 (mod p)
# a = 2, p = 7
# 8 / 4 를 7로 나누었을 때 나머지
# => (8%7 * 4^-1%7) => 1 * 4^5 % 7
# 8 / 2 를 5로 나누었을 때 나머지
# => (8%5 * 2^-1%5)%5 => (3 * 2^3%5)%5
# 제곱수가 크니까 예전에 풀었던 문제 이용(거듭제곱 연산 빠르게)
# fact[i-1] = i! 는 메모리 초과 나서 fact[i-1] = i! % p로 변경
# fact[i-1] = i! %p로 하니까 틀려서 k가 0일 때 문제가 있나 싶어서 fact[i] = i! % p로 고치니 성공
