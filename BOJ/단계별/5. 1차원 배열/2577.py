ls = []
for i in range(10):
    ls.append(0)

a = int(input())
b = int(input())
c = int(input())

res = str(a * b * c)

for item in res:
    ls[int(item)] += 1

for i in range(10):
    print(ls[i])