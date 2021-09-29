import sys


def solve(n, count):
    global temp, res
    if n == count:
        res.append(temp)
    else:
        for i in range(4):
            if opnum[i] > 0:
                bef = temp
                if i == 3 and temp < 0:
                    temp = -int(eval(str(-temp) + op[i] + str(num[n + 1])))
                else:
                    temp = int(eval(str(temp) + op[i] + str(num[n + 1])))
                opnum[i] -= 1
                solve(n + 1, count)
                temp = bef
                opnum[i] += 1


op = ["+", "-", "*", "//"]
t = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
opnum = list(map(int, sys.stdin.readline().split()))
res = []
temp = num[0]
solve(0, t - 1)
print(max(res))
print(min(res))
