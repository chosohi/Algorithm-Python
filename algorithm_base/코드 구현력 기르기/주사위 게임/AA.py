# import sys
# sys.stdin = open('input.txt')

N = int(input())

res = []
for _ in range(N):
    person = list(map(int, input().split()))
    tmp = [0]*7
    for i in range(3):
        tmp[person[i]] += 1
    idx = tmp.index(max(tmp))
    tmp.sort(reverse=True)
    if max(tmp) == 3:
        res.append(10000+1000*idx)
    elif max(tmp) == 2:
        res.append(1000+idx*100)
    else:
        res.append(100*tmp.index(max(tmp)))
print(max(res))