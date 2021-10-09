import sys
from collections import deque

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

step = 0
num = 1
stk = deque()
result = []

while True:
    if step == n:
        print("\n".join(result))
        break
    if num <= nums[step]:
        stk.append(num)
        result.append("+")
        num += 1
    else:
        if stk.pop() != nums[step]:
            print("NO")
            break
        else:
            result.append("-")
            step += 1


# 처음에 문제 무슨 말인지 이해하는데 조금 걸렸음
# 현재 숫자가 내가 필요한 숫자보다 작거나 같으면 일단 다 더함
# 현재 숫자가 내가 필요한 숫자보다 크면 이미 스택에 필요한 숫자가 들어간거임
# 그때 pop 했을 때 내가 필요한 애랑 다르면 불가능
# 같으면 다음으로
