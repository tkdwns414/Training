n = int(input())

for i in range(n):
    k, inp = input().split()
    for i in range(len(inp)):
        print(inp[i] * int(k), end="")
    print()