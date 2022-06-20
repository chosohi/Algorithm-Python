import sys
sys.stdin = open("input.txt", "rt")
N,M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

lt = 0
rt = N-1
while lt < rt:
    mid = (lt+rt) // 2
    print(lt, mid, rt)
    if nums[mid] == M:
        print(mid+1)
        break
    elif nums[mid] < M:
        lt = mid + 1
    elif nums[mid] > M:
        rt = mid - 1


