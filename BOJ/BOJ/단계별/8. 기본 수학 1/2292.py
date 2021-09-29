n = int(input())

temp = 1
dis = 1

while True:
    if n == 1:
        break
    else:
        temp += dis * 6
        dis += 1
        if n <= temp:
            break
print(dis)