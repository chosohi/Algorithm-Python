import sys
sys.stdin = open("input.txt", "rt")

arr = list(map(int, input().split(',')))
goal = int(input())

lt = 0
rt = len(arr)-1

while lt <= rt:
    mid = (lt+rt)//2
    if arr[mid] == goal:
        print(mid)
        break
    elif arr[mid] < goal:
        lt = mid + 1
    else :
        rt = mid - 1
