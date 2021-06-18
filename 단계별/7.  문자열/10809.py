n = input()

for i in range(ord("a"), ord("z") + 1):
    if chr(i) in n:
        print(n.find(chr(i)), end=" ")
    else:
        print(-1, end=" ")
