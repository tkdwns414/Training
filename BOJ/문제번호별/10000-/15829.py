import sys

r, M, H = 31, 1234567891, 0
L = int(sys.stdin.readline())
pr = sys.stdin.readline().rstrip()
for i in range(L):
    H += (ord(pr[i]) - 96) * (r ** i)
print(H % M)

# 학교에서 배웠던 해시 설명이 나와있는 문제다
"""
50점 짜리 : 괜히 연산마다 나머지 연산 넣어서 시간 통과를 못한듯?
r, M, H = 31, 1234567891, 0
L = int(sys.stdin.readline())
pr = sys.stdin.readline().rstrip()
for i in range(L):
    H += ((ord(pr[i]) - 96) * pow(r, i)) % M
print(H)
"""