n = int(input())
new = n
count = 0

while True:
    count += 1
    new = new % 10 * 10 + (new // 10 + new % 10) % 10
    if new == n:
        print(count)
        break

"""
def itos(a):
    if a < 10:
        return "0" + str(a)
    else:
        return str(a)


def tsum(a):
    return itos(int(a[0]) + int(a[1]))


n = int(input())
new = n
count = 0

while True:
    count += 1
    new = itos(new)
    new = new[1] + tsum(new)[1]
    new = int(new)

    if new == n:
        print(count)
        break
"""