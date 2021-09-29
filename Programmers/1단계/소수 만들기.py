def isprime(num):
    for i in range(2, int(pow(num, 1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    end = len(nums)

    for i in range(end):
        for j in range(i + 1, end):
            for k in range(j + 1, end):
                if isprime(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer


# combinations 라는게 있답니다 itertools
