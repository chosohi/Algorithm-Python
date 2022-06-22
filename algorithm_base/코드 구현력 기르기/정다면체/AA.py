# import sys
# sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())

res = []
nums = []

for i in range(1, N+1):
    for j in range(1, M+1):
        nums.append(i+j)
nums.sort()
small_nums = set(nums)
res = [0]*40

for num in small_nums:
    res[num] = nums.count(num)
maximum = max(res)
for i in range(len(res)):
    if res[i] == maximum:
        print(i, end=' ')
