def solution(numbers):
    numbers = [str(x) for x in numbers]
    # x라는 원소가 주어진 x를 4번반복하고 앞에서 4개까지 슬라이스한 것을 기준
    # 내림차순 정렬
    numbers.sort(key=lambda x : (x*4)[:4], reverse=True)
    # numbers의 원소가 0만 있을 때에 대한 처리 [0,0,0]
    if numbers[0] == "0" :
        answer = "0"
    else :
        answer = "".join(numbers)
    return answer

print(solution([3,30,34,5,9]))
print(solution([0,0,0]))