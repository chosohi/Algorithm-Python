# import sys
# sys.stdin = open("input.txt", "rt")

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

res = 0
for i in range(N//2+1):
    if i == N//2:
        res += sum(board[i][N//2-i:N//2+i+1])
        break
    res += sum(board[i][N//2-i:N//2+i+1])
    res += sum(board[N-i-1][N//2-i:N//2+i+1])
print(res)