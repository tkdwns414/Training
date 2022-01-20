import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

s, e = 1, max(trees)

while s <= e:
    h = (s + e) // 2
    wood = 0

    for tree in trees:
        if tree > h:
            wood += tree - h
        # wood += tree - h if (tree - h) >= 0 else 0 시간초과

    if wood >= m:
        s = h + 1
    else:
        e = h - 1
print(e)