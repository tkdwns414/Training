def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]

    # for x,y in zip(a,b):
    #     answer += x * y

    return answer