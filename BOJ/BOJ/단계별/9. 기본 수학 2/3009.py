ls = [[], []]
for i in range(3):
    a, b = map(int, input().split())
    if a in ls[0]:
        ls[0].remove(a)
    else:
        ls[0].append(a)
    if b in ls[1]:
        ls[1].remove(b)
    else:
        ls[1].append(b)

print(ls[0][0], ls[1][0])
