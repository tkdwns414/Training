import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))
card_dict = dict()

for card in cards:
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

for check in checks:
    if check in card_dict:
        print(card_dict[check], end=" ")
    else:
        print(0, end=" ")


# 이분탐색으로 안 풀었음
