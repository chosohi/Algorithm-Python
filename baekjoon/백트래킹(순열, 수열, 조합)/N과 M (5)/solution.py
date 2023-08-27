import sys
sys.stdin = open('baekjoon/백트래킹(순열, 수열, 조합)/N과 M (5)/input.txt', 'r') #file open

# N개의 서로 다른 자연수 중에서 M개를 고른 수열
# 중복되는 수열을 여러 번 출력하면 안됨

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    arr = sorted(list(map(int, input().split())))
    visited = [False for i in range(N+10)]
    res = []

    def recur():
        if len(res) == M :
            print(" ".join(map(str, res)))
            return
        for i in range(N):
            if visited[i]:
                continue
            visited[i]= True
            res.append(arr[i])
            recur()
            visited[i] = False
            res.pop()

    recur()