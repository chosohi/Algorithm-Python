# import sys
# sys.stdin = open("input.txt")

K, N = map(int, input().split())
# N개 이상도 N개 만드는 것에 포함
# N개를 만들 수 있는 랜선의 초대 길이 단위 출력
arr = []
for i in range(K):
    arr.append(int(input()))
s = 0
e = max(arr)
length = 0
res = 0
while True:
    m = (s+e) // 2
    for num in arr:
        res += num // m
    if res >= N :
        length = m
        s = m + 1
        if s > e:
            print(length)
            break
    else:
        e = m - 1
    length = 0
    res = 0
