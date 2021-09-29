# 대각선 줄 개수는 1,2,3,4,5...
# 대각선 읽는 순서는 홀수는 아래부터 짝수는 위에부터
# 분자 분모 합은 대각선 더하기 1
n = int(input())
temp = 0
step = 1
while temp + step < n:
    temp += step
    step += 1

if step % 2 == 0:
    print(f"{n-temp}/{step - n + temp+ 1}")
else:
    print(f"{step - n + temp +1}/{n-temp}")