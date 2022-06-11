import sys

s = sys.stdin.readline().rstrip()
temp = []
temp.append([0] * 26)

for i in range(1, len(s) + 1):
    alpha = ord(s[i - 1]) - 97
    new = temp[i - 1].copy()
    new[alpha] += 1
    temp.append(new)

n = int(sys.stdin.readline())
for _ in range(n):
    a = sys.stdin.readline().split()
    alpha = ord(a[0]) - 97
    res = temp[int(a[2]) + 1][alpha] - temp[int(a[1])][alpha]
    sys.stdout.write(str(res) + "\n")

# 다른 블로그들 자기들 100점이라 하는데 막상 제출하면 다 50점임
# 아래 코드는 50점짜리 코드(Python으로 제출 시에)
# Pypy는 자주 쓰는 코드 캐싱 기능이 있어 반복문이 많은 코드에 있어 Python보다 빠르지만
# 메모리를 사용하기 때문에 메모리 초과를 주의해아 한다. 간단한 코드는 Python이 더 빠를 수도 있으며
# 재귀 깊이 설정 같은 경우 Pypy는 불가능하다
# import sys

# s = sys.stdin.readline().rstrip()
# temp = [[0] * 26 for _ in range(len(s) + 1)]
# for i in range(1, len(s) + 1):
#     temp[i][ord(s[i - 1]) - 97] = 1
#     for key in range(26):
#         temp[i][key] += temp[i - 1][key]

# n = int(sys.stdin.readline())
# for _ in range(n):
#     a = sys.stdin.readline().split()
#     alpha = ord(a[0]) - 97
#     res = temp[int(a[2]) + 1][alpha] - temp[int(a[1])][alpha]
#     sys.stdout.write(str(res) + "\n")

# 처음에 다 초기화를 해서 0을 넣어두고
# 다음에 꺼내는 애의 알파벳을 더하고
# 나머지는 이전거 그대로