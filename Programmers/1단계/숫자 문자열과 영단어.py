def solution(s):
    temp = ""
    answer = ""
    dic = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for n in s:
        if not n.isdigit():
            temp += n
            if temp in dic.keys():
                answer += str(dic[temp])
                temp = ""
        else:
            answer += n

    return int(answer)


# replace가 모두 바꾸는 줄 몰랐음. 아래는 replace 사용 버전
"""
def solution(s):

    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",}
    
    for item in dic:
        s = s.replace(item,dic[item])
        
    return int(s)
"""