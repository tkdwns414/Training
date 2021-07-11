def w(a, b, c):
    global dict
    if (a, b, c) in dict.keys():
        return dict[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        dict[(a, b, c)] = w(20, 20, 20)
        return dict[(a, b, c)]
    if a < b and b < c:
        dict[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dict[(a, b, c)]
    else:
        dict[(a, b, c)] = (
            w(a - 1, b, c)
            + w(a - 1, b - 1, c)
            + w(a - 1, b, c - 1)
            - w(a - 1, b - 1, c - 1)
        )
        return dict[(a, b, c)]


dict = {}
while True:
    a, b, c = map(int, input().split())
    if a == b and a == c and b == -1:
        break
    if (a, b, c) in dict.keys():
        temp = dict[(a, b, c)]
    else:
        temp = w(a, b, c)
    print(f"w({a}, {b}, {c}) = {temp}")
