def solution(numbers, hand):
    answer = ""
    kp = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        "*": [3, 0],
        0: [3, 1],
        "#": [3, 2],
    }

    L = "*"
    R = "#"

    for num in numbers:
        if num in [1, 4, 7]:
            L = num
            answer += "L"
        elif num in [3, 6, 9]:
            R = num
            answer += "R"
        else:
            R_dis = abs(kp[R][0] - kp[num][0]) + abs(kp[R][1] - kp[num][1])
            L_dis = abs(kp[L][0] - kp[num][0]) + abs(kp[L][1] - kp[num][1])

            if R_dis > L_dis:
                L = num
                answer += "L"
            elif L_dis > R_dis:
                R = num
                answer += "R"
            else:
                if hand == "right":
                    R = num
                    answer += "R"
                elif hand == "left":
                    L = num
                    answer += "L"
    return answer