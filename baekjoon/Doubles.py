for tc in range(3):
    arr = list(map(int, input().split()))
    cnt = 0
    if arr[0] == -1:
        break
    else:
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if arr[i]*2 == arr[j]:
                    cnt +=1
    print(cnt)