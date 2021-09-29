import sys

asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = [8, 7, 6, 5, 4, 3, 2, 1]
cmp = list(map(int, sys.stdin.readline().split()))
if asc == cmp:
    print("ascending")
elif des == cmp:
    print("descending")
else:
    print("mixed")