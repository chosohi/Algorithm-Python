def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for i in range(len(board)):
            num = board[i][move - 1]
            if num == 0:
                continue
            else:
                stack.append(num)
                board[i][move - 1] = 0
                break
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                answer += 2
                stack.pop()
                stack.pop()

    return answer