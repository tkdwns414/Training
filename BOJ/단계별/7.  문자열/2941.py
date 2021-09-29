ls = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

n = input()

for s in ls:
    n = n.replace(s, "x")

print(len(n))