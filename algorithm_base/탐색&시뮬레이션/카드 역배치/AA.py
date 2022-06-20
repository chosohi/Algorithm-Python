import sys
sys.stdin = open("input.txt", "rt")

arr = list(range(1,21))
for i in range(10):
    a, b = map(int, input().split())
    lt = a-1
    rt = b-1
    for j in range((lt+rt)//2):
        arr[lt+j], arr[rt-j] = arr[rt-j], arr[lt+j]
        print(arr)

