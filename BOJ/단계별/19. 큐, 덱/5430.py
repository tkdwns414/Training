import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    my_deque = deque(eval(sys.stdin.readline().strip()))
    reverse_state = False
    error = False

    for func in p:
        if func == "R":
            if reverse_state:
                reverse_state = False
            else:
                reverse_state = True
        else:
            if my_deque:
                if reverse_state:
                    my_deque.pop()
                else:
                    my_deque.popleft()
            else:
                error = True
                break

    if error:
        print("error")
    else:
        if reverse_state:
            print("[" + ",".join(map(str, reversed(my_deque))) + "]")
        else:
            print("[" + ",".join(map(str, my_deque)) + "]")

# 띄어쓰기 때문에 틀렸다는거 너무하네...
