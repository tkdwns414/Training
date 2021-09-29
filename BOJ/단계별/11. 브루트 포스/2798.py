n, m = map(int, input().split())
ls = list(map(int, input().split()))

dst = len(ls)
my_max = 0

for i in range(dst):
    for j in range(i + 1, dst):
        for k in range(j + 1, dst):
            if my_max < ls[i] + ls[j] + ls[k] and ls[i] + ls[j] + ls[k] <= m:
                my_max = ls[i] + ls[j] + ls[k]

print(my_max)