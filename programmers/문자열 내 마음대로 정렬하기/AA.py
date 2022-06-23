def solution(strings, n):
    answer = []
    # n번째 값 기준 정렬 후, x 전체값 기준 재정렬
    strings.sort(key=lambda x: (x[n], x))
    print(strings)
    return strings
