def solution(n, arr1, arr2):
    answer = []

    new_arr = []
    for i in range(n):
        num = list(bin(arr1[i] | arr2[i]))[2:]
        if len(num) < n:
            while len(num) < n:
                num.insert(0, '0')
        new_arr.append(num)

    for i in range(len(new_arr)):
        tmp = ''
        for j in range(len(new_arr)):
            if new_arr[i][j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)

    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])

# def solution(n, arr1, arr2):
#     answer = []
#     for i in range(n):
#         tmp = bin(arr1[i] | arr2[i])
#
#         tmp = tmp[2:].zfill(n)
#         tmp = tmp.replace('1', '#')
#         tmp = tmp.replace('0', ' ')
#         answer.append(tmp)
#
#     return answer