import sys
sys.stdin = open('input.txt')

N = input()


number = ['0','1','2','3','4','5','6','7','8','9']

res = [0]*10
cnt = 1

for i in range(N):
    number[i] += 1
    if number[int(i)] >1:
        cnt += 1
        