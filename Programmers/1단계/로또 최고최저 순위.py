def solution(lottos, win_nums):
    answer = [0, 0]
    rank = [6, 6, 5, 4, 3, 2, 1]

    for num in lottos:
        if num in win_nums:
            answer[0] += 1
            answer[1] += 1
        if num == 0:
            answer[0] += 1

    answer[0] = rank[answer[0]]
    answer[1] = rank[answer[1]]

    return answer