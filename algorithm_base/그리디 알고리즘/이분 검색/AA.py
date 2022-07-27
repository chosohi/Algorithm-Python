# import sys
# sys.stdin = open("input.txt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

lt = 0
rt = len(arr)-1

while lt<=rt:
    if lt > rt:
        break
    md = (lt+rt) // 2
    if M > arr[md] :
        lt = md+1
    elif M < arr[md] :
        rt = md-1
    else:
        print(md+1)
        break
