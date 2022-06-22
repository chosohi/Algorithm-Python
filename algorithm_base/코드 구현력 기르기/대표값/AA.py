# import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
scores = list(map(int, input().split()))

middle = round(sum(scores) / n)

res = 0
gap = abs(middle-scores[res])
for i in range(1, len(scores)):
    if abs(middle-scores[i]) < gap:
        res = i
        gap = abs(middle - scores[res])
    elif abs(middle-scores[i]) == gap and scores[res] < scores[i]:
        res = i
        gap = abs(middle - scores[res])
print(middle, res+1)


