n = int(input())
count = 0
for i in range(n):
    inp = input()
    for i in range(len(inp)):
        check = 1
        temp = ""
        for j in range(i + 1, len(inp)):

            if inp[i] != inp[j]:
                temp = inp[j::]
                break
        if (inp[i] in temp) and (inp[i] != temp):
            check = 0
            break

    if check == 1:
        count += 1

print(count)