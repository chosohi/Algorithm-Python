import sys
sys.stdin = open('input.txt')

N = int(input())


arr = list(int(input()) for _ in range(N) )
# sort 쓴 방법
# arr.sort()
# for i in arr:
#     print(i)

# sort 안 쓴 방법

res = [0]*N
for i in range(N):
    base = arr[i]
    for j in range(N):
        if base > arr[j] :
            res[i] += 1

result = [0]*N

for i in range(len(res)):
    result[res[i]] = arr[i]
for i in result:
    print(i)

