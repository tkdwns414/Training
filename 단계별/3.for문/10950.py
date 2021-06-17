t = int(input())
ls = []

for i in range(t):
    ls.append(tuple(map(int, input().split())))

for i in ls:
    print(i[0] + i[1])
