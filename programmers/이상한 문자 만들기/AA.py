def solution(s):
    s = s.split(" ")
    answer = []
    for word in s:
        w = ""
        for i in range(len(word)):
            if i % 2== 0:
                w += word[i].upper()
            else:
                w += word[i].lower()
        answer.append(w)
    return ' '.join(answer)
res = solution("try hello world")
print(res)

# s.split() 은 모든 공백 없앰
# ''.join(list) list의 각 항목을 ''로 묶음 즉 뛰어쓰기가 있는 문자열 생성