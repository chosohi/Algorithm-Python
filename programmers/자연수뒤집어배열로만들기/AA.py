def solution(n):
    answer = []
    num = list(str(n))
    num.reverse()
    num = [int(i) for i in num]

    return num

# 문제를 잘 읽자 sort가 아니라 뒤집는거임