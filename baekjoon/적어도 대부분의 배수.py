arr = list(map(int, input().split()))

for i in range(1, 9999999):
    for j in range(len(arr)-2):
        if i % arr[j] ==0 and i % arr[j+1] ==0 and i % arr[j+2] ==0:
            print(i) 
            break
for i in range(1, 9999999):
    cnt = 0
    for j in range(len(arr)):
        if i % arr[j] ==0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break
    