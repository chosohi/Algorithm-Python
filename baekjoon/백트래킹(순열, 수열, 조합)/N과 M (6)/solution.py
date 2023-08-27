import sys
sys.stdin = open('baekjoon/백트래킹(순열, 수열, 조합)/N과 M (6)/input.txt', 'r') #file open

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    arr = sorted(list(map(int, input().split())))
    visited = [False for i in range(N+10)]
    res = []

    def recur(cur):
        if len(res) == M :
            print(" ".join(map(str, res)))
            return
        for i in range(cur,N):
            if len(res) and res[-1] > arr[i]:
                continue
            if visited[i]:
                continue
            visited[i]= True
            res.append(arr[i])
            recur(cur+1)
            visited[i] = False
            res.pop()

    recur(0)