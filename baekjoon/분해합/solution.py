import sys
sys.stdin = open('input.txt')

N = int(input())

# 생성자 변수 선언
res = 0


for i in range(N):
    tmp = i
    num = str(tmp)
    for j in num:
        tmp += int(j)

    if tmp == N:
        res = i
        break
print(res)