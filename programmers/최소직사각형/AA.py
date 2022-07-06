def solution(sizes):
    answer = 0
    # 둘 중 높은 값들을 1인덱스로 옮김
    # 각 인덱스의 맥스값을 구해서 곱합
    print(sizes)
    max_w = 0
    max_h = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if sizes[i][1] > max_w:
            max_w = sizes[i][1]
        if sizes[i][0] > max_h:
            max_h = sizes[i][0]

    return max_w * max_h