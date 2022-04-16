N = int(input())

#큰값부터 나누고, 나머지에서 계속 나눈다
#모든 if문에 해당하지 않으면 -1출력

cnt = 0
sub = 0
#나눌 수 없으면
if N // 5 ==0 or N // 3 == 0:
    print(-1)
else:
    cnt += N//5
    sub = N % 5
    cnt += sub//3
    sub %= 3
    #3으로 나눈 후, 1,2 남아있으면 한봉지 추가
    if sub>0:
        cnt += 1
    print(cnt)


