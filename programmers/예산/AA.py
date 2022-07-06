def solution(d, budget):
    answer = 0
    # 예산에서 제일 작은 값부터 뺀다
    d.sort()
    i = 0
    while i <= len(d) - 1 and budget > 0:
        if budget <= 0:
            break
        if d[i] <= budget:
            budget -= d[i]
            answer += 1
        i += 1

    return answer

solution([1,3,2,5,4], 9)