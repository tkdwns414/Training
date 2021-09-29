n, m = map(int, input().split())
ls = []
startW = "WBWBWBWB"
startB = "BWBWBWBW"

for i in range(n):
    ls.append(input())

res = n * m

for i in range(n - 7):
    for j in range(m - 7):
        minW = 0
        minB = 0
        for k in range(8):
            for l in range(8):
                if (i + k) % 2 == 0:
                    if ls[i + k][j + l] != startW[l]:
                        minW += 1
                    if ls[i + k][j + l] != startB[l]:
                        minB += 1
                else:
                    if ls[i + k][j + l] != startW[l]:
                        minB += 1
                    if ls[i + k][j + l] != startB[l]:
                        minW += 1
        res = min(minW, minB, res)
print(res)