def solution(n):
    answer = 0
    num = n ** (1/2)
    # 양의 정수인지 확인
    if num == int(num):
        answer = int((num+1) ** 2)
    else:
        answer = -1
    return answer

res = solution(121)
print(res)