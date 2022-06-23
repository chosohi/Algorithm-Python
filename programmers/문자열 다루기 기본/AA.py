def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6 :
        print(len(s) != 4 )
        print(len(s) != 6 )
        answer = False
        return answer
    for  i in s:
        if  (i.isdecimal() == False):
            answer = False
            print(answer)
            break
    return answer

solution("a12234")