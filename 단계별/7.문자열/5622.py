ls = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

n = input()

time = 0
for s in n:
    for item in ls:
        if s in item:
            time += ls.index(item) + 3

print(time)