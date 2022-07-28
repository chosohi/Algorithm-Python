def solution(n, lost, reserve):
    answer = 0
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))

    student = [1] * (n + 1)

    for num in new_lost:
        student[num] = 0

    for num in new_lost:
        if num - 1 in new_reserve:
            new_reserve.remove(num - 1)
            student[num] += 1
        elif num + 1 in new_reserve:
            new_reserve.remove(num + 1)
            student[num] += 1
    answer = student.count(1) - 1
    return answer

solution(5, [2,4], [1,3,5])