import sys

x = int(sys.stdin.readline())
ls = []

# 해당 숫자에 대해서 최소 횟수를 저장해놓는 형식
ls.append(0)
ls.append(1)
ls.append(1)

for i in range(3, x):
    ls.append(ls[i - 1] + 1)
    if (i + 1) % 3 == 0 and ls[i] > ls[i // 3] + 1:
        ls[i] = ls[i // 3] + 1
    if (i + 1) % 2 == 0 and ls[i] > ls[i // 2] + 1:
        ls[i] = ls[i // 2] + 1
    # i번째 숫자까지의 최소 연산 횟수는 (i//3, i//2, i-1 까지의 최소 연산횟수 +1) 중 최솟값
    # i번째 숫자는 i+1임
print(ls[x - 1])
