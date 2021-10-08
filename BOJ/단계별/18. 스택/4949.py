import sys

while True:
    case = sys.stdin.readline().rstrip()  # 그냥 strip 썼다가 한번 틀림 " ." 때문에

    if case == ".":
        break
    else:
        my_stk = []  # deque로 하면 top 보는 방법이 귀찮을 듯
        result = "yes"

        for i in range(len(case)):
            if case[i] == "(":
                my_stk.append("(")
            elif case[i] == ")":
                if my_stk and my_stk[-1] == "(":
                    my_stk.pop()
                else:
                    result = "no"
                    break
            elif case[i] == "[":
                my_stk.append("[")
            elif case[i] == "]":
                if my_stk and my_stk[-1] == "[":
                    my_stk.pop()
                else:
                    result = "no"
                    break
        if my_stk:
            print("no")
        else:
            print(result)