import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())

# [[1, 2, 4], [8, 16, 32]]
arr = list(list(map(int, input().split())) for _ in range(N))
K = int(input())
for _ in range(K):
    i,j,x,y = map(int, input().split())
    # print(i,j,x,y)
    res = 0
    for a in range(i-1,x):
        for b in range(j-1,y):
            res += arr[a][b]
    print(res)