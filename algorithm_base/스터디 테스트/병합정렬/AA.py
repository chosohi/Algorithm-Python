import sys
sys.stdin = open("input.txt", "rt")

arr = list(map(int, input().split()))

def merge(arr, lt, mid, rt):
    tmp = []
    i = lt
    j = mid + 1
    while i <= mid and j <= rt:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    if i <= mid :
        tmp += arr[i:mid+1]
    else:
        tmp += arr[j:rt+1]
    for k in range(lt, rt+1):
        arr[k] = tmp[k-lt]

def merge_sort(arr,lt,rt):
    if lt < rt :
        mid = (lt+rt)// 2
        merge_sort(arr, lt, mid)
        merge_sort(arr, mid+1, rt)
        merge(arr, lt, mid, rt)

merge_sort(arr, 0, len(arr)-1)
print(arr)