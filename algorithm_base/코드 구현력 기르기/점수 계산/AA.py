# import sys
# sys.stdin = open('input.txt')

N = int(input())
result = list(map(int, input().split()))

cnt = 0
score = 0

for i in range(N):
    if result[i] == 1:
        cnt += 1
        score += cnt * result[i]
    else:
        cnt = 0
print(score)