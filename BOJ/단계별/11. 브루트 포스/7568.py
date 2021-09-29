n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))

for i in range(n):
    ls[i].append(1)
    for j in range(n):
        if i == j:
            pass
        else:
            if ls[i][0] < ls[j][0] and ls[i][1] < ls[j][1]:
                ls[i][2] += 1
    print(ls[i][2], end=" ")
