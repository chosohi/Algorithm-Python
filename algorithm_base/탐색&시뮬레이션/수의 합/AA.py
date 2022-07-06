# import sys
# sys.stdin = open("input.txt", "rt")

N, M = map(int,input().split())
nums = list(map(int, input().split()))

lt = 0
cnt = 1
res = 0
while lt+cnt <= N and lt < N:
    summation = sum(nums[lt:lt+cnt])
    if summation > M :
        lt += 1
        cnt = 1
    elif summation == M:
        lt += 1
        cnt = 1
        res += 1
    else:
        cnt += 1
print(res)