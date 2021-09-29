while True:
    ls = list(map(int, input().split()))
    if ls[0] == 0:
        break
    side = ls.pop(ls.index(max(ls)))
    if side ** 2 == ls[0] ** 2 + ls[1] ** 2:
        print("right")
    else:
        print("wrong")
