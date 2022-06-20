import sys
sys.stdin = open("input.txt", "rt")
arr = list(map(int, input().split()))
print(arr)
for i in range(len(arr)):
    exchange = 0
    for j in range(len(arr)-1, i, -1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            exchange += 1
    print(arr)
    print(exchange)
    if exchange == 0: # 정렬할 것이 없다면
        break

print(arr)