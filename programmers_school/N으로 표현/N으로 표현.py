def solution(N, number):
    answer = 0
    # 최대 8개까지 연산 가능
    s = [set() for x in range(8)]

    # s를 enumerate로 꺼내는데 i의 시작값은 1
    for i, x in enumerate(s, start=1):
        # set인 x에 각 수들을 i번 반복한 문자열을 넣음 5, 55, 555...
        x.add(int(str(N)*i))
    for i in range(1,len(s)):
        for j in range(i):
            # j= 0,1,2 = op1
            # op2 = 2, 1, 0
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1 *op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i+1
            break
    else :
        answer -=1
    return answer
