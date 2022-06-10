import sys
sys.stdin = open("input.txt", "rt")
T = int(input())

for tc in range(1,T+1):
    N,s,e,k = map(int, input().split())
    nums = list(map(int,input().split()))

    res = nums[s-1:e]
    res.sort()
    print('#',tc, end=" ")
    print(res[k-1])
    print()