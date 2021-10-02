import sys

given = sys.stdin.readline().rstrip().split("-")

result = 0
for i in range(len(given)):
    nums = map(int, given[i].split("+"))
    if i == 0:
        result += sum(nums)
    else:
        result -= sum(nums)

print(result)

"""
이거 왜 안될까? syntax error?
for i in range(len(given)):
    if i == 0:
        result = eval(given[i])
    else:
        result -= eval(given[i])
"""