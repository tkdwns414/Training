import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    c_type = {}
    for __ in range(n):
        clothes = sys.stdin.readline().split()[1]
        if clothes in c_type.keys():
            c_type[clothes] += 1
        else:
            c_type[clothes] = 1
    result = 1
    for item in c_type.values():
        result *= item + 1  # 안 입은 것 포함 +1
    print(result - 1)  # 전체 다 안 입은 것 미포함 -1
