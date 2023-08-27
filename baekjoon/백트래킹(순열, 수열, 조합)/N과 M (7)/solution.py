import sys
sys.stdin = open('baekjoon/백트래킹(순열, 수열, 조합)/N과 M (1)/input.txt', 'r') #file open

N = int(input())


res = 0

for i in range(N) :
    tmp = i
    for j in range(len(str(N))):
        tmp += int(j)
    if tmp == N and tmp < res:
        res = tmp

print(res)