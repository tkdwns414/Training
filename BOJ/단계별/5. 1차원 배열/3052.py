ls = []
for i in range(10):
    ls.append(int(input()) % 42)

ls = set(ls)

print(len(ls))