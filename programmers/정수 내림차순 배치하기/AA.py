# def solution(n):
#     answer = ''
#     numbers = list(str(n))
#     print(numbers)
#     numbers = [int(i) for i in numbers]
#     numbers.sort(reverse=True)
#     for i in numbers:
#         answer += str(i)
#     answer = int(answer)
#     return answer

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    print(ls)
    return int("".join(ls))

res = solution(118372)
print(res)
