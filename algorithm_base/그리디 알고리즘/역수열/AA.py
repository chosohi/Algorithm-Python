def solution(arr1, arr2):
    answer = [[]]
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j]+arr2[i][j])
        answer.append(tmp)
    return answer

arr1 = [[1],[2]]
arr2 = [[3],[4]]
res = solution(arr1, arr2)
print(res)

# zip(a,b)
# a[0] + b[0]
# a[1] + b[1]