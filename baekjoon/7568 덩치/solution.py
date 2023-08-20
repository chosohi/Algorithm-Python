
N = int(input())


arr = [list(map(int,input().split())) for _ in range(N)]
# print(arr)
# [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]
res = [1]*N

# print(arr)
for i in range(N):
    tmp = arr[i]
    for j in range(N):
        if tmp[0] < arr[j][0] and tmp[1] <arr[j][1]:
            res[i] += 1
print(*res)