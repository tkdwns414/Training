import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    my_stk = deque()
    temp = sys.stdin.readline()
    result = "YES"
    for i in range(len(temp)):
        if temp[i] == "(":
            my_stk.append("(")
        elif temp[i] == ")":
            if my_stk:
                my_stk.pop()
            else:
                result = "NO"
    if my_stk:
        print("NO")
    else:
        print(result)

# 솔직히 스택으로 안풀어도 되긴 함
