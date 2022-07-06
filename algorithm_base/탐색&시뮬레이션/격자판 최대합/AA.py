
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

res = []
for i in range(N):
    summation_0 = 0
    summation = 0
    summation_1 = 0
    summation_2 = 0
    for j in range(N):
        summation += board[j][i]
        summation_0 += board[i][j]
        summation_1 += board[j][j]
        summation_2 += board[j][N-1-j]
        res.append(summation)
        res.append(summation_0)
        res.append(summation_1)
        res.append(summation_2)
print(max(res))
