import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
scores = list(map(int, input().split()))

middle = round(sum(scores) / n)
res = -1
for i in range(len(scores)):
    if abs(scores[i] - middle) 