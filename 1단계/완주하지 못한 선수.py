def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]


# 효율성 면에서 문제가 있음 (전체 검수 불가)
