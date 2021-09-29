def solution(N, stages):
    fail_rate = {}

    for i in range(1, N + 1):
        nume = 0
        deno = 0
        for stage in stages:
            if stage >= i:
                deno += 1
            if stage == i:
                nume += 1

        if deno == 0:
            fail_rate[i] = 0
        else:
            fail_rate[i] = nume / deno

    return sorted(fail_rate, key=lambda x: fail_rate[x], reverse=True)