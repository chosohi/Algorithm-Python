import sys
# sys.stdin = open("input.tx/t", "rt")
N, K = map(int, input().split())
cards = list(map(int,input().split()))
res = []
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            nums = cards[i] + cards[j] + cards[k]
            if nums not in res:
                res.append(nums)
res.sort(reverse=True)
print(res[K-1])
# print(cards.sort())
# cards.sort(reverse=True)
# print(sum(cards[:K]))