def solution(n, lost, reserve):
    new_lost = list(set(lost) - set(reserve))
    new_res = list(set(reserve) - set(lost))

    for l in new_res:
        if l - 1 in new_lost:
            new_lost.remove(l - 1)
        elif l + 1 in new_lost:
            new_lost.remove(l + 1)

    return n - len(new_lost)