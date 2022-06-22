# import sys
# sys.stdin = open("input.txt", "rt")
#

def digit_sum(x):
    res = 0
    for i in x:
        res+= int(i)
    return res

n = int(input())

nums = list((input().split()))

maximum = 0
res = 0
for i in range(n):
    hap = digit_sum(nums[i])
    if hap > maximum:
        maximum = hap
        res = nums[i]
print(res)







# 137