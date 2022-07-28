def solution(s):
    answer = len(s)
    # aabbccdd 압축의 범위는 최대 문자열 길이 / 2 -> 그 위로는 압축 불가
    for i in range(1, int(len(s)/2)+1):
        comp = ''
        cnt = 1
        summation = 0
        for j in range(0, len(s), i):
            tmp = s[j:j+i]
            if comp == tmp:
                cnt += 1
            elif comp != tmp:
                summation += len(tmp)
                if cnt > 1:
                    # cnt가 10, 100 단위일 수도 있음
                    summation += len(str(cnt))
                cnt = 1
                comp = tmp

        if cnt > 1:
            summation += len(str(cnt))
        answer = min(answer, summation)
    return answer