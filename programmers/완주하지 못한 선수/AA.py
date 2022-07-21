def solution(participant, completion):
    answer = ''
    tmp = {}
    for person in (participant):
        # participant을 하나씩 순회하면서
        # tmp에 키:밸류로 1씩 더해줌
        if tmp.get(person):
            tmp[person] += 1
        else:
            tmp[person] = 1

    # completion를 순회하면서
    for person in completion:
    # tmp의 키값에 해당되고, 그 벨류 1이상이면
        if person in tmp and tmp[person] >= 1:
        # participant의 벨류를 1씩 감소
            tmp[person] -= 1
    for val in tmp :
        if tmp[val] >= 1:
            answer = val
    return answer

