def solution(new_id):
    answer = ""
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for value in new_id:
        if value.islower() or value.isdigit() or value in ["-", "_", "."]:
            answer += value
    # 3단계
    while ".." in answer:
        answer = answer.replace("..", ".")
    # 4단계
    if answer[0] == ".":
        if len(answer) >= 2:
            answer = answer[1:]
    if answer[-1] == ".":
        if len(answer) == 1:
            answer = ""
        else:
            answer = answer[:-1]
    # 5단계
    if not answer:
        answer = "a"
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer

#정규식이라는게 있대요