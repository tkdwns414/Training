def solution(board, moves):
    answer = 0
    box = []

    for move in moves:
        for i in range(len(board[0])):
            if board[i][move - 1] != 0:
                box.append(board[i][move - 1])
                board[i][move - 1] = 0
                break

        if len(box) >= 2 and box[-2] == box[-1]:
            box.pop()
            box.pop()
            answer += 2

    return answer
