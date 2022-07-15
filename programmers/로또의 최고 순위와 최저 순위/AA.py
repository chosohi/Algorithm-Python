def solution(lottos, win_nums):
    answer = []
    max_win = 0
    min_win = 0
    for num in lottos:
        if num in win_nums:
            min_win += 1
        elif num == 0:
            max_win += 1
    max_win += min_win
    print(max_win, min_win)
    ranks = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer.append(ranks[max_win])
    answer.append(ranks[min_win])
    return answer