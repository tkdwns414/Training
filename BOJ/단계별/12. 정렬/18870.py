import sys

t = int(sys.stdin.readline())

ls = list(map(int, sys.stdin.readline().split()))
temp = list(sorted((set(ls))))

dic = {temp[i]: i for i in range(len(temp))}

for item in ls:
    print(dic[item], end=" ")

"""
시간 부족
for item in ls:
    print(temp.index(item), end=" ")
"""