def solution(dartResult):
    num = ''
    answer = []
    score = {'S':1, 'D':2, 'T':3}
    for i in dartResult:
        if i.isdecimal():
            if num:
                num = int(num + str(i))
            else:
                num = str(i)
        elif i.isalpha():
            # print(answer[-1])
            # print(score[dartResult[i][j]])
            answer.append(int(num))
            num = ''
            answer[-1] = (answer[-1]) ** score[i]
        elif i == "*":
            try:
                answer[-2] *= 2
                answer[-1] *= 2
            except:
                answer[-1] *= 2
        elif i == "#":
            answer[-1] *= (-1)

    return sum(answer)