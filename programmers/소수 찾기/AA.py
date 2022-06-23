def solution(n):
    answer = 0
    tmp = [0]*10000000
    for i in range(2, n+1):
        if tmp[i] == 0:
            answer += 1
            for j in range(i, n+1,i):
                tmp[j] = 1
    print(tmp)
    return answer
solution(10)