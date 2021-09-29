def solution(answers):
    answer = []
    rate = [0, 0, 0]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == first[i % 5]:
            rate[0] += 1
        if answers[i] == second[i % 8]:
            rate[1] += 1
        if answers[i] == third[i % 10]:
            rate[2] += 1

    for i in range(3):
        if rate[i] == max(rate):
            answer.append(i + 1)

    return answer


# from itertools import cycle 이라는 게 있대요
