import sys

t = int(sys.stdin.readline())

word = []

for _ in range(t):
    word.append(sys.stdin.readline().rstrip())

word = list(set(word))  # 중복 제거
word.sort(key=lambda x: (len(x), x))  # 정렬하는 기준이 len으로 먼저 하고 같으면 x로 해라

print("\n".join(word))
