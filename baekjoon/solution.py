import sys
sys.stdin = open('input.txt')

N = int(input())


res = 0

for i in range(N) :
    tmp = i
    for j in range(len(str(N))):
        tmp += int(N[j])
    if tmp == N and tmp < res:
        res = tmp

print(res)