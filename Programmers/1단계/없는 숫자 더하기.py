def solution(numbers):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return sum(list(set(nums) - set(numbers)))

    # 그냥 아래도 됨
    # return 45 - sum(numbers)
