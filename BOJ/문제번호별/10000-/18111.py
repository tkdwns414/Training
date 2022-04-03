import sys

N, M, B = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res_t, res_h = int(1e9), 0
for i in range(257):
    my_min, my_max = 0, 0
    for j in range(N):
        for k in range(M):
            if ground[j][k] < i:
                my_min += i - ground[j][k]  # 현재 높이보다 작은 블록 수
            else:
                my_max += ground[j][k] - i  # 현재 높이보다 높은 블록 수 (0 포함)

    if my_min > my_max + B:
        continue
    else:
        time = my_min + 2 * my_max
        if res_t >= time:
            res_t, res_h = time, i

print(res_t, res_h)
# 해결 방법 생각하기
# 일단 제일 먼저 가장 많은 숫자를 기준으로 맞추려고 시도해보기
# 근데 그게 안되면 가장 많은 숫자 -1 기준으로 맞추려고 시도해보기
# 될 때까지?
# 위 방식처럼 하려고 하니 복잡함
# 가장 많은 숫자보다 큰 애가 있을 수도 있고 작은 애가 있을 수도 있는데 그걸 블록 개수를 고려하여 가능한지 아닌지 판단이 쉽지 않고
# 가능하다 해도 블록 개수에 따라 음수도 나오고 그러는데 시간 계산이 쉽지 않을 것으로 보임
# 256 * 50 * 50 을 해도 1억이 안 넘으니 그냥 다 보는게 가능
# 시간 초과로 Pypy3로 제출